#!/usr/bin/env python3

import sys
print(sys.argv)


#you really should put some arguments in the PWD or CLI after calling this file

counter = 0
for i in sys.argv:
    counter += 1
    print("argument: {} : {}".format(counter, i))


#adding something to test tracking and commiting
#some more new writing yeehaw