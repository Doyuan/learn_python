import pymysql

no = int(input("部门编号:"))
name = input("部门名称:")
location = input("部门所在地:")

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="python", charset="utf8mb4")

try:
    # 获取游标对象
    with conn.cursor() as cursor:
        # 通过游标对象向数据库服务器发出sql语句
        affected_row = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
        )

        if affected_row == 1:
            print("新增部门成功")

    # 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()
