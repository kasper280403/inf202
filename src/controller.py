import numpy as np
from src.model.border.border import Border
from src.model.factory.factory import Factory
from src.model.point.point import Point
from src.model.view.createImage import CreateImage
import pathlib
import meshio
import cv2
from natsort import natsorted


def g_function(oil_i, oil_ngh, v_normal, u):
    dot = np.dot(v_normal, u)

    if dot > 0:
        return oil_i * dot
    else:
        return oil_ngh * dot


class Controller:
    """
    A bridge beetween the classes used in the simulation and the main.
    This class aims to simplify the main and make it a readable and clear script.

    Attributes:
        triangle_list (list[Triangle]): A list with instances of the class triangles.
        oil_null_point (list[float]): The center point of the oil spill.
        timeline (list[Dict{}]): The timeline of the oil spill. Each timestep represented by index in list, each triangel with ID in dict.
        next_oil_value (dict{}): The oil values waiting to be added when all the triangles have bben calculated in current timestep.
        timestep (int): The current number of timesteps used.
        timestep_length (float): The length of the timestep used.
        fishing_ground (list[]): The borders of the fishing ground.
    """

    def __init__(self):
        self.triangle_list = None
        self.oil_null_point = [0.35, 0.45]
        self.timeline = []
        self.next_oil_value = {}
        self.timestep = 0
        self.timestep_length = 0.01
        self.fishing_ground = None

    def set_oil_null_point(self, center_point):
        self.oil_null_point = center_point

    def set_initial_oil_values(self):
        value_dict = {}

        for triangle in self.triangle_list:
            midpoint = triangle.get_midpoint()
            distance = (midpoint[0] - self.oil_null_point[0]) ** 2 + (midpoint[1] - self.oil_null_point[1]) ** 2
            oil_value = np.exp(-distance / 0.01)
            triangle.set_oil_value(oil_value)
            value_dict[triangle.get_id] = oil_value

        self.timeline.append(value_dict)

    def set_fishing_ground(self, fishing_ground):
        self.fishing_ground = fishing_ground

    def update_timestep(self):
        self.timestep += 1

    def update_oil_values(self):
        for triangle in self.triangle_list:
            cell_id = triangle.get_id()
            oil_value = self.timeline[self.timestep].get(cell_id)
            triangle.set_oil_value(oil_value)

    def set_neighbours(self):

        for triangle in self.triangle_list:
            for other in self.triangle_list:

                if triangle is other:
                    continue
                elif triangle.get_n_borders() == 3:
                    continue
                elif points := triangle.check_neighbour(other.get_corner_points()):
                    border = Border(points[0], points[1], other, triangle)
                    triangle.add_border(border)

            if triangle.get_n_borders() < 3:
                triangle.finalize_borders()

    def calculate_timestep(self):

        self.update_timestep()

        for triangle in self.triangle_list:
            self.calculate_oil_triangle(triangle)

        for triangle in self.triangle_list:
            triangle.set_oil_value(self.next_oil_value.get(triangle.get_id()))

    def calculate_oil_triangle(self, triangle):

        area_i = triangle.get_area()
        flow_i = np.array(triangle.get_flow())
        oil_i = triangle.get_oil_value()

        flux_list = []
        for border in triangle.get_borders():
            if border.get_neighbour() is not None:
                flux = self.calculate_flux_triangle_edge(border, area_i, flow_i, oil_i)
                flux_list.append(flux)
            """elif border.get_border_type() == "ocean":
                flux = self.calculate_flux_edge(border, area_i, flow_i, oil_i)
                flux_list.append(flux)
            elif border.get_border_type() == "coast":
                continue"""

        oil_value_new = oil_i
        for flux in flux_list:
            oil_value_new = oil_value_new + flux

        self.next_oil_value[triangle.get_id()] = oil_value_new

    def calculate_flux_triangle_edge(self, border, area_i, flow_i, oil_i):
        p_1 = - self.timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = border.get_neighbour().get_oil_value()
        flow_ngh = np.array(border.get_neighbour().get_flow())

        p_2 = g_function(oil_i, oil_ngh, v_normal, (flow_i + flow_ngh) / 2)

        return p_1 * p_2

    def calculate_flux_edge(self, border, area_i, flow_i, oil_i):

        p_1 = - self.timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = 0
        flow_ngh = [0.0, 0.0]

        p_2 = g_function(oil_i, oil_ngh, v_normal, (flow_i + flow_ngh) / 2)

        return p_1 * p_2

    def set_up_folder(self):
        folder = pathlib.Path("src/resources/output")

        folder.mkdir(parents=True, exist_ok=True)

        for item in folder.iterdir():
            if item.is_file():
                item.unlink()

    def create_cells(self, mesh_path):
        mesh = meshio.read(mesh_path)

        point_cells = []
        for point in mesh.points:
            point_cells.append(Point(point))

        factory = Factory()

        triangle_cells = []
        for m in mesh.cells:
            if m.type == "triangle":
                for t in m.data:
                    triangle_cell = factory.create_cell(
                        "triangle",
                        corner_points=[
                            point_cells[t[0]],
                            point_cells[t[1]],
                            point_cells[t[2]],
                        ]
                    )
                    triangle_cells.append(triangle_cell)

        self.triangle_list = triangle_cells

    def run_simulation(self, simulation_length=10, n_simulations=100, n_images=None):
        self.timestep_length = float(simulation_length) / n_simulations
        n_simulations = int(n_simulations)
        for i in range(n_simulations):
            self.calculate_timestep()
            if type(n_images) is int and i % n_images == 0:
                self.create_image(int(i / n_images), f"time = {self.timestep_length * (i + 1):.2f}")

    def create_image(self, img_id, title=None):
        image = CreateImage(self.triangle_list)
        image.plot_Triangles()
        image.plot_line(self.fishing_ground, 'Fishing grounds')
        if title is not None:
            image.set_title(f'{title}')
        image.save_img(f"src/resources/output/image{img_id}.png")

    def make_video(self, name="oil_simulation", vid_length=5.0):
        if self.timestep_length <= 0:
            raise ValueError("timestep_length must be > 0")

        project_root = pathlib.Path(__file__).resolve().parents[1]

        image_dir = project_root / "src" / "resources" / "output"
        video_dir = project_root / "videos"
        video_dir.mkdir(parents=True, exist_ok=True)

        images = natsorted(image_dir.glob("image*.png"))

        if not images:
            raise FileNotFoundError(f"No images found in {image_dir}")

        frame = cv2.imread(str(images[0]))
        if frame is None:
            raise FileNotFoundError(f"Could not read {images[0]}")

        fps = len(images) / vid_length

        height, width, _ = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_path = video_dir / f"{name}.mp4"

        video = cv2.VideoWriter(
            str(video_path),
            fourcc,
            fps,
            (width, height),
        )

        for image in images:
            img = cv2.imread(str(image))
            if img is not None:
                video.write(img)

        video.release()
