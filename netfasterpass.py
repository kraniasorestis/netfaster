#!/bin/python

import time

intro = '''

This is a script that will generate all of the 10.000 possible default
passwords in a Netfaster AP, much like crunch. The only reason this script
exists is because when I tried doing that with crunch, I was getting an error
that didn't seem to be fixable (at the time of writing).

!!!
BE CAREFUL TO:

a) Enter the bssid WITHOUT the colons. That is

b) Enter the bssid CAPITALIZED.

For instance if our target bssid is a5:bA:f3:19:01:5b,
it should be entered like this: A5BAF319015B

'''

def bssid():
    ssid = raw_input("Enter the target's bssid > ")
    tmp = []
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    tmp.append(ssid+'-'+str(b)+str(c)+str(d)+str(e))
    return tmp


def write_out(x):
    mylist = file('Netfaster_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
    mylist.write(x)
    mylist.close
    raw_input("\n\nAll done! Press enter to exit")
    exit()

print intro

our_list = bssid()
our_list = "\n".join(our_list)
write_out(our_list)
