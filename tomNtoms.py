import httplib, urllib2, urllib
from random import randint
from utils import random_phone_number, extract_redirect, extract_user_password

class tomNtoms():

    __headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': 1
    }


    def generate_user_password( self ):
        phone_number = random_phone_number()
        url = "http://172.17.0.1/free_time.cgi?phone={}&phone_user=1&internal=1".format(phone_number)

        conn = urllib2.urlopen(url)

        content = conn.read()
        redirect_url = extract_redirect(content)

        next_url = 'http://172.17.0.1{}'.format(redirect_url)
        print "url to redirect: " + next_url

        conn = urllib2.urlopen(next_url)
        content = conn.read()

        user, password = extract_user_password(content)
        print "user: {} and password: {}".format(user, password)
        return user, password, next_url


    def send_login( self, user, password, referer ):
        headers = self.__headers
        headers['Referer'] = referer


        params = {
                "username": user,
                "password": password
                }

        encode_params = urllib.urlencode(params)
        #req = urllib2.Request(url, encode_params, headers)

        opener = urllib2.build_opener()
        req = urllib2.Request('http://172.17.0.1/weblogin.cgi', encode_params, headers)
        res = opener.open(req)
        print res.read()
