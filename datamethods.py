import sqlite3

def dbmkr():

    ''''
        it is a function that creates database if database is not exist then
        arguements:
            no arguement
        return:
            no return
    '''
    # Connect to the database (create if not exists)
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # Create Users Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT NOT NULL
        )
    ''')

    # Create Appointments Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Appointments (
            bookedby_id TEXT,
            date DATE NOT NULL,
            time TIME NOT NULL,
            doctor TEXT,
            phone_number INTEGER NOT NULL,
            FOREIGN KEY (phone_number) REFERENCES Patients(phone_number),
            FOREIGN KEY (bookedby_id) REFERENCES Users(user_id)
        )
''')

    # Create Patients Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            name TEXT NOT NULL,
            address TEXT,
            gender TEXT,
            phone_number INTEGER PRIMARY KEY
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()
    initialize()

def login(u,p):
    ''''
        it is a function that checks for credentials 
        arguments:
            u= Username
            p=Password 
        returns:
            usertype (admin or reception) :if the credential is true 
            False : if the credentials is not good
    ''' 
    dbmkr()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(f"SELECT password,user_type FROM Users WHERE user_id='{u}'")
    db_p=c.fetchone()
    conn.close()
    if db_p!=None:
        if p==db_p[0]: 
            return db_p[1]
        else:
            return False
    else:
        return False

def admchgpass(o,p):
    '''
        it changes password of admin 
        arguments:
            o:old password of admin
            p:new password of admin
        return:
            True: if old password is correct and password is changed
            False: if old password is not correct and password is not changed
    '''
    dbmkr()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    if login("admin",o)=="admin":
        c.execute(f"UPDATE Users SET password='{p}' WHERE user_id='admin'")
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def add_patient(Name,Address,Gender,Number):
    link=sqlite3.connect("database.db")
    c=link.cursor()
    c.execute(f"SELECT phone_number FROM Patients WHERE phone_number={Number}")
    dat=c.fetchone()
    if dat==None:
        c.execute(f"INSERT INTO Patients VALUES('{Name}','{Address}','{Gender}',{Number})")
        link.commit()
        link.close()
        return True
    else:
        link.close()
        return False        
    
def add_receptionist(uid,pss):
    ''''
        this function adds receptionist account in the data base
        arguments:
            uid:username
            pss:Password 
        return:
            case 1: when the data is not present
                type:tuple
                idd=userid created by the admin for receptionist
                True 
            case 2: when data is present
                False
    '''
    import random
    from tkinter import messagebox
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    idd=str(uid).replace(" ","_")+str(random.randint(100,200))
    c.execute(f"SELECT user_id FROM Users WHERE user_id='{idd}'")
    db_p=c.fetchone()
    if db_p==None:
        c.execute("INSERT INTO Users VALUES(?,?,?,?)",(f"{idd}",f"{uid}",f"{pss}","recpt"))
        conn.commit()
        conn.close()
        return (idd,True)
    else:
        conn.close()
        return False
    
def appointment_details(pnumber):
    return "Name of patient : Name \nPatient has appointment on \nDate: DATE\nTime= time \nDoctor: doctor name \nSpecialization= branch"

    
    
def initialize():
    '''
        makes admin account at first boot
        args: None
        Return : None
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(f"SELECT user_id FROM Users WHERE user_id='admin'")
    db_p=c.fetchone()
    if db_p==None:
        c.execute("INSERT INTO Users VALUES(?,?,?,?)",("admin","admin","admin","admin"))
        conn.commit()
    conn.close()
    

if __name__=="__main__":
    print (login("admin","admin"))