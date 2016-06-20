#   https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167

#

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter


from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re


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

