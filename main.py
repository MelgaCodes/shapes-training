from shapes import Segment, Point
import isinside

vertex_1_segment_x = input("Insert X coordinate of the first vertex of the segment: ")
vertex_1_segment_y = input("Insert Y coordinate of the first vertex of the segment: ")
vertex_2_segment_x = input("Insert X coordinate of the second vertex of the segment: ")
vertex_2_segment_y = input("Insert Y coordinate of the second vertex of the segment: ")

vertex_1_segment = (float(vertex_1_segment_x), float(vertex_1_segment_y))
vertex_2_segment = (float(vertex_2_segment_x), float(vertex_2_segment_y))

segment = Segment(vertex_1_segment, vertex_2_segment)

point_coordinates = (float(input("Insert the point X coordinate: ")), float(input("Insert the point Y coordinate: ")))
point = Point(point_coordinates)

print(isinside.point_in_line(point.coordinates, segment.vertex_1, segment.vertex_2))
