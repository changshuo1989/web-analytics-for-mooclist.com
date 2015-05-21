# -*- coding: utf-8 -*-
########################################################################
# BIA660 Mid-term project get information part
# @author 
# Xin Sun, Fangzhou Yan, Hui Zheng, Fei Feng, Changshuo Gao, Yi Wang
# @http://www.mooc-list.com/countrys/usa
#######################################################################
import urllib2,os,sys

browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

outFolder='E:\BIA660\Data\mid-term\MoocPages'

if not os.path.exists(outFolder): 
    os.mkdir(outFolder) 
    
fileReader=open('E:\BIA660\Data\mid-term\MoocCourses.txt')

for line in fileReader: 
        
        link=line.strip() 
        link = link.replace(' ','%20')
        
        print 'Donwloading: ', link
        
        
        
        try:
            html=browser.open(link).read()
        except:
            print link
            sys.exit()
        name=link[link.rfind('/')+1:]
        
        
        fileWriter=open(outFolder+'/'+name, 'w')
        fileWriter.write(html)
        fileWriter.close()

   
fileReader.close()