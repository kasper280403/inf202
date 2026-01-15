import pathlib
import time
from src.controller import Controller

controller = Controller()

controller.set_up_folder()

controller.set_center_point([0.35, 0.45])

mesh_path = pathlib.Path(__file__).parent / "src" / "resources" / "bay.msh"

controller.create_cells(mesh_path)

controller.set_initial_oil_values()

controller.set_neighbours()

controller.set_fishing_ground([[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]])

start_time = time.time()

controller.run_simulation(0.1, 0.01)

stop_time = time.time()
print(f"Time to run simulation:", stop_time - start_time, "seconds")
