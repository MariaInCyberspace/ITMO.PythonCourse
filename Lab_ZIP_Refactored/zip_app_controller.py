"""
This is a program to find location by ZIP code and ZIP code by location,
as well as to calculate the distance between to ZIP codes.

U.S. ZIP code is a five-digit integer number.
Location is given by the name of a city/town and a two-letter abbreviation
of the state.

Sample Execution:
-----------------

Command ('loc', 'zip', 'dist', 'end') => loc
loc

Enter a ZIP Code to lookup => 32963
32963
ZIP Code 32963 is in Vero Beach, FL, Indian River county,
coordinates: (027°41'23.23"N,080°22'32.61"W)


Command ('loc', 'zip', 'dist', 'end') => zip
zip

Enter a city name to lookup => Orlando
Orlando

Enter the state name to lookup => FL
FL
The following ZIP Code(s) found for Orlando, FL: 32801, 32802, 32803, 32804, 32805, 32806, 32807, 32808, 32809, 32810,
32811, 32812, 32814, 32815, 32816, 32817, 32818, 32819, 32820, 32821, 32822, 32824, 32825, 32826, 32827, 32828, 32829,
32830, 32831, 32832, 32833, 32834, 32835, 32836, 32837, 32839, 32853, 32854, 32855, 32856, 32857, 32858, 32859, 32860,
32861, 32862, 32867, 32868, 32869, 32872, 32877, 32878, 32886, 32887, 32890, 32891, 32893, 32897, 32898, 32899


Command ('loc', 'zip', 'dist', 'end') => dist
dist

Enter the first ZIP Code => 12180
12180

Enter the second ZIP Code => 32963
32963
The distance between 12180 and 32963 is 1102.72 miles


Command ('loc', 'zip', 'dist', 'end') => end
end

Done

Course: Python
Author(s): Konstantin Kuzmin
Date: 2/19/2019, modified 12/16/2021
"""
import math
import view as v
import zip_literals as lit


def handle_input(message) -> str:
    return input(message)


def calculate_distance(location1, location2):
    """
    This function returns the great-circle distance between location1 and
    location2.

    Parameters:
    location1 (iterable): The geographic coordinates
    of the first location. The first element of the iterable is latitude,
    the second one is longitude.

    location2 (iterable): The geographic coordinates
    of the second location. The first element of the iterable is latitude,
    the second one is longitude.

    Returns:
    float: Value of the distance between two locations computed using
    the haversine formula
    """

    lat1 = math.radians(location1[0])
    lat2 = math.radians(location2[0])
    long1 = math.radians(location1[1])
    long2 = math.radians(location2[1])
    del_lat = (lat1 - lat2) / 2
    del_long = (long1 - long2) / 2
    angle = math.sin(del_lat) ** 2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(del_long) ** 2
    distance = 2 * 3959.191 * math.asin(math.sqrt(angle))
    return distance


def degree_minutes_seconds(location):
    minutes, degrees = math.modf(location)
    degrees = int(degrees)
    minutes *= 60
    seconds, minutes = math.modf(minutes)
    minutes = int(minutes)
    seconds = 60 * seconds
    return degrees, minutes, seconds


def format_location(location):
    l1 = float(location[0])
    l2 = float(location[1])
    ns = ""
    if l1 < 0:
        ns = 'S'
    elif l1 > 0:
        ns = 'N'

    ew = ""
    if l2 < 0:
        ew = 'W'
    elif l1 > 0:
        ew = 'E'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(l1))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(l2))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'


def zip_by_location(codes, location):
    zips = []
    for code in codes:
        if location[0].lower() == code[3].lower() and \
                location[1].lower() == code[4].lower():
            zips.append(code[0])
    return zips


def location_by_zip(codes, zipcode):
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()


def process_loc(codes):
    zipcode = handle_input(lit.ENTER_ZIP_CODE)
    v.display_info(zipcode)
    location = location_by_zip(codes, zipcode)
    if len(location) > 0:
        loc_formatted = format_location((location[0], location[1]))
        v.display_for_zip(zipcode, location, loc_formatted)
    else:
        v.display_info(lit.INVALID_ZIP)


def process_zip(codes):
    city = handle_input(lit.ENTER_CITY)
    v.display_info(city)
    city = city.strip().title()
    state = handle_input(lit.ENTER_STATE)
    v.display_info(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))
    if len(zipcodes) > 0:
        v.display_for_city(city, state, zipcodes)
    else:
        v.display_for_city(city, state)


def process_dist(codes, logger):
    zip1 = handle_input(lit.ENTER_FIRST_ZIP)
    v.display_info(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    logger.info(f'Received the first ZIP {zip1}')
    zip2 = handle_input(lit.ENTER_SECOND_ZIP)
    v.display_info(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    logger.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        v.display_for_dist(zip1, zip2)
    else:
        dist = calculate_distance(location1, location2)
        v.display_for_dist(zip1, zip2, dist)
