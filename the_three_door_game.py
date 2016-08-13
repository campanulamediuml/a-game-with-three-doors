# -*- coding:utf-8 -*-  
import time
import random

score = 0
while True:
	print '正在往门后放积分...'
	time.sleep(1)
	print '积分安放完成~'
	print '+---+   +---+  +---+'
	print '|   |   |   |  |   |'
	print '| 1 |   | 2 |  | 3 |'
	print '|   |   |   |  |   |'
	print '+---+   +---+  +---+'

	
	award_door = int(random.uniform(1,4))

	#print award_door  #调试完成后请注释掉

	doors = [1,2,3]
	goats = []
	for i in doors :
		if i != award_door:
			goat_cache = [i]
			goats = goats + goat_cache

	#print goats #调试完成后请注释掉

	time.sleep(0.5)
	choose = raw_input('请挑一扇门：')
	if choose == 'exit':
		quit()
	else:
		choose = int(choose)
		if choose == 1:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '| √ |   |   |  |   |'
			print '+---+   +---+  +---+'
		elif choose == 2:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '|   |   | √ |  |   |'
			print '+---+   +---+  +---+'
		elif choose == 3:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '|   |   |   |  | √ |'
			print '+---+   +---+  +---+'	

		opendoor_list = []
		for i in goats :
			if i != choose :
				opencache = [i]
				opendoor_list = opendoor_list + opencache

	#print opendoor_list #调试完成后请注释掉

	opendoor = random.sample(opendoor_list, 1)
	if opendoor == 1 :
		if choose == 2:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '| × |   | √ |  |   |'
			print '+---+   +---+  +---+'
		elif choose == 3:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '| × |   |   |  | √ |'
			print '+---+   +---+  +---+'
	elif opendoor == 2 :
		if choose == 1:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '| √ |   | × |  |   |'
			print '+---+   +---+  +---+'	
		elif choose == 3:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '|   |   | × |  | √ |'
			print '+---+   +---+  +---+'			
	if opendoor == 3 :
		if choose == 2:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '|   |   | × |  | √ |'
			print '+---+   +---+  +---+'	
		elif choose == 1:
			print '+---+   +---+  +---+'
			print '|   |   |   |  |   |'
			print '| 1 |   | 2 |  | 3 |'
			print '| √ |   |   |  | × |'
			print '+---+   +---+  +---+'


	time.sleep(0.5)
	print '确定吗？'

	time.sleep(0.5)
	print "好的，我现在会从剩下的两扇门中，打开没有积分的那扇门！"

	#print opendoor #调试完成后注释掉
	time.sleep(0.5)
	print '看吧，第',opendoor,'扇门后没有积分'

	time.sleep(0.5)

	
	change = raw_input('那么？现在你打不打算换一扇门？好，请告诉我现在你选哪扇门?')
	choose = int(change)
	if choose == 'exit':
		quit()
	elif choose == award_door:
		time.sleep(0.5)
		print '祝贺你！赢得了100分'
		scorenow = 100
	else:
		time.sleep(0.5)
		print '胜败乃兵家常事，再来一场吧~'

	score = score + scorenow

	print '你当前的分数为',score

	raw_input('按下回车键进入下一回合~')


