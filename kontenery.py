# 1
"""stworzono kontener z kolorami"""
colors = ["nebieski", "szary", "czerwony"]
"""guess ma być zmienną do użytku w funkcji if """
guess = input("zgadnij kolor ")
"""stosujemy in, aby sprawdzić zwartość w tablicy """
if guess in colors:
    print("zgadłeś!")
else: 
    print("niestety :C, spórbuj jeszcze raz !")

# 2 Krotki
rhymes = {
    "1": "niebem",
    "2": "kwas kwas",
    "3": "śnić",
    "4": "odjazd",
}

n = input("Wpisz cyfrę: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Nie znaleziono")
# 3 container in container
lists = []
rap = ["Mata",
"żabson"
]
rock = ["Bob Dylan",]

djs = ["Tiesto",]
lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

# 4 Exercise
# 4a
first_list = ["Mata", "asd", " bsc"]
print(first_list)
# 4b
places = ("EOP - in centre", "Warsaw - in centre", )
print(places)

# 4c
lists_about_other = {
    "wzrost": "180c",
    "ulubiony-kolor": "czerwony",
    "autor": "none",
    "przyszłośc?": "nieznana",
}
# 4d
a = input("What do you want to know about me?: ")
if a in lists_about_other:
    lista = lists_about_other[a]
    print(lista)
else:
    print("nie wiem :<")

