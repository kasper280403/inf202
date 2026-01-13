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
        sm = plt.cm.ScalarMappable(cmap='coolwarm')
        sm.set_array([self._umin, self._umax])

        cbar_ax = plt.gca().inset_axes([1, 0, 0.05, 1])  # adjust position and size as needed
        plt.colorbar(sm, cax=cbar_ax, label='Oil level')

        for triangle in self._triangles:
            plt.gca().add_patch(plt.Polygon(([point.get_coordinates() for point in triangle.get_corner_points()]),
                                            color=plt.cm.coolwarm((triangle.get_oil_value() - self._umin) / (self._umax - self._umin)),
                                            alpha=0.9))
        # Add labels to axes
        plt.xlabel('x-coord')
        plt.ylabel('y-coord')

        plt.xlim(0, 1)  # set the x-axis limits
        plt.ylim(0, 1)  # set the y-axis limits
        plt.gca().set_aspect('equal')
        plt.gca().set_facecolor('green')
        # Show plot
        self._plot = plt

    def plot_line(self,line,print_txt = False):
        self._plot.plot(line[0],line[1], linewidth = 2, color = 'red')
        if print_txt == True:
            self._plot.text(line[1][0],line[1][1]+0.02, 'Fishing grounds', color ='red')

    def plot_normals(self,triangle):
        tri = self._triangles[triangle]
        borders = tri.get_borders()
        for i in range(3):
            norm = borders[i].get_normal()
            p1 = borders[i].get_points()[0].get_coordinates()
            p2 = borders[i].get_points()[1].get_coordinates()
            midt = [(p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0]
            self._plot.arrow(midt[0], midt[1], norm[0], norm[1], head_width=0.006, head_length=0.002, fc=['red','green','blue'][i], ec=['red','green','blue'][i])
            
            

    def show_img(self):
        self._plot.show()

    def save_img(self, file_loc):
        # Show plot
        self._plot.savefig(file_loc)
