#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import numeral
import re
from i2s import i2s
import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, b,e,a):
        
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name
        self.b = b
        self.e = e
        self.a = a


    def run(self):
        print ("Starting " + self.name)
        tt(self.b,self.e,self.a)
        print ("Exiting " + self.name)


def tt(b,e,a):
	i = b
	while i < e:
		s_i2s = i2s(i)
		s_pytils = numeral.in_words(i)
		if (s_pytils != s_i2s):
			print ("\tError on %d\n\t\ti2s\t!%s!\n\t\tpytils\t!%s!\n" % ((i),s_i2s,s_pytils))
		i += a 


if __name__ == '__main__':
	print ("Start Main Thread")
	tests = ((1,1000,1),
			(1000,1000000,999),
			(1000000,999000000,999999),
			(1000000000,999999999999,123456789))

	for b,e,a in tests:
		print ("call with b={}, e={}, a={}".format(b,e,a))
		a = myThread(b,"myThread{}".format(b),b,e,a)
		# print ("Now activ is {} threads".format(threading.activeCount()))
		a.start()



	print ("Finish Main Thread")
