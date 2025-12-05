import sqlite3
import getpass
import hashlib

#Connect to SQLite database:

conn=sqlite3.connect('College_ERP.db')
cursor=conn.cursor()

#Create table if not exists:

cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT PRIMAEY KEY,password TEXT,aadhar_number TEXT,mobile_number TEXT,college_name TEXT)")
conn.commit()

#Check if column exist and add if not:

cursor.execute("PRAGMA table_info(users)")
columns=[row[1] for row in cursor.fetchall()]
needed_columns=['aadhar_number','mobile_number','college_name']

for col in needed_columns:
    if col not in columns:
        cursor.execute(f"ALTER TABLE users ADD COLUMN {col} TEXT")
        conn.commit()

def register_user():
    username=str(input("Enter username: "))
    password=getpass.getpass("Enter password: ")
    hashed_password=hashlib.sha256(password.encode()).hexdigest()#This returns str
    aadhar_number=int(input("Enter your Aadhar Number: "))
    mobile_number=int(input("Enter your Mobile Number: "))
    college_name=str(input("Enter your College Name: "))

    try:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",(username,hashed_password,aadhar_number,mobile_number,
                                                              
                                                              college_name))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:   
            print("Username already exists.Please regiser with different username.")
      
def login_user():
    username=input("Enter username: ")
    password=getpass.getpass("Enter password: ")
    hashed_password=hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT aadhar_number,mobile_number,college_name FROM users WHERE username= ? AND password= ?",(username,hashed_password))
    user_data=cursor.fetchone()
    if user_data:
        print("Login successfully.")
        print(f"aadhar number: {user_data[0]}")
        print(f"mobile number: {user_data[1]}")
        print(f"college name: {user_data[2]}")
    else:
        print("Invalid username or password.Please try again.")
        return

        
    #Dashboard:
    
    while True:
        print("\n1.Examform Dashboard")
        print("2.Admit Card")
        print("3.Logout")
        choice=input("Choose an option: ")
        if(choice=="1"):
            for i in range(1,3,1):
                a=str(input("enter you subject"))
        elif(choice=="2"):
            print("java   -   bcs-524   -   10.12.2025,\npython -   bcs-102   -   12.12.2025")
        elif(choice=="3"):
            break
        else:
            print("Invalid option.")
    else:
        print("Invalid credentials")

#Main loop:

def main():
    while True:
        print("\n1.Register")
        print("2.Login")
        print("3.Exit")
        choice=input("Choose an option: ")
        
        if(choice=="1"):
            register_user()
        elif(choice=="2"):
            login_user()
        elif(choice=="3"):
            break
        else:
            print("Invalid choice.Please try again!")
        
if __name__=='__main__':
    main()
    conn.close()


