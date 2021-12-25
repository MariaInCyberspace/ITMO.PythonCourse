"""
This is a program to find Moscow's post office location by postal code and postal code by location,
as well as to calculate the distance between two postal codes.

Russian postal code is a six-digit integer number.
Location is given by the name of a particular district

Sample Execution:
-----------------

Команда ('район', 'индекс', 'расстояние', 'финиш') => район
район

Введите район => Басманный

Район: Басманный
В данном районе найдены следующие отделения: 101000, 105005, 105062, 105064, 105066, 105082, 107174, 105175, 107450




Команда ('район', 'индекс', 'расстояние', 'финиш') => индекс
индекс

Введите почтовый индекс => 101000
101000
Отделение 101000; Район: Басманный район,
Адрес: Мясницкая улица, дом 26, Телефон: (495) 625-37-48; (495) 625-04-27,
Часы приема: понедельник круглосуточно; вторник круглосуточно; среда круглосуточно; четверг круглосуточно;
пятница круглосуточно; суббота круглосуточно; воскресенье круглосуточно, Перерыв: без перерыва на обед,
координаты: (037°38'13.80"С,055°45'49.90"В)




Команда ('район', 'индекс', 'расстояние', 'финиш') => расстояние
расстояние

Enter the first ZIP Code => 12180
12180

Enter the second ZIP Code => 32963
32963
The distance between 12180 and 32963 is 1102.72 miles


Команда ('район', 'индекс', 'расстояние', 'финиш') => финиш
финиш

Работа завершена

Course: Python
Author(s): Konstantin Kuzmin
Date: 2/19/2019, modified 12/16/2021
"""
import math
import view as v
import pc_literals as pc_lit


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
    angle = math.sin(del_lat)**2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(del_long)**2
    distance = 2 * 6371.0088 * math.asin(math.sqrt(angle))
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
    ns = ""
    if location[0] < 0:
        ns = 'Ю'
    elif location[0] > 0:
        ns = 'С'

    ew = ""
    if location[1] < 0:
        ew = 'З'
    elif location[0] > 0:
        ew = 'В'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(location[0]))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(location[1]))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'


def postal_code_by_location(codes, location):
    p_codes = []
    for code in codes:
        if code[4].lower().__contains__(location.lower()):
            p_codes.append(code[2])
    return p_codes


def location_by_postal_code(codes, postal_code):
    for code in codes:
        if code[2] == postal_code:
            loc1, loc2 = code[18:20]
            distr, addr = code[4:6]
            phone = code[7]
            working_hours, break_time = code[10:12]
            return (float(loc1.replace(",", ".")), float(loc2.replace(",", ".")),
                    distr, addr, phone, working_hours, break_time)
    return ()


def process_loc(codes):
    postal_code = input(pc_lit.ENTER_POSTAL_CODE)
    v.display_info(postal_code)
    location = location_by_postal_code(codes, postal_code)
    if len(location) > 0:
        loc_formatted = format_location((location[0], location[1]))
        v.display_for_zip(postal_code, location, loc_formatted)
    else:
        v.display_info(pc_lit.INVALID_PC)


def process_postal_code(codes):
    district = handle_input(pc_lit.ENTER_DISTRICT)
    v.display_info(district)
    district = district.strip().title()
    postal_codes = postal_code_by_location(codes, district)
    if len(postal_codes) > 0:
        v.display_for_district(district, postal_codes)
    else:
        v.display_for_district(district)


def process_dist(codes, logger):
    pc1 = handle_input(pc_lit.ENTER_FIRST_PC)
    v.display_info(pc1)
    # logging.info(f'Received the first ZIP {zip1}')
    logger.info(f'Получен первый индекс {pc1}')
    pc2 = handle_input(pc_lit.ENTER_SECOND_PC)
    v.display_info(pc2)
    # logging.info(f'Received the second ZIP {pc2}')
    logger.info(f'Получен второй индекс {pc2}')

    location1 = location_by_postal_code(codes, pc1)
    location2 = location_by_postal_code(codes, pc2)
    if len(location1) == 0 or len(location2) == 0:
        v.display_for_dist(pc1, pc2, lang=True)
    else:
        dist = calculate_distance(location1, location2)
        v.display_for_dist(pc1, pc2, dist, lang=True)
