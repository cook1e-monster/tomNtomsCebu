from tomNtoms import tomNtoms
import time

def main():
    while (True):
        toms = tomNtoms()
        user, password, referer = toms.generate_user_password()
        toms.send_login(user, password, referer)

        time_to_sleep = 1805
        print "next connection in {}".format(time_to_sleep)
        time.sleep(time_to_sleep) # delays for 30 seconds


main()
