import pathlib
import time
from src.controller import Controller


border_default = [[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]]
run_simulation(50, 0.5, "bay.msh", border_default)







def run_simulation(n_steps, time_end, mesh_name, borders, log_name = "logfile", write_frequency = None, center_point=None):
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
    stop_time = time.time()
    print("Setup took:", stop_time - start_time, "seconds.")
    start_time = time.time()
    controller.run_simulation(time_end, n_steps, 2)
    stop_time = time.time()
    print("Time to run simulation:", stop_time - start_time, "seconds.")
    controller.make_video()
