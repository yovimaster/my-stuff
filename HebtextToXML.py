# coding: utf-8
__author__    = 'Yoav T L'

import random
import os
import codecs


print 'working......'


def CreateXml(name,txt):
	trandom = random.randint(1,100000)
	f = open('%s.xml'%name, 'w') 
	f.write('<?xml version="1.0" encoding="UTF-8"?> \n')
	f.write('<add> \n<doc>\n ')
	f.write('<field name="id"> %s </field>\n '%trandom)
	f.write('<field name="content">\n')
	good = txt.decode('cp1255').encode("utf-8")
	f.write('%s'%good)
	f.write(' </field>\n')
	f.write('</doc> \n</add>')
	f.close()




for i in os.listdir(os.getcwd()):
		if i[-3:] == 'txt':
			global readfile
			readfile = open(i,'r')	
			CreateXml(i[:-4],readfile.read())
			readfile.close()

