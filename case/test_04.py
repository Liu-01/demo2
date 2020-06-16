import unittest

from ddt import ddt, data, unpack
from jsonpath import jsonpath

from common.read_data import ReadData

@ddt
class Test000(unittest.TestCase):
    # global c
    # a = ReadData().ReadJson('data_json')
    # b=a['result']
    # print(b)
    # new=[]
    # for i in b:
    #     c =i['address']
    #     new.append(c)
    a = ReadData().ReadJson('data_json')
    b=a['result']

    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('finish')
    @data(*b)
    def test01(self,a):
        a=a['zipcode']
        print(a)

if __name__ == '__main__':
    unittest.main(verbosity=2)