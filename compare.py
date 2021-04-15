# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:42:43 2021

@author: admin
"""
a =  int(input('请输入一个整数：'))
if a>100:
    print('{}>100'.format(a))
elif a==100:
    print('{}==100'.format(a))
else:
    print('{}<100'.format(a))        
        
namelist = ['Sophia','Emma','Olivia','Ava','Mia','Isabella','Zoe','Lily','Emily','Madison','Jackson','Aiden','Liam','Lucas','Noah','Mason','Ethan','Caden','Logan','Jacob']
# 点名册
# for循环
for i in namelist :
    print(i)
    
#range()函数
for a in range(1,21) :
    if a==10:
        continue
    print(a)
       
#while循环
zsum=0
a=1
while a<=100:
    zsum = zsum + a
    a+=1
    if zsum > 1000:
        break
    print(zsum)
    
#for ... in ...:   点到为止，设定次数，次数够为止
#while ...:        不达目的不罢休，设定条件，条件满足为止   