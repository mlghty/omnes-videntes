import mysql.connector as mc
from datetime import date, datetime
import matplotlib.pyplot as plt


 #processList = processes
        #quantity = len(processList)

        #for x in range(0, quantity):
            #dataChunk = processList[x]

            #push_data(username, password, dataChunk)

def push_userdata(username, work):

    db = mc.connect(
    host = "35.223.136.62",
    user = "logged_usr",
    passwd = "Logged_usr",
    database = "3328_database"
    )

    #split up the time
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today_list = today.split('/')
    day = today_list[1]
    month = today_list[0]
    year = today_list[2]

    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    cursor = db.cursor()

    cursor.execute('INSERT INTO proxy_userdata VALUES (%s, NULL, %s, %s, %s, %s, %s)', (username, day, month, year, time, work))
    cursor.callproc('handle_userdata')
    db.commit()

def push_appdata(username, day, month, year, time, appname, runtime):

    db = mc.connect(
    host = "35.223.136.62",
    user = "logged_usr",
    passwd = "Logged_usr",
    database = "3328_database"
    )

    cursor = db.cursor()
    cursor.execute('INSERT INTO proxy_appdata VALUES (%s, NULL, %s, %s, %s, %s, %s, %s)', (username, day, month, year, time, appname, runtime))
    db.commit()
    cursor.callproc('handle_appdata')
    db.commit()

def get_appdata(username):

    db = mc.connect(
    host = "35.223.136.62",
    user = "logged_usr",
    passwd = "Logged_usr",
    database = "3328_database"
    )

    cursor = db.cursor()
    cursor.execute('INSERT INTO get_appdata VALUES (%s, NULL, NULL, NULL, NULL, NULL, NULL, NULL)', (username,))
    db.commit()

    cursor.callproc('handle_get_appdata')
    db.commit()
    cursor.execute('SELECT * FROM good_appdata')
    re_data = cursor.fetchall()

    return re_data

def get_userdata(username):

    db = mc.connect(
    host = "35.223.136.62",
    user = "logged_usr",
    passwd = "Logged_usr",
    database = "3328_database"
    )

    cursor = db.cursor()
    cursor.execute('INSERT INTO get_userdata VALUES (%s, NULL, NULL, NULL, NULL, NULL, NULL)', (username,))
    db.commit()

    cursor.callproc('handle_get_userdata')
    db.commit()
    cursor.execute('SELECT * FROM good_userdata')
    re_data = cursor.fetchall()

    return re_data


def login(username, password):

    db = mc.connect(
    host = "35.223.136.62",
    user = "logged_usr",
    passwd = "Logged_usr",
    database = "3328_database"
    )

    # Check if account exists using MySQL
    cursor = db.cursor()
    
    cursor.execute('INSERT INTO proxy_account VALUES (%s, %s)', (username, password))

    cursor.callproc('authenticate')
    cursor.execute('SELECT logged FROM authenticated WHERE username = %s', (username,))
    account = cursor.fetchone()

    if account:
        
        return 1
    else:
        
        return 0
    
def registration(username, password):

    db = mc.connect(

    host = "35.223.136.62",
    user = "new_usr",
    passwd = "New_!__usrs",
    database = "3328_database"

    )

    cursor = db.cursor()

    cursor.callproc('Clear_Temp')
    cursor.execute('INSERT INTO temp_username VALUES (%s, %s)', (username, 0))
    cursor.callproc('search_accounts')

    cursor.execute('SELECT * FROM temp_username')
    account = cursor.fetchall()
    account = account[0]
    account = account[1]

    if account == 1:
        
        cursor.callproc('Clear_Temp')
        
        return 1
    else:

        cursor.execute('INSERT INTO new_accounts VALUES (NULL, %s, %s)', (username, password))
        cursor.callproc('handle_register')
        db.commit()

        cursor.callproc('Clear_Temp')

        return 0

get_userdata('test')