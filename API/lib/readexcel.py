# _*_ coding:utf-8 _*_
import xlrd

class ReadExcel():
    # -------------读取excel文件数据--------------
    def __init__(self,fileName,SheetName):
        """
        初始化数据
        :param fileName:xls的文件名
        :param SheetName：表名
        :return: 无
        """
        # 打开excel读取文件，文件名有中文需要加r
        self.data = xlrd.open_workbook(fileName)
        # 通过表名称获取表数据
        self.table = self.data.sheet_by_name(SheetName)
        # ------------获取总行数、总列数--------------
        self.rowsnum = self.table.nrows# 获取表的有效行数
        self.colsnum = self.table.ncols# 获取表的有效列数

    def read_data(self,SheetName):
        """
        从表格读取数据
        :param SheetName：表名
        :return: 返回表格读取的数据，数据以列表形式显示，空返回None
        """
        if self.rowsnum> 1:
            # 获取第一行的内容，列表格式，返回由该行中所有单元格的数据类型组成的列表
            keys = self.table.row_values(0)
            listApiData =[]
            # 获取每一行的内容，列表格式
            for col in range(1,self.rowsnum):
                values = self.table.row_values(col)
                # keys,values组合转换为字典，将keys和values打包为元组对象，并转化为dict
                api_dict = dict(zip(keys,values))
                # 字典中加入xls的表名键值对，用于后续循环遍历各个表使用
                api_dict['SheetName']=SheetName
                # 将字典格式的键值对加入到列表中
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格为空！")
            return None