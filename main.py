import PySimpleGUI


import PySimpleGUI as sg
import mariadb
import sys








def jotain():
    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()
#jotain()



def tietokanta():
    try:
        conn = mariadb.connect(
            user="root",
            password="P4ssw0rd",
            host="localhost",
            port=3306,
            database="testi"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
tietokanta()
