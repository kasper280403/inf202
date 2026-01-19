import pathlib
import time
from src.controller import Controller


border_default = [[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]]
run_simulation(50, 0.5, "bay.msh", border_default)




def create_folder(base_name):
    result_path = pathlib.Path(__file__).parent / "results"

    i = 0
    folder_path = None
    while True:
        folder_name = base_name if i == 0 else f"{base_name}{i}"
        folder_path = result_path / folder_name
        if not folder_path.exists():
            break
        i += 1
    folder_path.mkdir(parents=True, exist_ok=False)
    print(f"Simulation saved under results/{folder_name}")

    return folder_path


def run_simulation(n_steps, time_end, mesh_name, borders, log_name = "logfile", write_frequency = None, center_point=None):
    log_folder_path = create_folder(log_name)
    if center_point is None:
        center_point = [0.35, 0.45]
    start_time = time.time()
    controller = Controller()
    controller.set_up_folder()
    controller.set_center_point(center_point)
    mesh_path = pathlib.Path(__file__).parent / "src" / "resources" / mesh_name
    controller.create_cells(mesh_path)
    controller.set_initial_oil_values()
    controller.set_neighbours()
    controller.set_fishing_ground(borders)
    controller.create_image(0, "time: 0.00")
    stop_time = time.time()
    print("Setup took:", stop_time - start_time, "seconds.")
    start_time = time.time()
    controller.run_simulation(time_end, n_steps, 2)
    stop_time = time.time()
    print("Time to run simulation:", stop_time - start_time, "seconds.")
    controller.make_video(log_folder_path, time_end)

