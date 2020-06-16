import pytest







class Test000():

    def setup(self):
        print('start')
    def teardown(self):
        print('finish')

    def test01(self):
        a=1
        b=2
        c=3
        print('1111')
        assert c==a+b
    def test02(self):
        a=1
        b=2
        c=b-a
        print('2222')
        assert c>a



