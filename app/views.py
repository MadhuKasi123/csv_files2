from django.shortcuts import render
from app.models import *
import csv
from django.http import HttpResponse
# Create your views here.


def Create_Business(self):
    with open('C:\\Users\\madhu\\OneDrive\\Desktop\\Django projects\\madhu\\Scripts\\project41\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            sr=i[0]
            p=i[1]
            dv=i[2]
            su=i[3]
            st=i[4]
            u=i[5]
            mg=i[6]
            sub=i[7]
            gr=i[8]
            s1=i[9]
            s2=i[10]
            s3=i[11]
            s4=i[12]
            s5=i[13]
            BO=Business_Data_Collection(Series_reference=sr,Period=p,data_value=dv,suppresed=su,status=st,units=u,magnitude=mg,subject=sub,group=gr,series_title_1=s1,series_title_2=s2,series_title_3=s3,series_title_4=s4,series_title_5=s5)
            BO.save()
        return HttpResponse('data inserted into Business_Data_Collection')
