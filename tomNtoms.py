import httplib, urllib2, urllib
from random import randint
from utils import random_phone_number, extract_redirect, extract_user_password
import time

class tomNtoms():

    __headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': 1
    }

    __time_to_sleep = 1800
    __user = None
    __password = None
    __referer = None

    def generate_user_password( self ):
        print 'generating user and password'

        phone_number = random_phone_number()

        print "phone number to register is: {}".format(phone_number)
        url = "http://172.17.0.1/free_time.cgi?phone={}&phone_user=1&internal=1".format(phone_number)

        try:
            conn = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.args
        conn = urllib2.urlopen(url)

        content = conn.read()
        redirect_url = extract_redirect(content)

        next_url = 'http://172.17.0.1{}'.format(redirect_url)
        print "url to redirect: " + next_url

        try:
            urllib2.urlopen(next_url)
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.args

        user, password = extract_user_password( content )

        self.__user = user
        self.__password = password
        self.__referer = next_url

        print "user: {} and password: {}".format(user, password)
        return


    def send_login( self ):
        print "sending form to register new number"

        headers = self.__headers
        headers['Referer'] = self.__referer


        params = {
                "username": self.__user,
                "password": self.__password
                }

        encode_params = urllib.urlencode(params)
        #req = urllib2.Request(url, encode_params, headers)

        opener = urllib2.build_opener()
        req = urllib2.Request('http://172.17.0.1/weblogin.cgi', encode_params, headers)

        try:
            opener.open(req)
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.args

        print "Perfect, you have internet now. Enjoy. :)"
        return

    def connect(self):
        while( True ):
            print "connecting ...."
            self.generate_user_password()
            self.send_login()


            print "next connection in {}".format(self.__time_to_sleep)
            time.sleep(self.__time_to_sleep) # delays for 30 mins
