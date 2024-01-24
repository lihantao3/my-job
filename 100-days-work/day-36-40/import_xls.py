import pymysql
from openpyxl import load_workbook


workbook = load_workbook('data.xlsx')
sheet = workbook.worksheets[0]

conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        for i, row in enumerate(sheet.values):
            if i == 0:
                continue
            sql = 'insert into `tb_emp` (`eno`, `ename`, `job`, `sal`, `comm`, `dno`) values (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, row)
    print('添加数据成功!')
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()
