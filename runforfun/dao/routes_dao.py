import csv

class Route:
    def __init__(self, name, distance, elevation, city, url):
        self.name = name
        self.distance = distance
        self.elevation = elevation
        self.city = city
        self.url = url

    def info(self):
        return {
            'name': self.name,
            'distance': self.distance,
            'elevation': self.elevation,
            'city': self.city,
            'url': self.url
        }


def get_suggested_routes(routes_path, desired_distance):
    with open(routes_path) as csv_file:
        routes_reader = csv.reader(csv_file)

        routes = []
        # Skip first row (header)
        next(routes_reader)
        for row in routes_reader:
            distance = float(row[0])
            elevation = row[1]
            name = row[2]
            city = row[3]
            url = row[4]
            if desired_distance > distance - 1 and desired_distance < distance + 1:
                routes.append(Route(name, distance, elevation, city, url))

    return routes
