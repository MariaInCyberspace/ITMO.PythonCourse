def read_postal_codes_all():
    """
    This function returns a list of postal code information pertinent
        to each post office in the 'Отделения почтовой связи.csv' file (only for Moscow)

    Parameters: no parameters

    :return:
    list: a list of postal code information about each Moscow's post office, e.g.:
    FullName;ShortName;PostalCode;AdmArea;District;Address;AddressExtraInfo;ChiefPhone;
        DeliveryDepartmentPhone;TelegraphPhone;WorkingHours;WorkingHoursExtraInfo;ClassOPS;
        TypeOPS;MMP;CloseFlag;CloseExtraInfo;UNOM;X_WGS84;Y_WGS84;GLOBALID
    """
    postal_codes = []
    with open('Отделения почтовой связи.csv') as raw_file:
        full_file = raw_file.read().split("\n")
        for line in range(0, len(full_file)):
            if line == 0:
                pass
            elif full_file[line] == "":
                pass
            else:
                parts_in_line = full_file[line].split('"')
                detailed_elements = []
                for part in range(0, len(parts_in_line)):
                    if parts_in_line[part] != "":
                        elements = parts_in_line[part].strip().split(";")
                        if part % 2 == 1:
                            detailed_elements.append(parts_in_line[part].strip())
                        else:
                            for elem in range(0, len(elements)):
                                if elem == 0:
                                    if elements[elem] == "":
                                        elements.pop(elem)
                                if elem == len(elements) - 1:
                                    if elements[elem] == "":
                                        elements.pop(elem)
                            if len(elements) > 0:
                                for el in elements:
                                    detailed_elements.append(el.strip())
                postal_codes.append(detailed_elements)

    return postal_codes


