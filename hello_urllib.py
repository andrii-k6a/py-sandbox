import urllib.request, urllib.parse, urllib.error


def simple_http_request():
    response = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in response:
        print(line.decode().strip())


simple_http_request()
