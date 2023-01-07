import sqlite3
import random

class User():
    def __init__(self, nama = "", password= "", balance = 0, unik_id=None):
        self.nama = nama
        self.unik_id = unik_id
        self.password = password
        self.balance = balance
        self.con = sqlite3.connect("Koperasi.db")
        self.c = self.con.cursor()

    def register(self):
        """
        This method for register user in this app
        """
        self.c.execute("""
            create table if not exists koperasi(
                nama text,
                password text,
                unik_id text,
                balance integer
            )
        """)
        self.unik_id = str(self.nama[0:4])+str((random.randint(1,100)))
        self.c.execute("insert into koperasi values(?,?,?,?)",(self.nama, self.password, self.unik_id, self.balance))
        self.con.commit()
        self.con.close()
        return self.unik_id

    def login(self, value1, value2):
        """
        This method for login user in this app
        """
        try:
            self.c.execute("select * from koperasi where unik_id =? and password =?",(value1, value2))
            check = self.c.fetchall()
            self.con.commit()
            self.con.close()
            if len(check) != 0:
                return True
            else: 
                return False
        except:
            pass

    def borrow_money(self, value, unik_id):
        """
        This method for borrow money in this app
        value: the amount of money to be borrowed
        unik_id = user unique key to update data in DB
        """
        try:
            self.c.execute("select balance from koperasi where unik_id=?",(unik_id, ))
            balance = self.c.fetchone()[0]
            total_balance = int(balance) + value
            self.c.execute("update koperasi set balance =? where unik_id=?",(total_balance, unik_id))
            self.c.execute("select * from koperasi")
            self.con.commit()
            self.con.close()
        except:
            pass

    def account_info(self, unik_id):
        """
        This method showing account info user
        unik_id = user unique key for filter in DB
        """
        try:
            data_account = {
                "nama":"",
                "unique":"",
                "balance":""
            }
            self.c.execute("select * from koperasi where unik_id = ?",(unik_id, ))
            data = self.c.fetchall()
            data_account["nama"] = data[0][0]
            data_account["unique"] = data[0][2]
            data_account["balance"] = data[0][3]
            self.con.commit()
            self.con.close()
            return data_account
        except:
            pass