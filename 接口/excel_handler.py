import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


class ExcelHandler():
    def __init__(self, file):
        self.file = file

    def open_sheet(self, name) -> Worksheet:
        """
            在方法后面加 -> 指向类型，代表这个方法返回的类型是这个
            加了Worksheet 类，下面的sheet就会有提示
        :param name:
        :return:
        """
        wb = openpyxl.load_workbook(self.file)
        sheet_name = wb[name]
        return sheet_name

    # 获取表头数据
    def header(self, sheet_name):
        sheet = self.open_sheet(sheet_name)
        headers = []
        for i in sheet[1]:
            headers.append(i.value)
        return headers

    # 获取所有数据
    def read(self, sheet_name):
        sheet = self.open_sheet(sheet_name)
        rows = list(sheet.rows)[1:]
        data = []
        for row in rows:
            data_row = []
            for cell in row:
                data_row.append(cell.value)

                # 列表转成字典，要和header 去zip

            data.append(data_row)
        return data


if __name__ == '__main__':
    excel = ExcelHandler(r'd:\cases.xlsx')
    data = excel.read('Sheet1')
    print(data)