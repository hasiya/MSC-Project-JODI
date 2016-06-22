import csv
# import codecs
import StringIO
# import io
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
#     csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
#     for row in csv_reader:
#         yield [unicode(cell, 'utf-8') for cell in row]
#
# def csv_unireader(f, encoding="utf-8"):
#     for row in csv.reader(codecs.iterencode(codecs.iterdecode(f, encoding), "utf-8")):
#         yield [e.decode("utf-8") for e in row]

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