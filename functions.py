def get_coordinates():

    coordinates = ""

    while len(coordinates) != 2:
        coordinates = input().split(" ")

    for i in range(0,len(coordinates)):
        coordinates[i] = int(coordinates[i])

    return coordinates
