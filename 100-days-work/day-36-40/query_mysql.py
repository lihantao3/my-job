import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!',database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        sql = 'select * from `tb_dept`'
        affected_rows = cursor.execute(sql)
        print(f'查询到{affected_rows}行数据。')
        results = iter(cursor)
        for _ in results:
            print(_)
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    conn.close()
