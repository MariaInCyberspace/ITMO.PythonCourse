import zip_util_model as z_model
import postal_codes_moscow_model as pc_model
import zip_app_controller as z_control
import pc_controller as pc_control
import zip_literals as z_lit
import pc_literals as pc_lit
import view as v
import logging.handlers


def handle_input(info):
    return input(info)


def init_zip_app():
    zip_codes = z_model.read_zip_all()
    command = ""
    while command != z_lit.END_COM:
        command = handle_input(z_lit.INPUT_COMMANDS)
        # logging.info(f'Received command {command}')
        logger.info(f'Received command {command}')
        v.display_info(command)
        command = command.strip().lower()
        if command == z_lit.LOC_COM:
            z_control.process_zip(zip_codes)
        elif command == z_lit.ZIP_COM:
            z_control.process_loc(zip_codes)
        elif command == z_lit.DIST_COM:
            z_control.process_dist(zip_codes, logger)
        elif command == z_lit.SWITCH_LANG:
            init_postal_code_app()
            break
        elif command != z_lit.END_COM:
            v.display_info(z_lit.INVALID_COM_MESSAGE)
        print()
    if command == z_lit.END_COM:
        v.display_info(z_lit.DONE_MESSAGE)


def init_postal_code_app():
    postal_codes = pc_model.read_postal_codes_all()

    command = ""
    while command != pc_lit.END_COM:
        command = handle_input(pc_lit.INPUT_COMMANDS)
        # logging.info(f'Received command {command}')
        logger.info(f'Получена команда {command}')
        print(command)
        command = command.strip().lower()
        if command == pc_lit.LOC_COM:
            pc_control.process_postal_code(postal_codes)
        elif command == pc_lit.ZIP_COM:
            pc_control.process_loc(postal_codes)
        elif command == pc_lit.DIST_COM:
            pc_control.process_dist(postal_codes, logger)
        elif command == pc_lit.SWITCH_LANG:
            init_zip_app()
            break
        elif command != pc_lit.END_COM:
            v.display_info(pc_lit.INVALID_COM_MESSAGE)

        print()
    if command == pc_lit.END_COM:
        v.display_info(pc_lit.DONE_MESSAGE)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=5 * 1024 * 1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S",
                        handlers=[rfh])
    logger = logging.getLogger('main')

    choose_version = handle_input(z_lit.CHOOSE_VERSION)

    if choose_version == 'RU'.lower():
        init_postal_code_app()
    else:
        init_zip_app()

    logging.shutdown()
