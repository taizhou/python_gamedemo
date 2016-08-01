#!	/usr/bin/python
#coding=utf-8"

import random


def createball(dict,num,str):
		# create double color ball
		for i in range(1,num):
					if i < 10:
						dict[i] = "%s0%d"%(str,i)
					else:
						dict[i] = "%s%d"%(str,i)
		return


def showball(dict):
		# show ball
		random.shuffle(dict)
		print "中奖号码:",
		for val in dict.values():
			print val,
		return

while 1:
		print "\n------------------"
		print "----双色球摇奖----"
		print "----启动y---------"
		print "----停止n---------"
		print "------------------"
		flag=raw_input()
		if flag.lower() == 'y':
			reddict = {} #红色
			bluedict = {} #蓝色
			dict = {}
			createball(reddict,34,"红")
			createball(bluedict,17,"蓝")
			i = 0
			while i < 6:
				dict[i] = reddict[random.choice(range(1,34))]
				i += 1
			dict[i] = bluedict[random.choice(range(1,17))]
			showball(dict)
		else:
			break


		





