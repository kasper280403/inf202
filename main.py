import pathlib
import time
from src.controller import Controller

start_time = time.time()

controller = Controller()

controller.set_up_folder()

controller.set_center_point([0.35, 0.45])

mesh_path = pathlib.Path(__file__).parent / "src" / "resources" / "bay.msh"

controller.create_cells(mesh_path)

controller.set_initial_oil_values()

controller.set_neighbours()

controller.set_fishing_ground([[0.0, 0.0, 0.45, 0.45, 0.0],
                               [0.0, 0.2, 0.2, 0.0, 0.0]])

stop_time = time.time()
print("Setup took:", stop_time - start_time, "seconds.")

start_time = time.time()

controller.run_simulation(0.5, 50, 2)

stop_time = time.time()
print("Time to run simulation:", stop_time - start_time, "seconds.")

controller.make_video()
