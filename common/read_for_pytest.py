import os

import xlrd

class ReadData1():
    def ReadExecl(self,filename):
        path=os.path.abspath('.')+'/'+'data'+'/'+filename+'.xlsx'
        work=xlrd.open_workbook(path)
        sheet=work.sheet_by_name('Sheet1')
        nrows=sheet.nrows
        dataList=[]
        for rows in range(1,nrows):
            datas=sheet.row_values(rows)
            dataList.append(datas)
        return dataList

# print(ReadData().ReadExecl('dara'))


