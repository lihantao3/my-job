import pymysql


no = int(input('部门编号：'))

# 1. 建立连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        affected_rows = cursor.execute(
            'delete from `tb_dept` where dno=%s' % no
        )
        if affected_rows == 1:
            print('删除部门成功！')
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()
