import PySimpleGUI


import PySimpleGUI as sg
import mariadb
import sys



"""

#<

koita saada tehtyä nyt aluksi edes:
-tietojen tallentaminen tietokantaan
    -se tietokanta itsessään
-tietojen hakeminen tietokannasta listaan
-tallennettujen tietojen muokkaus


kaikissa ikkunoissa:
-ruksi josta menee kiinni (on kai oletuksena joka tapauksessa)
-ruksista ikkuna menee yllättäen kiinni.  Laittaa sen vain kiinni ilman että tallentaa mitään muutoksia
    -> ideana että kaikki muutokset mitä haluaa tehdä tallentuu heti kun ne on tehnyt ja ne voi poistaa
        samasta ikkunasta jos haluaa

pääikkuna
napit{
    lisää uusi
    muokkaa vanhaa (valitse listasta)
    avaa generointi ikkuna
    perustietoikkuna
    poista vanha (joko kysyy varmistuksen tai voisi laittaa lisänapin lukolle, joka pitää ottaas pois jos haluaa poistaa)
}
näytöt{
    tallennetut tekstinpätkät
        otsikko | tagit | preview
}

tekstinmuokkausikkuna
napit{
    lisää uusi tagi
    hyväksy
    tyhjennä
}
kentät{
    otsikko
    valitut tagit
    kommentti
    Teksti(iso kenttä)
}


tekstingenerointi ikkuna
näytöt{

    tekstikenttä
}

perustiedot ikkuna
-[asia] = {nimi : tieto}

tagilista ikkuna
napit{
    tallenna uusi tagi
    tyhjennä kenttä
    tallenna tagit
}
näytöt{
    listaa aiemmin tallennetut

        [x] loota sille että voi valita aiemmin tallennetun
}
kentät{
tagin nimi, kentässä myös nappi tallentamiselle tai tyhjennykselle


}



>#
"""



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

