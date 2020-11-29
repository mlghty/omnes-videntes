import mysql.connector as mc

 #processList = processes
        #quantity = len(processList)

        #for x in range(0, quantity):
            #dataChunk = processList[x]

            #push_data(username, password, dataChunk)

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