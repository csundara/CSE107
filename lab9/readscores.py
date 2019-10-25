def read_scores(lines):
    """This function takes a list of strings that represent whitespace-
    separated data. Returns a list of dictionaries.
    """
    data = []

    for line in lines:
        values = line.split('\t')

        # Creates an empty dictionary
        row = dict()

        row["state"] = values[0]
        row["act_percent_taking"] = values[1]
        row["act_average_score"] = values[2]
        row["sat_percent_taking"] = values[3]
        row["sat_average_math"] = values[4]
        row["sat_average_reading"] = values[5]
        row["sat_average_writing"] = values[6]
        data.append(row)

    return data


def test():
    # TODO This should be a with-statement.
    # TODO What if the file doesn't exist? What if the filename is a directory
    # and not a file? Make sure you catch exceptions when opening this file.
    try:
        with open("actsat.txt") as f:
            # This is a list of strings.
            lines = f.readlines()

            for data_row in read_scores(lines):
                print(data_row)
    except FileNotFoundError:
        print('File \'actsat.txt\' does not exist')

        # TODO call the test() function


if __name__ == "__main__":
    test()
