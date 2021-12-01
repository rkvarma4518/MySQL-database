from DatabaseSys import db_operation

def main():
    db = db_operation()
    while True:
        print("Enter 1 to Count()")
        print("Enter 2 to Sum()")
        print("Enter 3 to Avg()")
        print("Enter 4 to Min()")
        print("Enter 5 to Max()")
        print("Enter 6 to Exit\n")

        try:
            select = int(input("Enter choice: "))
            if select==1:
                db.count()
            elif select==2:
                db.sum()
            elif select==3:
                db.avg()
            elif select==4:
                db.min()
            elif select==5:
                db.max()
            elif select==6:
                break
            else:
                print("Invalid Input! Try again...\n\n")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()