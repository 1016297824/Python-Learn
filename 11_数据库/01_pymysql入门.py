# Python操作MySQL数据库
from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='138992',
    autocommit=True  # 设置自动提交
)

# 获取数据库信息
print(conn.get_server_info())

# 创建游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('test')
# 使用游标对象，执行SQL语句，创建数据库表
create_table_query = ("create table if not exists pymysql("
                      "id int auto_increment primary key,"
                      "name varchar(10) not null,"
                      "age int not null);")
cursor.execute(create_table_query)
# 查询并打印结果
cursor.execute('select * from student')
result: tuple = cursor.fetchall()
print(result)
for r in result:
    print(r)

# 更新数据库表
# add_data_query = ("insert into pymysql "
#                   "values(1,'霸气可爱小蜜蜂',18),(2,'霸气可爱小州官',19)")
# cursor.execute(add_data_query)
# add_data_query = ("insert into pymysql "
#                   "values(3,'霸气可爱小蜜蜂',18),(4,'霸气可爱小州官',19),(5,'霸气可爱小州官',19)")
# cursor.execute(add_data_query)
# add_data_query = ("insert into pymysql "
#                   "values(5,'霸气可爱小蜜蜂',18)")
# cursor.execute(add_data_query)
#conn.commit()

# 关闭数据库连接
conn.close()
