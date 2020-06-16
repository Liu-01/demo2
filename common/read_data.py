import csv
import xlrd
import os
import json
import yaml


class ReadData():

    def ReadExecl(self,filename):
        path=os.path.abspath('..')+'/data/'+filename
        work=xlrd.open_workbook(path)
        sheet=work.sheet_by_name('Sheet1')
        nrows=sheet.nrows
        data=[]
        for rows in range(1,nrows):
            row=sheet.row_values(rows)
            data.append(row)
        return data
    def ReadJson(self,filename):
        path=os.path.abspath('..')+'/data/'+filename
        with open(path,'r',encoding='utf-8')as f:
            a=json.load(f)
            return a

    def ReadCsv(self,filename):
        path=os.path.abspath('..')+'/data/'+filename
        new=[]
        with open(path,'r',encoding='utf-8')as f:
            a=csv.reader(f)
            for i in a:
                new.append(i)
        return new

    def ReadYaml(self,filename):
        path=os.path.abspath('..')+'/data/'+filename
        with open(path,'r',encoding='utf-8')as f:
            a=yaml.safe_load(f)
            return a


