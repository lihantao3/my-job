import pymysql


page = int(input('页码：'))
size = int(input('大小：'))
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        sql = 'select * from tb_emp order by `sal` desc limit %s, %s'
        cursor.execute(sql, ((page - 1) * size, size))
        for row in cursor.fetchall():
            print(row)
finally:
    conn.close()
