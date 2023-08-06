def point_in_line(point_coordinates, segment_vertex_1, segment_vertex_2):

    m = (segment_vertex_2[1] - segment_vertex_1[1])/(segment_vertex_2[0]-segment_vertex_1[0])
    n = segment_vertex_1[1] - segment_vertex_1[0] * m

    if (point_coordinates[1] == m * point_coordinates[0] + n) and \
            ((segment_vertex_1[0] < point_coordinates[0] < segment_vertex_2[0]) or
             (segment_vertex_2[0] < point_coordinates[0] < segment_vertex_1[0])):
        return True
    return False
