#   https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
#

"""This python file contain readText function which takes a PDF file and page number (optional).
The function reads the file and extract the content of the file.
"""

from cStringIO import StringIO

"""
importing the pdfminer library
"""
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

"""
The pdf Reader function
"""
def readText(fname, pages=None):
    text = ""
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    try:

        infile = file(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close()
    except IOError as e:
        print e
    return text
