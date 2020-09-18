# _*_ coding:utf-8 _*_
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt
from API.config import setting
from API.lib.readexcel import ReadExcel
from API.lib.sendrequests import SendRequests
from API.lib.writeexcel import WriteExcel

sheetnames = ["Sheet1"]
allData=[]
for i in range(len(sheetnames)):
    allData += ReadExcel(setting.Source_File,sheetnames[i]).read_data(sheetnames[i])
print(allData)
@ddt.ddt

class Demo_API(unittest.TestCase):
    """大数据接口"""
    def setUp(self):
        print("测试开始")

    @ddt.data(*allData)
    def test_demoapi(self,data):

         # 调用发送请求，获取响应判断，写入测试结果到表格
         # :param data:获取表格中所有接口的数据信息，每个接口数据执行一次
         # :return: 无
         # 获取ID字段数值，截取结尾数字并去掉开头0
         rowNum = int(data['ID'].split("_")[2])
         print("用例编号：",rowNum)
         print("请求数据：",data)
         sheetname =data['SheetName']
         # 发送请求， 获取excel表格数据的状态码和消息
         result = SendRequests().sendRequests(data)
         print("响应数据：",result)

         if result =='None':
             self.msg =""
         else:
             self.msg = result.get('msg')

         self.status = result.get('status_code')
         # 获取响应数据的状态码和消息
         readData_code = int(data["status_code"])
         readData_msg = data["msg"]
         OK_data = "PASS"
         NOT_data = "FAIL"
         # 判断如果响应信息msg为空，则以状态码code为判断依据，如果msg不为空，则以状态码code和msg判断是否通过
         if readData_msg =='':
            if readData_code == self.status:
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,OK_data)
            if readData_code != self.status:
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,NOT_data)
            self.assertEqual(self.status, readData_code, "返回实际结果是->:%s" % self.status)
         else:
            if readData_code == self.status and readData_msg == self.msg:
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,OK_data)
            if readData_code != self.status or readData_msg !=self.msg:
               WriteExcel(setting.Target_File,sheetname).write_data(rowNum + 1,NOT_data)
            self.assertEqual(self.status, readData_code, "返回实际结果是->:%s" % self.status)
            self.assertEqual(self.msg, readData_msg, "返回实际结果是->:%s" %self.msg)

    def tearDown(self):
         print("测试结束")


if __name__ == "__main__":
    unittest.main()