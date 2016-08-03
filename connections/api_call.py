from urllib2 import Request, urlopen, URLError


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

# get_api_content('http://data.aberdeencity.gov.uk/OpenDataService/TemporaryTrafficOrderReport/json')
