
import pymysql
import os

from common.myConf import MyConf
from common.my_path import conf_dir


class MyMysql:

    def __init__(self):
        # 实例化配置类对象
        conf = MyConf(os.path.join(conf_dir, "mysql.ini"))
        # 连接数据库/生成游标
        self.db = pymysql.connect(
            host=conf.get("mysql", "host"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "passwd"),
            port=conf.getint("mysql", "port"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

        # 2、创建游标
        self.cur = self.db.cursor()

#执行后得到的条数
    def get_count(self,sql):
        count = self.cur.execute(sql)
        return count


    def get_one_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

#获取所有的数据--用得少
    def get_many_data(self,sql, size=None):
        self.cur.execute(sql)
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    # def update_data(self):
    #     事务
    #     提交commit  回滚 rollback
    #     pass

    def close_conn(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    conn = MyMysql()
    sql = "select id from member where mobile_phone='13350000000'"
    count = conn.get_count(sql)
    print(count)
    conn.close_conn()

