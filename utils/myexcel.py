# encoding: utf-8
# @author: w4dll
# @file: myExcel.py
# @time: 2021/4/2 12:51

import xlwt, xlrd
from utils.utils import dy
"""
这个包主要是写一些关于excel操作的函数
"""


# 将数据写入excel
def writeToExcel(queryset, filename, filepath):
    """
    将数据集中的数据写入到excel文件中去，并保存到指定的路径
    :param queryset:
    :param filename:
    :return:
    """

    wb = xlwt.Workbook()
    ws = wb.add_sheet(filename)

    # 写入标题行
    ws.write(0, 0, '序号')
    ws.write(0, 1, '单位')
    ws.write(0, 2, '姓名')
    ws.write(0, 3, '成绩')
    ws.write(0, 4, '有效')
    ws.write(0, 5, '时间')

    # 写入数据
    rowNum = 1
    style = xlwt.XFStyle()
    style.num_format_str = 'YY年MMM月D日h时mm分ss秒'  # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
    for q in queryset:
        ws.write(rowNum, 0, rowNum)
        ws.write(rowNum, 1, q.userid.unit.unit_name)
        ws.write(rowNum, 2, q.userid.nick_name)
        ws.write(rowNum, 3, q.grade)
        ws.write(rowNum, 4, '有效' if q.is_valid else '无效')
        ws.write(rowNum, 5, q.test_time, style)

    wb.save('/tmp_results/' + filename + '.xls')


# 将excel文件转换成题库数据返回
def readExcelToData(filepath):
    data = []
    file = xlrd.open_workbook(filepath)
    table = file.sheet_by_index(0)
    for i in range(1, table.nrows):
        row = []
        for j in range(table.ncols):
            row.append(table.cell(i, j).value)

        title = row[0] + '\n'
        i = 0
        for r in row[4:12]:
            if r:
                title += chr(65+i) + '、' + r + '\n'
                i += 1

        dt = {}
        dt["question_type"] = row[1]
        dt["answer"] = row[12]
        dt["score"] = int(row[3])
        dt["difficulty"] = row[2]
        dt['title'] = title
        data.append(dt)
    return data
