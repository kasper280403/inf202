import matplotlib.pyplot as plt


class CreateImage:
    """
    This class provides functionality to print a mesh of triangles with
    coresponding oil values

    Attributes:
        _plot: plt: The matplotlib plot
        _triangles (list[Triangles]): List containing all  instances of Triangle.
        _umax (float): maximum value for oil plotting
        _umin (float): minimum value for oil plotting
    """

    def __init__(self, triangle_list, umax=1.0, umin=0.0):
        self._plot = None
        self._triangles = triangle_list
        self._umax = umax
        self._umin = umin

    def plot_triangles(self):
        """
        Function to plot the triangles stored in the class, with oil values
        Saves the plot in  _plot
        """
        plt.figure()

        # Create the colormap
        sm = plt.cm.ScalarMappable(cmap='coolwarm')
        sm.set_array([self._umin, self._umax])

        # adjust position and size as needed
        cbar_ax = plt.gca().inset_axes([1.0, 0.0, 0.05, 1.0])
        plt.colorbar(sm, cax=cbar_ax, label='Oil value')

        for triangle in self._triangles:  # add all the triangles into the plot
            plt.gca().add_patch(
                plt.Polygon([point.get_coordinates()
                             for point in triangle.get_corner_points()],
                            color=plt.cm.coolwarm(
                                (triangle.get_oil_value() - self._umin) /
                                (self._umax - self._umin)),
                            alpha=0.9))
            if triangle.is_in_fg() is True and triangle.get_oil_value() < 0.001:
                plt.gca().add_patch(
                    plt.Polygon([point.get_coordinates()
                                 for point in triangle.get_corner_points()],
                                color='green',
                                alpha=0.5))

        # Add labels to axes
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')

        plt.xlim(0, 1)  # set the x-axis limits
        plt.ylim(0, 1)  # set the y-axis limits
        plt.gca().set_aspect('equal')
        plt.gca().set_facecolor('gray')  # set land to gray

        self._plot = plt  # save plot to be accessed later

    def plot_fishing_ground(self, fg, print_txt=""):
        """
        Function to plot given line

        Attributes:
            fg (list[list[float]]): List with borderlines for the fishing ground
            print_txt (str): String of text to plot beside the line
        """
        x_values = [fg[0][0], fg[0][0], fg[0][1], fg[0][1], fg[0][0]]
        y_values = [fg[1][0], fg[1][1], fg[1][1], fg[1][0], fg[1][0]]
        self._plot.plot(x_values, y_values, linewidth=2, color='red')
        if len(print_txt) != 0:
            self._plot.text(x_values[1] + 0.01, y_values[1] + 0.02,
                            print_txt,
                            color='red'
                            )

    def save_img(self, file_loc):
        """
        Saves the plotted image to specified file location

        Attributes:
            file_loc (str): String or path to the save location
        """
        self._plot.savefig(file_loc)
        self._plot.close()

    def set_title(self, title):
        """
        Sets the title in the plotted image

        Attributes:
            title (str): The title
        """
        self._plot.title(title)
