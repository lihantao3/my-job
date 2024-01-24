import pymysql


dno = int(input('部门编号：'))
dname = input('部门名称：')
dloc = input('部门所在地：')

conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        print(f'dname:{dname}, dloc:{dloc}, dno:{dno}')
        sql = 'update `tb_dept` set `dname`=%s, `dloc`=%s where `dno`=%s'
        print(sql)
        affected_rows = cursor.execute(sql, (dname, dloc, dno))
        if affected_rows == 1:
            print('更新部门信息成功！')
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()
