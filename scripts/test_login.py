import pytest


class TestLogin:
    def test_success(self):
        """this test succeeds"""
        assert True

    def test_failure(self):
        """this test fails"""
        assert False

    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')

    def test_broken(self):
        raise Exception('oops')

#
# if __name__ == '__main__':
#     pytest.main(['-s', '-v', 'test_login', '--html=jenkins/report/num1.html','--alluredir','jenkins/report/result'])
# #     # pytest.main(['-sv','--alluredir=report'])
