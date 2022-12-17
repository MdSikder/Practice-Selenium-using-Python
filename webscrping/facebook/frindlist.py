import http.cookiejar
import urllib.request
import requests
import bs4

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)

urllib.request.install_opener(opener)

authentication_url = "https://m.facebook.com/login.php"

payload = {

    'email': "01953791444",
    'pass': "01953791444"
}

data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
print(contents)
