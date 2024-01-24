import pymysql
import openpyxl


#创建工作簿对象
workbook = openpyxl.Workbook()
#获得默认的工作表
sheet = workbook.active
#修改工作表标题
sheet.title = '员工基本信息'
#给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
#创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        sql = 'select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` from `tb_emp` natural join `tb_dept`'
        cursor.execute(sql)
        results = iter(cursor)
        for row in results:
            sheet.append(row)
    workbook.save('hrs.xlsx')
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    conn.close()
