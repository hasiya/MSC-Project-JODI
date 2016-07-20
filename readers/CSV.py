import csv
# import codecs
import StringIO
# import io
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def read(string):
    try:
        csv_s = StringIO.StringIO(string)
        reader = csv.reader(csv_s)
        headers = reader
        Data_dict = []
        i = 1
        for line in reader:
            if i == 1:
                headers = line
                i += 1

            else:
                line_as_dict = {}
                for h in headers:
                    new_h = h
                    new_h = new_h.lstrip().rstrip()
                    line_as_dict[new_h] = line[headers.index(h)]
                    # print(h, ":",line[h])
                Data_dict.append(line_as_dict)
                i += 1
        return Data_dict
    except IOError as e:
        print(e)
