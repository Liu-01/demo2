import unittest
from common.HTMLTestRunner1 import HTMLTestRunner
from ddt import ddt,data,unpack
from common.read_for_unittest import ReadData


@ddt
class Test000(unittest.TestCase):

    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('finish')
    @data(*ReadData().ReadExecl('dara.xlsx'))
    @unpack
    def test01(self,name,password):
        print(name,password)

if __name__ == '__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(Test000)
    with open('../report/report.html','wb')as f:
        HTMLTestRunner(stream=f,title='测试',tester='lg',description='测试发送邮件').run(suit)
