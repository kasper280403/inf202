import pathlib
from src.model.view.createImage import CreateImage
from src.controller import Controller
import time


controller = Controller([0.35, 0.45])

mesh_path = pathlib.Path(__file__).parent / "src" / "resources" / "bay.msh"

controller.create_cells(mesh_path)

controller.set_up_folder()

controller.set_initial_oil_values()

controller.set_neighbours()

start_time = time.time()
fishing_ground = [[0.0, 0.0, 0.45, 0.45, 0.0], [0.0, 0.2, 0.2, 0.0, 0.0]]
# triangle_cells[1].set_oil_value(1.0)

image = CreateImage(triangle_cells)
image.plot_Triangles()
# image.plot_normals(5)

image.plot_line(fishing_ground, print_txt=True)
image.save_img("src/resources/output/image1.png")
stop_time = time.time()
print("Time:", stop_time - start_time, "seconds")

for triangle in triangle_cells[:10]:
    print(f"Triangle: {triangle.get_id()}, oilvalue: {triangle.get_oil_value()}")

print("\n\n Calculating timesteps \n\n")



start_time = time.time()

run_simulation(5, 0.01)

stop_time = time.time()
print(f"Time to run {i} simulations:", stop_time - start_time, "seconds")

def run_simulation(simulation_length, step_size):
    n_simulations = int(simulation_length / step_size)
    for _ in range(n_simulations):
        controller.calculate_timestep()
        image = CreateImage(triangle_cells)
        image.plot_Triangles()
        image.plot_line(fishing_ground, print_txt=True)
        image.save_img(f"src/resources/output/image{i}.png")