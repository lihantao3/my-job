import pymysql


no = int(input('部门编号：'))
name = input('部门名称：')
location = input('部门所在地：')

print(type(no))


#1. 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user',
                       password='qwer1234!', database='hrs', charset='utf8mb4')
try:
    #  2. 获取游标对象
    with conn.cursor() as cursor:
        # 3. 通过游标向数据库发出mysql语句
        affected_rows = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)', (no, name, location)
        )
        print(affected_rows)
        if affected_rows == 1:
            print('新增部门成功！')
    # 4. 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
