import csv
import StringIO
import io


def read(string):
    try:
        csv_s = StringIO.StringIO(string)
        reader = csv.reader(csv_s)
        headers = reader
        Data_dict = []
        i = 1
        for line in reader:
            if (i == 1):
                headers = line
                i = i + 1

            else:
                line_as_dict = {}
                for h in headers:
                    line_as_dict[h] = line[headers.index(h)]
                    # print(h, ":",line[h])
                Data_dict.append(line_as_dict)
                i = i + 1
        return Data_dict
    except IOError as e:
        print(e)