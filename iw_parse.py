#! /usr/bin/env python

# Hugo Chargois - 17 jan. 2010 - v.0.1
# Parses the output of iwlist scan into a table

# You can add or change the functions to parse the properties
# of each AP (cell) below. They take one argument, the bunch of text
# describing one cell in iwlist scan and return a property of that cell.

def get_name(cell):
    """ Gets the name / essid of a network / cell.
    @param string cell
        A network / cell from iwlist scan.

    @return string
        The name / essid of the network.
    """

    return matching_line(cell, "ESSID:")[1:-1]

def get_quality(cell):
    """ Gets the quality of a network / cell.
    @param string cell
        A network / cell from iwlist scan.

    @return string
        The formatted quality of the network.
    """

    quality = matching_line(cell, "Quality=").split()[0].split("/")
    return str(int(round(float(quality[0]) / float(quality[1]) * 100))) \
            .rjust(3) + " %"

def get_channel(cell):
    """ Gets the channel of a network / cell.
    @param string cell
        A network / cell from iwlist scan.

    @return string
        The channel of the network.
    """

    return matching_line(cell, "Channel:")

def get_encryption(cell):
    """ Gets the encryption type of a network / cell.
    @param string cell
        A network / cell from iwlist scan.

    @return string
        The encryption type of the network.
    """

    enc = ""
    if matching_line(cell, "Encryption key:") == "off":
        enc = "Open"
    else:
        for line in cell:
            matching = match(line,"IE:")
            if matching != None:
                wpa = match(matching,"WPA Version ")
                if wpa != None:
                    enc = "WPA v." + wpa
        if enc == "":
            enc = "WEP"
    return enc

def get_address(cell):
    """ Gets the address of a network / cell.
    @param string cell
        A network / cell from iwlist scan.

    @return string
        The address of the network.
    """

    return matching_line(cell, "Address: ")

# Here you can choose the way of sorting the table. sortby should be a key of
# the dictionary rules.

def sort_cells(cells):
    sortby = "Quality"
    reverse = True
    cells.sort(None, lambda el:el[sortby], reverse)


# Below here goes the boring stuff. You shouldn't have to edit anything below
# this point

def matching_line(lines, keyword):
    """ Returns the first matching line in a list of lines.
    @see match()
    """
    for line in lines:
        matching = match(line,keyword)
        if matching != None:
            return matching
    return None

def match(line, keyword):
    """ If the first part of line (modulo blanks) matches keyword,
    returns the end of that line. Otherwise returns None"""

    line = line.lstrip()
    length = len(keyword)
    if line[:length] == keyword:
        return line[length:]
    else:
        return None

def parse_cell(cell, rules):
    """ Applies the rules to the bunch of text describing a cell.
    @param string cell
        A network / cell from iwlist scan.
    @param dictionary rules
        A dictionary of parse rules.

    @return dictionary
        parsed networks. """

    parsed_cell = {}
    for key in rules:
        rule = rules[key]
        parsed_cell.update({key: rule(cell)})
    return parsed_cell

def print_table(table):
    # Functional black magic.
    widths = map(max, map(lambda l: map(len, l), zip(*table)))

    justified_table = []
    for line in table:
        justified_line = []
        for i, el in enumerate(line):
            justified_line.append(el.ljust(widths[i] + 2))
        justified_table.append(justified_line)

    for line in justified_table:
        for el in line:
            print el,
        print

def print_cells(cells, columns):
    table = [columns]
    for cell in cells:
        cell_properties = []
        for column in columns:
            cell_properties.append(cell[column])
        table.append(cell_properties)
    print_table(table)

def get_parsed_cells(iw_data, rules=None):
    """ Parses iwlist output into a list of networks.
        @param str iw_data
            Output from iwlist scan.

        @return list
            properties: Name, Address, Quality, Channel, Encryption.
    """

    # Here's a dictionary of rules that will be applied to the description
    # of each cell. The key will be the name of the column in the table.
    # The value is a function defined above.
    rules = rules or {
        "Name": get_name,
        "Quality": get_quality,
        "Channel": get_channel,
        "Encryption": get_encryption,
        "Address": get_address,
    }

    cells = [[]]
    parsed_cells = []

    for line in iw_data:
        cell_line = match(line, "Cell ")
        if cell_line != None:
            cells.append([])
            line = cell_line[-27:]
        cells[-1].append(line.rstrip())

    cells = cells[1:]

    for cell in cells:
        parsed_cells.append(parse_cell(cell, rules))

    sort_cells(parsed_cells)
    return parsed_cells
