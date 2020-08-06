#importiere zufall
import random
user_auswahl = str(input("In order to test your current password press 't'\n\nIn order to generate a password press 'g' "))
if user_auswahl == "g":
    #eingabe des users
    eingabe = int(input("Enter the desired length of you password(8-32 characters)"))

    if eingabe < 8:
        eingabe = int(input("Your password is too short! Please make sure it contains at least of 8 characters"))
    elif eingabe > 32:
        eingabe = int(input("Your password is too long. Make sure it contains not more than 32 characters."))

    #arrays//erweitern mit buchstaben und sonderzeichen
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    buchstaben_klein = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    buchstaben_gross = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    sonderzeichen = ["#", "(", ")", "/", "!", "§", "%", "&", "?", "=", "+", "-", "*", ":", ".", "_", "{", "}", "[", "]", "ü", "ä", "ö", "Ä", "Ü", "Ö"]
    verteilungs_wert_zufall = ["zahlen", "buchstaben_gross", "buchstaben_klein", "sonderzeichen"]
    #verteilung und rest
    verteilungs_wert_eingabe = eingabe//4
    verteilungs_wert_rest = eingabe%4
    #array für das passwort-leer
    password_arr = []

    #anzahl der angegebenen stellen in 'eingabe' wird umgesetzt
    for i in range(verteilungs_wert_eingabe):
        zufall = random.choice(zahlen)
        password_arr.append(zufall)

    for i in range(verteilungs_wert_eingabe):
        zufall = random.choice(buchstaben_gross)
        password_arr.append(zufall)

    for i in range(verteilungs_wert_eingabe):
        zufall = random.choice(buchstaben_klein)
        password_arr.append(zufall)

    for i in range(verteilungs_wert_eingabe):
        zufall = random.choice(sonderzeichen)
        password_arr.append(zufall)

    for val in range(verteilungs_wert_rest):
        zufall_array = random.choice(verteilungs_wert_zufall)
        if zufall_array == "zahlen":
            zufall = random.choice(zahlen)
            password_arr.append(zufall)

        if zufall_array == "buchstaben_gross":
            zufall = random.choice(buchstaben_gross)
            password_arr.append(zufall)

        if zufall_array == "buchstaben_klein":
            zufall = random.choice(buchstaben_klein)
            password_arr.append(zufall)

        if zufall_array == "sonderzeichen":
            zufall = random.choice(sonderzeichen)
            password_arr.append(zufall)

    #durchmischen
    for i in range(len(password_arr)):
        random.shuffle(password_arr)
        final_password_output = password_arr
    #darstellung
    print('')
    print(''.join(str(e) for e in final_password_output))

#fals der user 'test' eingibt, wird geschaut ob das passwort sicher ist
elif user_auswahl == "t":
    #arrays für den Vergleich
    zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    buchstaben_klein = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    buchstaben_gross = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    sonderzeichen = ["#", "(", ")", "/", "!", "§", "%", "&", "?", "=", "+", "-", "*", ":", ".", "_", "{", "}", "[", "]", "ü", "ä", "ö", "Ä", "Ü", "Ö"]
    #eingabe des users
    passwort_test_eingabe = str(input("Please enter your password:"))
    #liste die die fehler sammelt
    fehler_liste = []
    #schaut ob passwort zu lang oder zu kurz ist
    if len(passwort_test_eingabe) < 8:
        fehler_liste.append("Your password is too short. Choose a password wit at least 8 characters!")
    elif len(passwort_test_eingabe) > 32:
        fehler_liste.append("Your password is too long!")
    #print(''.join(str(e) for e in fehler_liste))
    #variablen für die abfrage-kette
    buchstaben_gross_vorhanden = False
    buchstaben_klein_vorhanden = False
    sonderzeichen_vorhanden = False
    zahlen_vorhanden = False
    counter_buchstaben_groß = 0
    counter_buchstaben_klein = 0
    counter_zahlen = 0
    counter_sonderzeichen = 0
    #abfrage-kette
    for i in buchstaben_gross:
        for a in passwort_test_eingabe:
            if i == a:
                counter_buchstaben_groß += 1
    if counter_buchstaben_groß >= 1:
            buchstaben_gross_vorhanden = True
    if counter_buchstaben_groß < 1:
            fehler_liste.append("Your password does not contain any upper case letter!(At least one is recommended)")
    for i in buchstaben_klein:
        for a in passwort_test_eingabe:
            if i == a:
                counter_buchstaben_klein += 1
    if counter_buchstaben_klein >= 1:
        buchstaben_klein_vorhanden = True
    else:
        fehler_liste.append("Your password does not contain any lower case letter!(At least one is recommended)")
    for i in zahlen:
        for a in passwort_test_eingabe:
            if i == a:
                counter_zahlen += 1
    if counter_zahlen >= 1:
        zahlen_vorhanden = True   
    else:
        fehler_liste.append("Your password does not contain any number!(At least one is recommended)")
    for i in sonderzeichen:
        for a in passwort_test_eingabe:
            if i == a:
                counter_sonderzeichen += 1
    if counter_sonderzeichen >= 1:
        sonderzeichen_vorhanden = True  
    else:
        fehler_liste.append("Your password does not contain any special characters!(At least one is recommended)")


    #passwort-test ergebniss und zusamenstellung der fehler
    if buchstaben_gross_vorhanden == True and buchstaben_klein_vorhanden == True and zahlen_vorhanden == True and sonderzeichen_vorhanden == True:
        print('')
        print('')
        print("Your password is safe! Wuhu:)") 
        #wahrscheinlichkeit, dass das Passwort geknackt wird, wird berechnet
        passwort_chance = 100*(((1/26)**counter_buchstaben_groß)*((1/26)**counter_buchstaben_klein)*((1/10)**counter_zahlen)*((1/26)**counter_sonderzeichen))   
        print("The chance that your password will be cracked is:")
        print(passwort_chance, "%")
    else:
        print('')
        print('')
        print("Your password is insecure!")
        print("Fix following errors:")   
        print(fehler_liste)

    

        


