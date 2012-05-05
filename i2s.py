#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from optparse import OptionParser


def q_test():
	return 'qqqq'

def i2s(dig):
	base = (u'',u'один',u'два',u'три',u'четыре',u'пять',u'шесть',u'семь',u'восемь',u'девять');
	ebase = (u'',u'одна',u'две');
	hbase = (u'',u'сто',u'двести',u'триста',u'четыреста',u'пятьсот',u'шестьсот',u'семьсот',u'восемьсот',u'девятьсот');
	dbase = (u'',u'десять',u'двадцать',u'тридцать',u'сорок',u'пятьдесят',u'шестьдесят',u'семьдесят',u'восемьдесят',u'девяносто');
	abase = (u'десять',u'одиннадцать',u'двенадцать',u'тринадцать',u'четырнадцать',u'пятнадцать',u'шестнадцать',u'семнадцать',u'восемнадцать',u'девятнадцать');
	sel_0 = (u'',u'тысяч',u'миллио',u'миллиар');

	ok_2 = (u'нов',u'н',u'на',u'на',u'на',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов')
	ok_2_ext = (u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов',u'нов')

	ok_3 = (u'дов',u'д',u'да',u'да',u'да',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов')
	ok_3_ext = (u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов',u'дов')

	ok_1 = (u'',u'а',u'и',u'и',u'и',u'',u'',u'',u'',u'',u'',u'')
	ok_empty = (u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'',u'')

	s = ''
	s_array = []
	sdig = str(dig)
	l =  len(sdig)

	# print ("Получили=%s!" % dig)

	steps = list()

	for i in range((len(sdig) / 3)+1):
		b = l-(i+1)*3
		steps.append(sdig[(b if b>=0 else 0):(l-(i)*3)])

	step_count = 0
	for step in steps:
		# print ("\t1\t%s" % step)
		# шаг 1 - добиваем до 3 знаков
		l = len(step)
		if l: 
			if l==2:
				step = ("0{}".format(step))
			elif l==1:
				step = ("00{}".format(step))
			# получаем цифры и загоняемы их в массив
			dstep = [int(step[0]),int(step[1]),int(step[2])]	# массив цифр
			# print ("\tСтрока для работы=%s!" % step)
			# print ("\tСтрока для работы=%d %d %d!" % (dstep[0],dstep[1],dstep[2]))

			base1 = hbase
			base2 = dbase
			base3 = base
			sel = sel_0

			# особый случай для десять-девятьнадцать
			if dstep[1]== 1:
				dstep[1] = 0
				base3 = abase

			out_array = [base1[dstep[0]],base2[dstep[1]],base3[dstep[2]]]

			# получаем название триады

			# это случай одна/две. 
			# print ("join=%d %d %d" % (dstep[0],dstep[1],dstep[2]))

			if (dstep[2] == 1  or dstep[2] == 2) and step_count==1 and base3 != abase:
				out_array[2] = ebase[dstep[2]]

			if step_count == 1:
				if base3 == abase:
					ok = ok_empty
				else:
					ok = ok_1
			elif step_count == 2:
				if base3 == abase:
					ok = ok_2_ext
				else:
					ok = ok_2
			elif step_count == 3:
				if base3 == abase:
					ok = ok_3_ext
				else:
					ok = ok_3

			else:
				ok = ok_empty		

			# случай, когда пусто
			if step == "000":
				sel = ok_empty
				ok = ok_empty

			out_array.append(u"{}{}".format(sel[step_count],ok[dstep[2]]))

			# print ("\tПервый вариант: %s" % "_".join(out_array))

			s_array = out_array + s_array

		# увеличивем счетчик  шагов
		step_count=step_count+1
	s = " ".join(s_array)

	s = s.strip()
	s = re.sub('\s\s*',' ',s)

	return s


if __name__ == '__main__':
	print ("Start")
	# a =  12345678;
	# print ("%d = %s" % (a, i2s(a)))

	# a =  12315678;
	# print ("%d = %s" % (a, i2s(a)))


	# a =  7654321;
	# print ("%d = %s" % (a, i2s(a)))

	# a =  1111;
	# print ("%d = %s" % (a, i2s(a)))

	# for i in range(1000000,100000000,1000000):
	# 	# i2s(i)
	# 	print ("!%d!%s!" % (i,i2s(i)))

	parser = OptionParser()
	parser.add_option("--get", dest="d")
	parser.add_option("--beg", dest="b")
	parser.add_option("--end", dest="e")
	parser.add_option("--step", dest="s")
	(options, args) = parser.parse_args()
	if options.d:
		print ("!%s!" % i2s(options.d))
	if options.b and options.e:
		for d in range(int(options.b), int(options.e),(int(options.s) if options.s else 1)):
			print ("!%s!" % i2s(str(d)))

	exit();

	f = open('list_4_test.txt','r')
	for s in f.readlines():
		s = s.rstrip()
		ss = s.split('\t')
		i2s_out = i2s(int(ss[0]))
		if i2s_out != ss[1]:
			print ("Error on %d\n\ti2s=%s\n\tget=%s" % (int(ss[0]),i2s_out,ss[1]))
	f.close()

	print ("Finish")