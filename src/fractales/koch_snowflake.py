import numpy as np
import matplotlib.pyplot as plt

from .base import BaseFractale

    
class KochSnowflake(BaseFractale):
    def __init__(self, order: int):
        super().__init__(title="Koch's Fractal", order=order)

    def _recursive_generate_segments(self, segment, depth):
        # Base case
        if depth == 0:
            return segment
        
        # Recursive case
        start_point, end_point = segment
        segment_vector = end_point - start_point
        segment_length = np.linalg.norm(segment_vector)
        
        # Calculate the center point of the segment
        center_point = start_point + segment_vector / 2
        
        # Calculate the height of the equilateral triangle
        triangle_height = (segment_length / 3) * np.sqrt(3) / 2
        # Calculate the outward-pointing direction vector (perpendicular to the segment)
        outward_direction = np.array([segment_vector[1], -segment_vector[0]]) / segment_length

        # Calculate the apex point of the equilateral triangle
        apex_point = center_point + outward_direction * triangle_height
        # Calculate the division points (two evenly spaced points along the segment)
        division_points = []
        for i in range(1, 3):  # Divide the segment into three equal parts
            division_point = start_point + segment_vector / 3 * i
            division_points.append(division_point)

        # Split the segment and add the equilateral triangle to the list of segments
        s1 = np.array([start_point, division_points[0]])
        s2 = np.array([division_points[0], apex_point])
        s3 = np.array([apex_point, division_points[1]])
        s4 = np.array([division_points[1], end_point])
        segments = np.vstack([
            self._recursive_generate_segments(s1, depth - 1),
            self._recursive_generate_segments(s2, depth - 1),
            self._recursive_generate_segments(s3, depth - 1),
            self._recursive_generate_segments(s4, depth - 1)
        ])

        # Return the coordinates of the three points forming the equilateral triangle
        return np.vstack([start_point, segments, end_point])
        
    def _generate_points(self) -> np.ndarray:
        # Define the vertices of the triangle
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2], [0, 0]])
        points = np.vstack([
            self._recursive_generate_segments(segment=[vertices[0], vertices[1]], depth=self.order),
            self._recursive_generate_segments(segment=[vertices[1], vertices[2]], depth=self.order),
            self._recursive_generate_segments(segment=[vertices[2], vertices[0]], depth=self.order)
        ])
        
        return points
    
    def _specific_plot(self, ax: plt.Axes):
        # Use Polygon to create the shape
        poly = plt.Polygon(self.points, closed=True, edgecolor='blue', fill=None)
        ax.add_patch(poly)
        ax.set_xlim(-0.5, 1.5)
        ax.set_ylim(-0.5, 1.5)

if __name__ == "__main__":
    koch = KochSnowflake(3)
    koch.plot()
    plt.show()