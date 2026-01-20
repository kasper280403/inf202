"""
This module provides functionality to print a mesh of triangles with
coresponding oil values
"""

import matplotlib.pyplot as plt


class CreateImage():
    """
    Class to print out triangles in a mesh

    Attributes:
        triangles (list[Triangles]):    A list containing all the instances of
                                        triangle class.
        umax (float): maximum value for oil plotting
        umin (float): minimum value for oil plotting
    """

    def __init__(self, TriangleList, umax=1.0, umin=0.0):
        self._triangles = TriangleList
        self._umax = umax
        self._umin = umin

    def plot_Triangles(self):
        """
        Function to plot the triangles stored in the class, with oil values
        """
        plt.figure()

        # Create the colormap
        sm = plt.cm.ScalarMappable(cmap='coolwarm')
        sm.set_array([self._umin, self._umax])

        # adjust position and size as needed
        cbar_ax = plt.gca().inset_axes([1, 0, 0.05, 1])
        plt.colorbar(sm, cax=cbar_ax, label='Oil level')

        for triangle in self._triangles:  # add all the triangles into the plot
            plt.gca().add_patch(
                    plt.Polygon([point.get_coordinates()
                                for point in triangle.get_corner_points()],
                                color=plt.cm.coolwarm(
                                    (triangle.get_oil_value() - self._umin) /
                                    (self._umax - self._umin)),
                                alpha=0.9))
            if triangle.get_in_fg() is True and triangle.get_oil_value() < 0.01:
                plt.gca().add_patch(
                    plt.Polygon([point.get_coordinates()
                                for point in triangle.get_corner_points()],
                                color='green',
                                alpha=0.5))

        # Add labels to axes
        plt.xlabel('x-coord')
        plt.ylabel('y-coord')

        plt.xlim(0, 1)  # set the x-axis limits
        plt.ylim(0, 1)  # set the y-axis limits
        plt.gca().set_aspect('equal')
        plt.gca().set_facecolor('gray')    # set land to gray

        self._plot = plt    # save plot to be accessed later

    def plot_fishing_ground(self, fg, print_txt=''):
        """
        Function to plot given line

        Attributes:
            fish_ground (list[list[float]]): A list containing lists of the different
                                      axis coordinates for the line
            print_txt (Bool): String of text to plot beside the line
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
        Function to save the plotted image to file location

        Attributes:
            file_loc (str): String or path to where to save current image
        """
        self._plot.savefig(file_loc)
        self._plot.close()

    def set_title(self, title):
        """
        Function to set a title in the plotted image

        Attributes:
            title (str): String of the title
        """
        self._plot.title(title)
