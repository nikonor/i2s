#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def i2s(dig):
	base = ('','один','два','три','четыре','пять','шесть','семь','восемь','девять');
	ebase = ('','одна','две');
	hbase = ('','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот');
	dbase = ('','десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто');
	abase = ('десять','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать');
	sel_0 = ('','тысяч','миллио','');
	ok_2 = ('нов', 'н','на','на','на','нов','нов','нов','нов','нов','нов','нов')
	ok_2_ext = ('нов', 'нов','нов','нов','нов','нов','нов','нов','нов','нов','нов','нов')
	ok_1 = ('', 'а','и','и','и','и','','','','','','')
	ok_empty = ('', '','','','','','','','','','','')

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

			if (dstep[2] == 1  or dstep[2] == 2) and step_count == 1:
				out_array[2] = ebase[dstep[2]]

			if step_count == 1:
				ok = ok_1
			elif step_count == 2:
				if base3 == abase:
					ok = ok_2_ext
				else:
					ok = ok_2
			else:
				ok = ok_empty		

			# случай, когда пусто
			if step == "000":
				sel = ok_empty
				ok = ok_empty

			out_array.append("{}{}".format(sel[step_count],ok[dstep[2]]))

			# print ("\tПервый вариант: %s" % "_".join(out_array))

			s_array = out_array + s_array

		# увеличивем счетчик  шагов
		step_count=step_count+1
	s = " ".join(s_array)

	s = s.strip()
	s = re.sub('\s\s*',' ',s)

	return s


if __name__ == '__main__':
	# print ("Start")
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

	f = open('list_4_test.txt','r')
	for s in f.readlines():
		s = s.rstrip()
		ss = s.split('\t')
		i2s_out = i2s(int(ss[0]))
		if i2s_out != ss[1]:
			print ("Error on %d\n\ti2s=%s\n\tget=%s" % (int(ss[0]),i2s_out,ss[1]))
	f.close()

	print ("Finish")