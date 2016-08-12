"""This function is been used to get api data from api call.
"""
from urllib2 import Request, urlopen, URLError

"""
THe function sends a request to the url parameter and return the data.
"""
def get_api_content(url):
    request = Request(url)
    data = {}

    try:
        response = urlopen(request)
        data = response.read()
        # print data
        # return data
    except URLError, e:
        print 'Got an error code:', e

    return data
