#!/usr/bin/python

import time
import requests


print "Start : %s" % time.ctime()
while 1:
    r = requests.get('http://127.0.0.1')
    print r.status_code
    time.sleep( 15 )

print "End : %s" % time.ctime()
