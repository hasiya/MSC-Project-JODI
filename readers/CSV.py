import csv
import simplejson as json

def readFile(file):
    try:
        with open(file,'r') as C_file:
            reader = csv.reader(C_file)
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
                    # print()
            return Data_dict
    except IOError as e:
        print(e)

