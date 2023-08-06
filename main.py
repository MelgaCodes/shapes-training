import shapes
import functions

choice = ''

while choice not in (1, 2):
    choice = int(input("""Select an option
    1 - Point in line.
    2 - Line cross with line
    """))

if choice == 1:
    print("Enter the coordinates of the first point of the segment")
    vertex_1_segment = functions.get_coordinates()
    print("Enter the coordinates of the second point of the segment")
    vertex_2_segment = functions.get_coordinates()

    segment = shapes.Segment(vertex_1_segment, vertex_2_segment)

    print("Enter the coordinates of the point")
    point = shapes.Point(functions.get_coordinates())

    print(segment.vertex_1, segment.vertex_2, point.coordinates)

    print(functions.point_in_line(point.coordinates, segment.vertex_1, segment.vertex_2))

elif choice == 2:
    print("Enter the coordinates of the first point of the first segment")
    vertex_1_segment_1 = functions.get_coordinates()
    print("Enter the coordinates of the second point of the first segment")
    vertex_2_segment_1 = functions.get_coordinates()

    segment_1 = shapes.Segment(vertex_1_segment_1, vertex_2_segment_1)

    print("Enter the coordinates of the first point of the second segment")
    vertex_1_segment_2 = functions.get_coordinates()
    print("Enter the coordinates of the second point of the second segment")
    vertex_2_segment_2 = functions.get_coordinates()

    segment_2 = shapes.Segment(vertex_1_segment_2, vertex_2_segment_2)

    print(segment_1.vertex_1, segment_1.vertex_2, segment_2.vertex_1, segment_2.vertex_2)

    print(functions.line_with_line(segment_1.vertex_1, segment_1.vertex_2, segment_2.vertex_1, segment_2.vertex_2))
