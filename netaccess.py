#!/usr/bin/python
from requests import session
import httplib
import urllib2, urllib
import sys
from time import sleep
login = {
    'submit': '',
    'userLogin': 'rollNum',
    'userPassword': 'userPassword'
}
approv = {
    'duration': '2',
    'approveBtn': '',
}
print ("\n\n\n\n\033[1;33;40m                                                                    \n"
                            "     _   _        _     ___                                         \n"
                            "    | \\ | |      | |   / _ \\                                        \n"
                            "    |  \\| |  ___ | |_ / /_\\ \\  ___   ___   ___  ___  ___            \n"
                            "    | . ` | / _ \\| __||  _  | / __| / __| / _ \\/ __|/ __|           \n"
                            "    | |\\  ||  __/| |_ | | | || (__ | (__ |  __/\\__ \\\\__ \\           \n"
                            "    \\_| \\_/ \\___| \\__|\\_| |_/ \\___| \\___| \\___||___/|___/           \n"
                            "                                                                    \n"
                            "                                                                    \n\033[0m")

for i in range(10):
    with session() as c:
        try:
            c.post('https://netaccess.iitm.ac.in/account/login', data=login)
            response = c.post('https://netaccess.iitm.ac.in/account/approve', data=approv)
            print ("\n\033[1;32m                                                        \n"
                            "                                                           \n"
                            "      db    888b. 888b. 888b. .d88b. Yb    dP 8888 888b.   \n"
                            "     dPYb   8  .8 8  .8 8  .8 8P  Y8  Yb  dP  8www 8   8   \n"
                            "    dPwwYb  8wwP' 8wwP' 8wwK' 8b  d8   YbdP   8    8   8   \n"
                            "   dP    Yb 8     8     8  Yb `Y88P'    YP    8888 888P'   \n"
                            "                                                           \n\033[0m")
            sleep(2)
            sys.exit(0)
        except Exception:
            print "\033[1;31m Error Approving NetAccess!\n Check your connection\033[0m\n"
        for i in range(5):
            sys.stdout.write("\r\033[3mRetrying in %ds...\033[0m" % (5-i))
            sys.stdout.flush()
            sleep(1)
        print "\n\nRetrying..."
print "\nExiting..."
