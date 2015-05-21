# -*- coding: utf-8 -*-
########################################################################
# BIA660 Mid-term project get information part
# @author 
# Xin Sun, Fangzhou Yan, Hui Zheng, Fei Feng, Changshuo Gao, Yi Wang
# @http://www.mooc-list.com/countrys/usa
# @Data
#  Discreption, MoreInformation, Initiative, University, Instructors, Categories, Date, Length, 
#  EstimatedEffort, RecommendedBackground, Certificate, 
#  Exam, Country, Language, Tags
#######################################################################

import os,sys
os.chdir('E:\BIA660\Data\mid-term')
inFolder='E:\BIA660\Data\mid-term\MoocPages'
files=os.listdir(inFolder)
fw=open('E:\BIA660\Data\mid-term\Info.txt','w')

for moocList in files:
    f=open(inFolder+'/'+moocList)
    print '\n\n\n\n',moocList
    
    f2=open(inFolder+'/'+moocList)
     
    
        
        
    Description='Unknown'  
    MoreInformation='Unknown' 
    Initiative='Unknown'
    University='Unknown'
    Instructors=''
    Categories=''
    Date='Unknown'
    Length='Unknown'
    EstimatedEffort='Unkown'  
    RecommendedBackground='UnKnown'
    Certificate='unkown'
    exam='Unknown'
    country='Unknown'
    language='Unknown'
    tags=''
    
    ignoreThisMooclist=False
  
    
    for line in f:
        line=line.strip()
        
        
#More Information
        if line.find('<div class="row-fluid gotoCurso">')!=-1:
            try:
                line=next(f)
                MoreInformation=line[line.find('="')+2:line.find('" class')]
                
            except:
                exc_type, exc_obj,exc_tb = sys.exc_info()
                print 'ERROR: ' + str(exc_obj), '\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break
                
            print MoreInformation       
                                
        
        
#Description     
        elif line.startswith('<meta name="description"'):
            try:
                Description=line[line.rfind('="')+2:line.rfind('"/')]                
            except:
                exc_type, exc_obj,exc_tb = sys.exc_info()
                print 'ERROR: ' + str(exc_obj), '\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break
            print Description    
            
            
#Initiative       
        elif line.startswith('<a herf="#" data-original-title="Initiative / Provider"'):
            try:
                Initiative=line[line.rfind('">') + 2:line.rfind('</a>')]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break     
            print Initiative  
            

#University   
        elif line.startswith('<a herf="#" data-original-title="University / Entity"'):
            try:
                University=line[line.rfind('">') + 2:line.rfind('</a>')]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break
            print University         


#Instructors       
        elif line.startswith('<a herf="#" data-original-title="Instructors"'):
            try:
                segment = line.split('<a href="/instructor/')
                for i in range(1,len(segment)):
                     Instructor=segment[i][segment[i].find('">') + 2:segment[i].rfind('</a>')]
                     #Instructors=Instructors + Instructor + '///'
                     if (Instructors==''):
                         Instructors=Instructor
                     else:
                         Instructors=Instructors+','+Instructor    
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break  
            print Instructors 
            
                    

#Categories                       
        elif line.startswith('<a herf="#" data-original-title="Categories"'):
            try:
                line = line.replace('&amp','')
                segment = line.split('<a href="/categories/')
                for i in range(1,len(segment)):
                    cat=segment[i][segment[i].find('">')+2:segment[i].rfind('</a>')]
                    #Categories=Categories+cat+'///'
                    if(Categories==''):
                        Categories=cat
                    else:
                        Categories=Categories+','+cat   
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break    
            print Categories      
            
#Start Date            
        elif line.startswith('<a herf="#" data-original-title="Start Date"'):
           try:
               Date=line[line.rfind('">')+2:line.rfind('</div>')-12]
           except:
               exc_type, exc_obj, exc_tb = sys.exc_info()
               print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
               ignoreThisMocc=True
               break  
           print Date      

#Length           
        elif line.startswith('<a herf="#" data-original-title="Course Length"'):
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
            print EstimatedEffort
                           
                  

#Certificate        
        elif line.find('href="/certificate/')!=-1:
            try:
                Certificate=line[line. rfind('">')+2:line.rfind('</a>')] 
            except:
                 exc_type,exc_obj,exc_tb=sys.exc_info()
                 print 'ERROR:'+str(exc_obj),'\nError happened in line:' + str(exc_tb.tb_lineno)
                 ignoreThisMooclist=True
                 break 
            print  Certificate


#Exam       
        elif line.find('<a href="/exam/')!=-1:
            try:
                exam=line[line.rfind('">')+2:line.rfind('</a')]               
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break        
            print exam   
            
   
                       
                 
    


# Country  
        elif line.find('<a href="/countrys/') !=-1:
            try:
                country=line[line.rfind('">')+2:line.rfind('</a')]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break    
            print country     
    
#Language
        elif line.find('<a href="/language/') !=-1:
            try:
                language=line[line.rfind('">')+2:line.rfind('</a')]
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break    
            print language
            
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
                       tags=tags+','+subtag   
 
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print 'ERROR: '+str(exc_obj),'\nError happened in Line : ' + str(exc_tb.tb_lineno)
                ignoreThisMocc=True
                break 
            print tags
            
              
#RecommendedBackground      

        elif line.find('<a herf="#" data-original-title="Recommended Background"')!=-1:
            try:
                
                 RecommendedBackground=line[line.rfind('">')+2:line.rfind('</div></div></div>')]
                           
            except:
                 exc_type,exc_obj,exc_tb=sys.exc_info()
                 print 'ERROR:'+str(exc_obj),'\nError happened in line:' + str(exc_tb.tb_lineno)
                 ignoreThisMooclist=True
                 break 
            print  RecommendedBackground      
    
    fileReader=f2.read()      
    if fileReader.rfind('<a herf="#" data-original-title="Recommended Background"')==-1:
        RecommendedBackground='Unknown'
        print RecommendedBackground
        
                                
    if ignoreThisMooclist==False:
        fw.write(moocList+'\n'+Description+'\n'+MoreInformation+'\n'+Date+'\n'+Initiative +'\n'+ University+'\n'+Instructors+'\n'+Categories+'\n'+country+'\n'+Length+'\n'+EstimatedEffort+'\n'+RecommendedBackground+'\n'+exam+'\n'+Certificate+'\n'+language+'\n'+tags+'\n\n')
    f.close()
    f2.close()

fw.close()

    


