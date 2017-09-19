# create_db.py
# 只运行一次！！！

import sqlite3

# 连接
conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# 创建表
c.execute('''DROP TABLE IF EXISTS weather''')
c.execute('''CREATE TABLE weather (month TEXT, evaporation TEXT, precipitation TEXT)''')

# 数据
# 格式：月份,蒸发量,降水量
purchases = [('1月', 2, 2.6),
             ('2月', 4.9, 5.9),
             ('3月', 7, 9),
             ('4月', 23.2, 26.4),
             ('5月', 25.6, 28.7),
             ('6月', 76.7, 70.7),
             ('7月', 135.6, 175.6),
             ('8月', 162.2, 182.2),
             ('9月', 32.6, 48.7),
             ('10月', 20, 18.8),
             ('11月', 6.4, 6),
             ('12月', 3.3, 2.3)
             ]

# 插入数据
c.executemany('INSERT INTO weather VALUES (?,?,?)', purchases)

# 提交！！！
conn.commit()

# 查询方式一
for row in c.execute('SELECT * FROM weather'):
    print(row)

# 查询方式二
c.execute('SELECT * FROM weather')
print(c.fetchall())

# 查询方式二_2
res = c.execute('SELECT * FROM weather')
print(res.fetchall())

# 关闭
conn.close()