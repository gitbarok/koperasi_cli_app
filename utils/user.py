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
        try:
            self.c.execute("select * from koperasi where unik_id =? and password =?",(value1, value2))
            check = self.c.fetchall()
            self.con.commit()
            self.con.close()
            print(check)
            if len(check) != 0:
                return True
            else: 
                return False
        except:
            pass

    def borrow_money(self, value, unik_id):
        try:
            for balance in self.c.execute("select balance from koperasi where unik_id=?",(unik_id, )):
                total_balance = int(balance[0]) + value
                self.c.execute("update koperasi set balance =? where unik_id=?",(total_balance, unik_id))
                self.c.execute("select * from koperasi")
                print(self.c.fetchall())
                self.con.commit()
                self.con.close()
        except:
            pass

    def account_info(self, unik_id):
        try:
            data = []
            for nama, _, unique, balance in self.c.execute("select * from koperasi where unik_id = ?",(unik_id, )):
                data.append(nama)
                data.append(unique)
                data.append(balance)
            return data
        except:
            pass