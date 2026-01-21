import pathlib
import argparse
import time
import tomllib
from src.controller import Controller
from rich.console import Console


def main():
    args = parse_args()

    if args.folder:
        search_directory = pathlib.Path(args.folder)
    else:
        search_directory = pathlib.Path(__file__).parent / "toml_files"
    print("")

    if args.folder and not args.find_all and not args.config_file:
        print("The following config files were found in this folder:")
        for config_file in search_directory.glob("*.toml"):
            print(config_file.name)
    elif args.find_all:
        print(f"Running simulations on all files in: {search_directory}")
        for config_file in search_directory.glob("*.toml"):
            run_file(config_file)
    elif args.config_file:
        run_file(pathlib.Path(args.config_file))
    else:
        default_config = search_directory / "input.toml"
        if default_config.exists():
            run_file(default_config)
        else:
            print("No toml file found")


def run_file(toml_file):
    with toml_file.open("rb") as f:
        config = tomllib.load(f)

        print("")
        print("Running simulation with toml file:", toml_file.name)

        n_steps = config["settings"]["nSteps"]
        time_end = config["settings"]["tEnd"]

        mesh_name = config["geometry"]["meshName"]
        borders = config["geometry"]["borders"]

        log_name = config["IO"].get("logName")
        write_frequency = config["IO"].get("writeFrequency")

        run_simulation(n_steps, time_end, mesh_name, borders, write_frequency, log_name)


def run_simulation(n_steps, time_end, mesh_name, borders, write_frequency=None, log_name=None, center_point=None):
    if log_name is None:
        log_name = "logfile"
    log_folder_path = create_folder(log_name)
    if center_point is None:
        center_point = [0.35, 0.45]
    console = Console()

    start_time = time.time()
    with console.status("[bold cyan]Setting up simulation parameters..."):
        controller = Controller()
        controller.set_up_folder()
        controller.set_oil_null_point(center_point)
        mesh_path = pathlib.Path(__file__).parent / "src" / "resources" / mesh_name
        controller.create_cells(mesh_path)
        controller.set_initial_oil_values()
        controller.set_neighbours()
        controller.set_fishing_ground(borders)
        controller.calculate_triangles_fg()
        controller.config_logger(log_folder_path / f"{log_name}.log", log_name)
        controller.log_variables(n_steps, time_end, mesh_name, borders, log_name, write_frequency)
        controller.log_oil_level(0)
        controller.create_image(0, "time: 0.00")
    stop_time = time.time()
    print(f"Setup took: {(stop_time - start_time):.2f} seconds.")

    start_time = time.time()
    console = Console()
    with console.status("[bold cyan]Running simulation..."):
        controller.run_simulation(time_end, n_steps, write_frequency)
    stop_time = time.time()
    print(f"Simulation finished. Time to run simulation: {(stop_time - start_time):.2f} seconds.")
    print(f"Simulation saved under {log_folder_path.resolve()}")

    if write_frequency is not None:
        controller.make_video(log_folder_path, time_end)
    controller.create_image("final_image", f"time: {time_end:.2f}", log_folder_path)


def create_folder(base_name):
    result_path = pathlib.Path(__file__).parent / "results"

    i = 0
    while True:
        folder_name = base_name if i == 0 else f"{base_name}{i}"
        folder_path = result_path / str(folder_name)
        if not folder_path.exists():
            break
        i += 1
    folder_path.mkdir(parents=True, exist_ok=False)

    folder_path = result_path / folder_name

    return folder_path


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument(
        "--find_all",
        action="store_true",
        help="Finds and runs all .toml files. "
             "If folder is not specified, toml_files is used."
    )

    parser.add_argument(
        "-f", "--folder",
        metavar="FOLDER",
        help="Folder to search for config files"
    )

    parser.add_argument(
        "-c", "--config_file",
        metavar="FILE",
        help="Read a specific config file. "
             "If not specified, defaults to input.toml."
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
