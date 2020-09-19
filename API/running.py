# _*_ coding:utf-8 _*_
import os,sys
sys.path.append(os.path.dirname(__file__))
from API.config import setting
import unittest,time
from API.lib.newreport import new_report
from API.package.HTMLTestRunnerone import HTMLTestRunner
from API.lib.sendmail import send_mail


def add_case(test_path = setting.Test_Case):
    """
         加载所有的测试用例
         :param test_path:加载用例的路径
         :return: 返回测试套件
    """
    # 批量调用setting.Test_Case路径下的文件，返回一个测试套件
    discover = unittest.defaultTestLoader.discover(test_path,pattern='test*.py')
    return discover



def run_case(all_case,result_path=setting.Test_Report):
    """
         执行所有的测试用例
         :param all_case:测试套件
         :param result_path：生成报告保存路径
         :return: 无
    """
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path+'/'+now+'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='大数据接口自动化测试报告',description=u"大数据接口用例测试情况",
                            tester='归乐'
                            )
    runner.run(all_case)
    fp.close()
    # 发送邮件
    send_mail()

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)