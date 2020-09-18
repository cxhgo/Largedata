# _*_ coding:utf-8 _*_
import os,sys
# 文件路径根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path是一个列表，包括有所有查找包的目录，直接启动python使用
sys.path.append(BASE_DIR)

# 配置文件
Test_Config = os.path.join(BASE_DIR,"database","config.ini")
# 测试用例模板文件
Source_File = os.path.join(BASE_DIR,"database","APITestCase.xlsx")
# excel测试用例结果文件
Target_File = os.path.join(BASE_DIR,"report","excelReport","APITestCase.xlsx")
# 测试用例报告
Test_Report = os.path.join(BASE_DIR,"report")
# 测试用例程序文件
Test_Case = os.path.join(BASE_DIR,"testcase")
