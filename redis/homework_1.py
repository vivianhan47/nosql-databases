import urllib2
from ast import literal_eval

url = "https://api.nasa.gov/planetary/apod?date=2017-04-07&api_key=eI5cMXVVbLb1RRE8bJTf3JaXQ379B83HQZVV2TzN"

result = urllib2.urlopen(url).read()


print literal_eval(result)['url']
