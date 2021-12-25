import sys
import zip_util_model as z_model
import postal_codes_moscow_model as pc_model
import zip_app_controller as z_control
import pc_controller as pc_control
import logging

logging.basicConfig(filename="tester.log", level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def check_expected(cmd, result, expected):
    if type(result) != type(expected):
        print('The return value of {} is of type {}, not of type {}'.
              format(cmd, type(result), type(expected)))
    if result != expected:
        print('The return value of {} is {}, expected {}'.
              format(cmd, result, expected))


zip_codes = z_model.read_zip_all()


print(sys.argv[1])

if sys.argv[1] == 'zip_by_location':
    try:
        result = z_control.zip_by_location(zip_codes, ('trOy', 'nY'))
        check_expected(z_control.zip_by_location(zip_codes, ('trOy', 'nY')),
                       result, ['12179', '12180', '12181', '12182', '12183'])
        result = z_control.zip_by_location(zip_codes, ('Mechanicsburg', 'pa'))
        check_expected(z_control.zip_by_location(zip_codes, ('Mechanicsburg', 'pa')), result, ['17055'])
        result = z_control.zip_by_location(zip_codes, ('Helsinki', 'FI'))
        check_expected(z_control.zip_by_location(zip_codes, ('Helsinki', 'FI')), result, [])
    except Exception as e:
        print(e)
elif sys.argv[1] == 'location_by_zip':
    try:
        result = z_control.location_by_zip(zip_codes, '17055')
        check_expected(z_control.location_by_zip(zip_codes, '17055'),
                       result, (40.180953, -77.177086, 'Mechanicsburg', 'PA',
                                'Cumberland'))
        result = z_control.location_by_zip(zip_codes, '96201')
        check_expected(z_control.location_by_zip(zip_codes, '96201'),
                       result, ())
    except Exception as e:
        print(e)
elif sys.argv[1] == 'format_location':
    try:
        location = (40.922326, -72.637078)
        result = z_control.format_location(location)
        check_expected(z_control.format_location(location),
                       result, '(040°55\'20.37"N,072°38\'13.48"W)')

        location = (48.877183, "-102.382327")
        result = z_control.format_location(location)
        check_expected(z_control.format_location(location),
                       result, '(048°52\'37.86"N,102°22\'56.38"W)')
    except Exception as e:
        print(e)
elif sys.argv[1] == 'location_by_postal_code':
    try:
        postal_codes = pc_model.read_postal_codes_all()
        result = pc_control.location_by_postal_code(postal_codes, "111394")
        check_expected(pc_control.location_by_postal_code(postal_codes, "111394"),
                       result, (37.800644, 55.747719, 'район Новогиреево', 'Новогиреевская улица, дом 54',
                                '(495) 302-88-07', 'понедельник 08:00-20:00; вторник 08:00-20:00; среда 08:00-20:00; '
                                'четверг 08:00-20:00; пятница 08:00-20:00; суббота 09:00-18:00; воскресенье выходной',
                                'обед 13:00-14:00'))
        result = pc_control.location_by_postal_code(postal_codes, "127221")
        check_expected(pc_control.location_by_postal_code(postal_codes, "127221"),
                       result, (37.637323, 55.876508, 'район Южное Медведково', 'Полярная улица, дом 16, корпус 1',
                                '(495) 477-13-33', 'понедельник 08:00-20:00; вторник 08:00-20:00; среда 08:00-20:00; '
                                'четверг 08:00-20:00; пятница 08:00-20:00; суббота 09:00-18:00; воскресенье выходной',
                                'обед 13:00-14:00'))
    except Exception as e:
        print(e)
