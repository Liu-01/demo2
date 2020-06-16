import pytest
from common.read_for_pytest import ReadData

class Test001():

    def setup(self):
        print('start')

    @pytest.mark.parametrize("name,password",ReadData().ReadExecl('dara.xlsx'))
    def test01(self,name,password):
        print(name,password)


