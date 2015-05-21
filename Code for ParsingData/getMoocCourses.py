# -*- coding: utf-8 -*-
########################################################################
# BIA660 Mid-term project get information part
# @author 
# Xin Sun, Fangzhou Yan, Hui Zheng, Fei Feng, Changshuo Gao, Yi Wang
# @http://www.mooc-list.com/countrys/usa
#######################################################################
import urllib2

browser=urllib2.build_opener()

browser.addheaders=[('User-agent', 'Mozilla/5.0')]

pagesToGet=49


fileWriter=open('E:\BIA660\Data\mid-term\MoocCourses.txt','w')

string1 ="?sort_by=field_start_date_value&sort_order=DESC&page="

for page in range(0,pagesToGet+1):
 
    url='http://www.mooc-list.com/countrys/usa'+string1 + str(page)
    #print url

    response=browser.open(url)    

    myHTML=response.read()
  
    segments=myHTML.split('<span class="field-content"><a href="/course')

    for j in range(1,len(segments)): 

        segment=segments[j]

        index=segment.find('"')
        
        link= segment[0:index ]

        fileWriter.write('http://www.mooc-list.com/course'+link+'\n')

fileWriter.close()