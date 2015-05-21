#coding=utf-8 

import os,sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


os.chdir('E:\BIA660\Data\mid-term')
inFolder='E:\BIA660\Data\mid-term\MoocPages'
files=os.listdir(inFolder)


countProgramming=0
sumProgramming=0

countEducation=0
sumEducation=0

countBusiness=0
sumBusiness=0

countMath=0
sumMath=0

countHistory=0
sumHistory=0

countEconomics=0
sumEconomics=0

countData=0
sumData=0

countScience=0
sumScience=0

countHealth=0
sumHealth=0

countBiology=0
sumBiology=0


for moocList in files:
    f=open(inFolder+'/'+moocList)
    print '\n\n\n\n',moocList

  
    Length='Unknown'
    EstimatedEffort='Unkown'  
    tags=''
    
    ignoreThisMooclist=False
  
    
    for line in f:
        line=line.strip()
        
        


#Length           
        if line.startswith('<a herf="#" data-original-title="Course Length"'):
            try:
               Length=line[line.rfind('">')+2:line.rfind('</a>')]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break  
            print Length 
                 
             
#EstimatedEffort        
        elif line.find('class="field field-name-field-estimated-effort')!=-1:
            try:
                EstimatedEffort=line[line.rfind('">')+2:line.rfind('</a')] 
            except:
                 exc_type,exc_obj,exc_tb=sys.exc_info()
                 print 'ERROR:'+str(exc_obj),'\nError happened in line:' + str(exc_tb.tb_lineno)
                 ignoreThisMooclist=True
                 break 
            EstimatedEffort=EstimatedEffort.replace('–','-') 
            print EstimatedEffort
            
                           
                  


            
#Tags        
            
        elif line.startswith('<a herf="#" data-original-title="Tags"'):
            try:
                segments=line.split('<a href="/tags/')
                for i in range(1,len(segments)):
                    subtag=segments[i]    
                    subtag=subtag[subtag.find('">')+2:subtag.rfind('</a>')]
                
                    #print subtag
                    if(tags==''):
                       tags=subtag
                    else:
                       tags=tags+' '+subtag   
 
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break 
            print tags
            
           
    segments=tags.split(' ')
    for j in range(0,len(segments)):
            print segments[j]
            if(cmp(Length,'Self Paced')!=0 and cmp(Length,'Course length not available')!=0 and cmp(Length,'Majors')!=0 and cmp( Length,'Minors')!=0 and cmp(EstimatedEffort,'Self study')!=0 and cmp( EstimatedEffort,'No information')!=0 and cmp(EstimatedEffort,'Unkown')!=0):
                if(segments[j]=='Programming'):
                    averageEffort=0.0  
                    countProgramming=countProgramming+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumProgramming=averageEffort*float(Length[0:Length.find(' ')])+sumProgramming
                    #print sumProgramming
                  
                  
                elif(segments[j]=='Education'):
                    averageEffort=0.0  
                    countEducation=countEducation+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumEducation=averageEffort*float(Length[0:Length.find(' ')])+sumEducation
                      
                    
                    
                elif(segments[j]=='Business'):
                    averageEffort=0.0  
                    countBusiness=countBusiness+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumBusiness=averageEffort*float(Length[0:Length.find(' ')])+sumBusiness  
                    
                    
                elif(segments[j]=='Math'):
                    averageEffort=0.0  
                    countMath=countMath+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumMath=averageEffort*float(Length[0:Length.find(' ')])+sumMath
                    
                    
                    
                elif(segments[j]=='History'):
                    averageEffort=0.0  
                    countHistory=countHistory+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumHistory=averageEffort*float(Length[0:Length.find(' ')])+sumHistory
                    
                    
                elif(segments[j]=='Economics'):
                    averageEffort=0.0  
                    countEconomics=countEconomics+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumEconomics=averageEffort*float(Length[0:Length.find(' ')])+sumEconomics
                    
                    
                    
                elif(segments[j]=='Data'):
                    averageEffort=0.0  
                    countData=countData+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumData=averageEffort*float(Length[0:Length.find(' ')])+sumData  
                    
                    
                elif(segments[j]=='Science'):
                    averageEffort=0.0  
                    countScience=countScience+1
                    
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumScience=averageEffort*float(Length[0:Length.find(' ')])+sumScience
                    
                    
                    
                elif(segments[j]=='Health'):
                    averageEffort=0.0  
                    countHealth=countHealth+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumHealth=averageEffort*float(Length[0:Length.find(' ')])+sumHealth
                    
                elif(segments[j]=='Biology'):
                    averageEffort=0.0  
                    countBiology=countBiology+1
                    seg=EstimatedEffort.split()
                    for h in range(0,len(seg)):
                       #print seg[h]
                       if(seg[h].find('-')>=0):
                           startE=EstimatedEffort[0:EstimatedEffort.rfind('-')]
                           endE=EstimatedEffort[EstimatedEffort.find('-')+1:EstimatedEffort.find(' ')]
                           averageEffort=(float(startE)+float(endE))/2
                           break
                       elif(h==len(seg)-1):
                           averageEffort=float(EstimatedEffort[0:EstimatedEffort.find(' ')])
                    
                    print averageEffort
                    sumBiology=averageEffort*float(Length[0:Length.find(' ')])+sumBiology     
                    
                           

    f.close()
    
labels = ('Programming', 'Education', 'Business', 'Math' , 'History' , 'Economics' , 'Data' , 'Science' , 'Health' , 'Biology')

#The positions of each bar on the y-axis (5 bars in this case)
y_pos=[9,8,7,6,5,4,3,2,1,0]

#the age that corresponds to each user
time =[sumProgramming/countProgramming,sumEducation/countEducation,sumBusiness/countBusiness,sumMath/countMath,sumHistory/countHistory,sumEconomics/countEconomics,sumData/countData,sumScience/countScience,sumHealth/countHealth,sumBiology/countBiology] 

#Make random error bars. np.random.rand(x) returns a table of x numbers between 0 and 1
error = np.random.rand(len(labels))

#barh makes the histogram. Alpha tunes the darkness of the color
plt.barh(y_pos, time, xerr=error, align='center', color='blue', alpha=0.4) 

#add the labels
plt.yticks(y_pos, labels)

#Add the label of the x axis
plt.xlabel('Average Effort (Hours)')

#Add the title of the plot
plt.title('Average Effort for Top 10 Tags')

#show the plot
plt.show()



    


