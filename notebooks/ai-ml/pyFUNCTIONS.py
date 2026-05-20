import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import netCDF4 as nc
import pytz
import time
import datetime
import calendar

###########FUNCTION TO CONVERT ARM TIME TO CAL TIME##########
def JDtocal(obstime, nn):

#######CONVERT TIME TO HR MIN SEC
 yy=[]
 mo=[]
 dd=[]
 hh=[]
 mm=[]
 ss=[]
 rday=[]
 rdoy=[]

 for jj in range(0,nn):
   foo=obstime[jj]
   foo1=datetime.datetime.fromtimestamp(foo, tz=pytz.utc)
# print(foo1.hour)
   yy.append(foo1.year)
   mo.append(foo1.month)
   dd.append(foo1.day)
   hh.append(foo1.hour)
   mm.append(foo1.minute)
   ss.append(foo1.second)
   tdelta=datetime.timedelta(hours=foo1.hour, minutes=foo1.minute, seconds=foo1.second)
  
   foorday=foo1.day+tdelta.total_seconds()/(24. * 60. * 60.)
   imonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   if foo1.year % 4 == 0:
    imonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   imo=int(foo1.month)
   foordoy = foorday+np.sum(imonth[0:imo])
  
#  rday.append(foo1.day+tdelta.total_seconds()/(24. * 60. * 60.))  ###CONVERT TO FRAC DAY
   rday.append(foorday)
   rdoy.append(foordoy)
###########END FOR ON ALL ELEMENTS

#############THE FUNCTION RETURNS an array NVARIABLE=year...sec X NTIME
 yy=np.array(yy)
 mo=np.array(mo)
 dd=np.array(dd)
 hh=np.array(hh)
 mm=np.array(mm)
 ss=np.array(ss)
 return [yy,mo,dd,hh,mm,ss,rday,rdoy]
###########END FUNCTION############

###############################################################################################
###################################################
###########FUNCTION TO READ model##
def readmodel(filename):

 month=np.array([])
 tb23=np.array([])
 tb31=np.array([])
 pwv=np.array([])
 lwp=np.array([])
 with open(filename, 'r') as file:
  for line in file:
   row = np.array([float(x) for x in line.split()])
#   print(row)
   month=np.append(month,row[13])
   tb23=np.append(tb23,row[20])
   tb31=np.append(tb31,row[25])
   pwv=np.append(pwv,row[14])  ##cm
   lwp=np.append(lwp,row[15])  ##mm

 print('FOUND SIMULATIONS ', len(tb23))
 return(month,tb23,tb31,pwv,lwp)


