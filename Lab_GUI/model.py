import json

class Airport():
    def __init__(self, id, airport, city, country, iata, icao, latitude, longitude, elevation, utc, dst, region):
        self.id = id
        self.airport = airport
        self.city = city
        self.country = country
        self.iata = iata
        self.icao = icao
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.utc = utc
        self.dst = dst
        self.region = region


    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f"{self.airport} in {self.city}, {self.country}"

    def location(self):
        return (self.latitude, self.longitude)

def get_all_airports():
    """
    Function returns a list of airports
    {'id': 1,
    'airport': 'Goroka Airport',
    'city': 'Goroka',
    'country': 'Papua New Guinea',
    'iata': 'GKA',
    'icao': 'AYGA',
    'latitude': -6.081689834590001,
    'longitude': 145.391998291,
    'elevation': 5282,
    'utc': 10,
    'dst': 'U',
    'region': 'Pacific/Port_Moresby'}
    :return:
    """
    all_data = []
    with open("airports.json", encoding="UTF-8") as raw_file:
        # element1 = list(raw_file)[1]
        # print(element1)
        all_data = json.loads(raw_file.read())
        airports = []
        for arpt in all_data:
            new_air = Airport(arpt['id'], arpt['airport'], arpt['city'], arpt['country'], arpt['iata'], arpt['icao'],
                              arpt['latitude'], arpt['longitude'], arpt['elevation'], arpt['utc'], arpt['dst'],
                              arpt['region'])
            airports.append(new_air)
        return airports

def get_cities():
    airports = get_all_airports()
    return sorted(set(a.city for a in airports))

def get_countries():
    airports = get_all_airports()
    return sorted(set(a.country for a in airports))

# airports_list = read_file()
# for a in list(sorted(airports_list, key=lambda x: x.city)):
#     print(a.city + ', ' + a.airport , end=", \n\n")
# my_set = set(sorted(airports_list, key=lambda a: a.city))
# my_list = list(my_set)[:]
# for c in sorted(my_list, key=lambda a: a.city):
#     print(c.city)

# cities =
# for c in sorted(set(a.city for a in airports_list)):
#     print(c)


