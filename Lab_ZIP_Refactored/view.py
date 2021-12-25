def display_info(info):
    print(info)


def display_for_zip(zipcode, location, loc_formatted):
    if len(location) == 7:
        print('Отделение {}; Район: {}, \nАдрес: {}, Телефон: {}, \nЧасы приема: {}, Перерыв: {},\nкоординаты: {}'.
              format(zipcode, location[2], location[3], location[4], location[5], location[6],
                     loc_formatted))
    else:
        print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: {}'.
          format(zipcode, location[2], location[3], location[4],
                 loc_formatted))


def display_for_district(district, p_codes=None):
    if p_codes is None:
        print(f"Район {district} не найден")
    else:
        print('Район: {}\nВ данном районе найдены следующие отделения: {}'.format(district, ", ".join(p_codes)))


def display_for_city(city, state, zipcodes=None):
    if zipcodes is not None:
        print('The following ZIP Code(s) found for {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        print('No ZIP Code found for {}, {}'.format(city, state))


def display_for_dist(zip1, zip2, dist=None, lang=False):
    if lang:
        if dist is None:
            print('Расстояние между {} и {} не может быть установлено'.
                  format(zip1, zip2))
        else:
            print('Расстояние между {} и {} составляет {:.2f} километров'.
                  format(zip1, zip2, dist))
    else:
        if dist is None:
            print('The distance between {} and {} cannot be determined'.
                  format(zip1, zip2))
        else:
            print('The distance between {} and {} is {:.2f} miles'.
                  format(zip1, zip2, dist))
