import unittest
from common.HTMLTestRunner1 import HTMLTestRunner



class Test000(unittest.TestCase):

    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('finish')
    def test01(self):
        a=1
        b=2
        c=3
        print('1111')
        self.assertEqual(a+b,c)
    def test02(self):
        a=1
        b=2
        c=b-a
        print('2222')
        self.assertEqual(c,a)
if __name__ == '__main__':
    suit=unittest.TestLoader().loadTestsFromTestCase(Test000)
    with open('../report/report.html','wb')as f:
        HTMLTestRunner(stream=f,title='测试',tester='lg',description='测试发送邮件').run(suit)
