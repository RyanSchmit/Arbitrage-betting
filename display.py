# Defines functions that help write the current arbitage oportunities 
# to csv file 

def write_csv(rows, filename):
    """
    Write integers to a Comma-Separated Value file.
    TODO: Complete this function.
    :param rows: A list of rows to be written, where each row is a dictionary
                 mapping column names to cell values
    :param filename: A desired CSV's filename
    """
    keys = rows[0].keys()
    keys_str = ','.join(map(str, keys))
    keys_str.strip()

    values = []
    for row in rows:
       curr = []
       for key in keys:
           curr.append(row[key])
       values.append(curr)
    with open(filename, "w") as file:
        file.write(keys_str)
        file.write("\n")
        for row in values:
            values_str = ','.join(map(str, row))
            values_str.strip()
            file.write(values_str)
            file.write("\n")
