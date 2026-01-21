import numpy as np
from src.model.border.border import Border
from src.model.factory.factory import Factory
from src.model.point.point import Point
from src.model.view.createImage import CreateImage
import pathlib
import meshio
import cv2
from natsort import natsorted
import logging


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
        logger (logger): logger used to log the result of the simulation over time
    """

    def __init__(self):
        self._triangle_list = None
        self._oil_null_point = [0.35, 0.45]
        self._timeline = []
        self._next_oil_value = {}
        self._timestep = 0
        self._timestep_length = 0.01
        self._fishing_ground = None
        self._logger = None

    def set_oil_null_point(self, center_point):
        self._oil_null_point = center_point

    def set_initial_oil_values(self):
        """
        Calculates the initial oil values, according to the formula provided.
        Adds the inital oil value to the timeline.
        """
        value_dict = {}

        for triangle in self._triangle_list:
            midpoint = triangle.get_midpoint()
            distance = (midpoint[0] - self._oil_null_point[0]) ** 2 + (midpoint[1] - self._oil_null_point[1]) ** 2
            oil_value = np.exp(-distance / 0.01)
            triangle.set_oil_value(oil_value)
            value_dict[triangle.get_id] = oil_value

        self._timeline.append(value_dict)

    def set_fishing_ground(self, fishing_ground):
        self._fishing_ground = fishing_ground

    def update_timestep(self):
        self._timestep += 1

    def update_oil_values(self):
        """
        Loops through the triangle_list and updates the oil values from the latest timestep.
        """
        for triangle in self._triangle_list:
            cell_id = triangle.get_id()
            oil_value = self._timeline[self._timestep].get(cell_id)
            triangle.set_oil_value(oil_value)

    def set_neighbours(self):
        """
        Loops through the triangle_list and finds the neighbours of each triangle.
        """
        for triangle in self._triangle_list:
            for other in self._triangle_list:

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
        """
        Excecutive function to calculate the next timestep for all the triangles.
        Loops through the triangle_list and calls the calculate_oil_triangle() function.
        Loops through the triangle_list and updates each Triangle with new value.
        """
        self.update_timestep()

        for triangle in self._triangle_list:
            self.calculate_oil_triangle(triangle)

        for triangle in self._triangle_list:
            triangle.set_oil_value(self._next_oil_value.get(triangle.get_id()))

        self.calculate_triangles_fg()

    def calculate_oil_triangle(self, triangle):
        """
        Takes a single Triangle and calls the calculate_flux_triangle_edge on all sides.
        Calculates the next oil value in the Triangle based on the 3 fluxes and adds to the next_oil_value

        Args:
            triangle (Triangle): The triangle to calculate the oil value for.
        """
        area_i = triangle.get_area()
        flow_i = np.array(triangle.get_flow())
        oil_i = triangle.get_oil_value()

        flux_list = []
        for border in triangle.get_borders():
            flux = self.calculate_flux_triangle_edge(border, area_i, flow_i, oil_i)
            flux_list.append(flux)

        oil_value_new = oil_i
        for flux in flux_list:
            oil_value_new = oil_value_new + flux

        self._next_oil_value[triangle.get_id()] = oil_value_new

    def calculate_flux_triangle_edge(self, border, area_i, flow_i, oil_i):
        """
        Calculates flux over an edge of the triangle.

        Args:
            border (Border): A instance of the class Border belonging to the Triangle.
            area_i (float): The area of Triangle.
            flow_i (np.array[float]): The flow of the Triangle.
            oil_i (float): The oil value of the Triangle.

        Returns:
            float: The flux over the edge of the Triangle.
        """
        p_1 = - self._timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = border.get_neighbour().get_oil_value()
        flow_ngh = np.array(border.get_neighbour().get_flow())

        p_2 = self.g_function(oil_i, oil_ngh, v_normal, (flow_i + flow_ngh) / 2)

        return p_1 * p_2

    def calculate_flux_edge(self, border, area_i, flow_i, oil_i):

        p_1 = - self._timestep_length / area_i

        v_normal = border.get_normal()
        oil_ngh = 0
        flow_ngh = [0.0, 0.0]

        p_2 = self.g_function(oil_i, oil_ngh, v_normal, (flow_i + flow_ngh) / 2)

        return p_1 * p_2

    def g_function(self, oil_i, oil_ngh, v_normal, u):
        """
        Simplifies the calculate_flux_triangle_edge function, by doing some of the math operations.
        """
        dot = np.dot(v_normal, u)

        if dot > 0:
            return oil_i * dot
        else:
            return oil_ngh * dot

    def set_up_folder(self):
        """
        Empties if exists or creates the folder to store the images for the simulation
        """
        folder = pathlib.Path("src/resources/output")

        folder.mkdir(parents=True, exist_ok=True)

        for item in folder.iterdir():
            if item.is_file():
                item.unlink()

    def create_cells(self, mesh_path):
        """
        Reads the mesh file and creates the instances of the Triangles.
        Adds the Triangles to the triangle_list.

        Args:
            mesh_path (pathlib.Path): The path to the mesh file.
        """
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

        self._triangle_list = triangle_cells

    def run_simulation(self, simulation_length=10, n_simulations=100, sim_per_img=None):
        """
        Runs the simulation until it reaches the desired length, with the specified number of simulations.
        Creates images, with the specified number of simulation per image.

        Attributes:
            simulation_length (float): The length of the simulation in seconds.
            n_simulations (int): The number of simulation steps to run.
            write_frequency (int): The number of simulations to calculate per image.
        """
        if sim_per_img == 0:
            sim_per_img = None
        self._timestep_length = float(simulation_length) / n_simulations
        n_simulations = int(n_simulations)
        for i in range(n_simulations):
            self.calculate_timestep()
            time = self._timestep_length * (i + 1)
            self.log_oil_level(time)
            if type(sim_per_img) is int and (i+1) % sim_per_img == 0:
                self.create_image(int((i+1.0)/sim_per_img), f"time = {time:.2f}")

    def create_image(self, img_id, title=None, save_path=None):
        """
        Creates an image of the current oil distribution.

        Attributes:
            img_id (float): Added to the end of the image as a way to order them.
            title (string): Optional title added to the image
            save_path (pathlib.Path): Path to the folder the image is saved in, optional.
        """
        image = CreateImage(self._triangle_list)
        image.plot_triangles()
        image.plot_fishing_ground(self._fishing_ground, 'Fishing grounds')
        if title is not None:
            image.set_title(f'{title}')
        if save_path is not None:
            image.save_img(save_path / f'{img_id}.png')
        else:
            image.save_img(f"src/resources/output/image{img_id}.png")

    def make_video(self, log_folder_path, vid_length=5.0, name="oil_simulation"):
        """
        Creates a video using all the images added to the output folder.
        Optional to add name and length to the video, else default is used.

        Attributes:
            log_folder_path (pathlib.Path): The path to the folder the video is saved in.
            vid_length (float): The length of the video in seconds.
            name (string): The name of the video file, optional.
        """
        if self._timestep_length <= 0:
            raise ValueError("timestep_length must be > 0")

        project_root = pathlib.Path(__file__).resolve().parents[1]

        image_dir = project_root / "src" / "resources" / "output"

        images = natsorted(image_dir.glob("image*.png"))

        if not images:
            raise FileNotFoundError(f"No images found in {image_dir}")

        frame = cv2.imread(str(images[0]))
        if frame is None:
            raise FileNotFoundError(f"Could not read {images[0]}")

        fps = len(images) / (vid_length*10.0)

        height, width, _ = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video_path = log_folder_path / f"{name}.mp4"

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

    def config_logger(self, filename, logname):
        """
        Configure the logger to log info in given filename

        Attributes:
            filename (str): filename of log to write to
        """
        self._logger = logging.getLogger(logname)
        self._logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(logging.INFO)

        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        self._logger.addHandler(file_handler)

    def log_variables(self, nSteps, tEnd, meshName, borders, logName, writeFrequency):
        self._logger.info(f"settings: nSteps={nSteps}, tEnd={tEnd}")
        self._logger.info(f"geometry: meshName={meshName}, borders={borders}")
        self._logger.info(f"IO: logName={logName}, writeFrequency={writeFrequency}")

    def calculate_triangles_fg(self):
        """
        Loops through all triangles and calculates if it is in the fishing grounds.
        """
        for triangle in self._triangle_list:
            triangle.calculate_in_fg(self._fishing_ground)

    def log_oil_level(self, time):
        """
        logs the current oil values to logging file

        Attributes:
            time (float): current time in the simulation
        """
        sum_oil = 0
        sum_area = 0
        for triangle in self._triangle_list:
            if triangle.is_in_fg() is True:
                sum_area = sum_area + triangle.get_area()
                if triangle.get_oil_value() > 0.01:
                    sum_oil = sum_oil + triangle.get_area()
        percentage = sum_oil / sum_area * 100
        self._logger.info(
            f"t:{time:.3f} Area of oil in fishing grounds {sum_oil:.3f} / {sum_area:.3f} ({percentage:.0f}%)")
