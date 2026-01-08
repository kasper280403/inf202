import matplotlib.pyplot as plt
import numpy as np


class CreateImage():
    """
    Class to print out triangles in a mesh
    """

    def __init__(self, TriangleList):
        self._triangles = TriangleList  # get a list of triangles can be done multiple ways
        self._umax = 1.0
        self._umin = 0.0
        self._u = 0.0




    def plot_Triangles(self):  # Plot the mesh by adding all triangles with their value
        plt.figure()

        # Create the colormap
        sm = plt.cm.ScalarMappable(cmap='viridis')
        sm.set_array([self._umin, self._umax])

        cbar_ax = plt.gca().inset_axes([1, 0, 0.05, 1])  # adjust position and size as needed
        plt.colorbar(sm, cax=cbar_ax, label='Oil level')

        for triangle in self._triangles:
            plt.gca().add_patch(plt.Polygon(([point.get_coordinates() for point in triangle.get_corner_points()]),
                                            color=plt.cm.viridis((triangle.get_oil_value() - self._umin) / (self._umax - self._umin)),
                                            alpha=0.9))
        # Add labels to axes
        plt.xlabel('x-coord')
        plt.ylabel('y-coord')

        plt.xlim(0, 1)  # set the x-axis limits
        plt.ylim(0, 1)  # set the y-axis limits
        plt.gca().set_aspect('equal')
        # Show plot
        plt.show()

    def save_img(self, file_loc):
        # Show plot
        plt.savefig(file_loc)
