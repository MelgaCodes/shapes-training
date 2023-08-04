import shapes, isinside, functions

print("Enter the coordinates of the first point of the segment")
vertex_1_segment = functions.get_coordinates()
print("Enter the coordinates of the second point of the segment")
vertex_2_segment = functions.get_coordinates()

segment = shapes.Segment(vertex_1_segment, vertex_2_segment)

print("Enter the coordinates of the point")
point = shapes.Point(functions.get_coordinates())

print(point.coordinates, segment.vertex_1, segment.vertex_2)

print(isinside.point_in_line(point.coordinates, segment.vertex_1, segment.vertex_2))
