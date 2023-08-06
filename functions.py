def get_coordinates():

    coordinates = []

    while len(coordinates) != 2:
        coordinates = input().split(" ")

    for i in range(0, len(coordinates)):
        coordinates[i] = float(coordinates[i])

    return coordinates


def line_parameters(point_1, point_2):

    m = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
    n = point_1[1] - point_1[0] * m

    return m, n


def point_in_line(point_coordinates, segment_vertex_1, segment_vertex_2):

    m, n = line_parameters(segment_vertex_1, segment_vertex_2)

    if (point_coordinates[1] == m * point_coordinates[0] + n) and \
            ((segment_vertex_1[0] < point_coordinates[0] < segment_vertex_2[0]) or
             (segment_vertex_2[0] < point_coordinates[0] < segment_vertex_1[0])):
        return True
    return False


def line_with_line(segment_1_vertex_1, segment_1_vertex_2, segment_2_vertex_1, segment_2_vertex_2):

    m1, n1 = line_parameters(segment_1_vertex_1, segment_1_vertex_2)

    if (segment_2_vertex_1[1] < (m1 * segment_2_vertex_1[0] + n1)
            and segment_2_vertex_2[1] > (m1 * segment_2_vertex_2[0] + n1)) \
        or (segment_2_vertex_2[1] < (m1 * segment_2_vertex_2[0] + n1)
            and segment_2_vertex_1[1] > (m1 * segment_2_vertex_1[0] + n1)):

        return True
    return False