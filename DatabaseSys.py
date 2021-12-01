import mysql.connector

class db_operation:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            database='databasesystem',
            user='root',
            password='')

        print("connection sucssesfull\n")
        query = "create table if not exists Student(Id int(4),Name varchar(30),Mobile_No varchar(10))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created Sucssesfully\n")


    def count(self):
        clm = input("Enter colum name: ")
        query = f"select COUNT({clm}) as COUNT from Student"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        print()

    def sum(self):
        clm = input("Enter colum name: ")
        query = f"select SUM({clm}) as SUM from Student"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        print()

    def avg(self):
        clm = input("Enter colum name: ")
        query = f"select AVG({clm}) as AVG from Student"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        print()

    def min(self):
        clm = input("Enter colum name: ")
        query = f"select MIN({clm}) as MIN from Student"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        print()

    def max(self):
        clm = input("Enter colum name: ")
        query = f"select MAX({clm}) as MAX from Student"
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        print(result)
        print()

