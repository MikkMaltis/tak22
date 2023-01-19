username = input('Mis su nimi on? : ')
print("Tere " + username)

living_place = (input('Kus sa elad? '))

if living_place == ('Saaremaa'):
    print("Very good")

age = int(input('Sisesta oma vanus: '))

if age < 18:
    print("Oled liiga noor, et autot juhtida, rip bozo.")
elif age > 18:
    print("Võid autot juhtida.")
elif age == 18:
    print("Palju õnne 18 saamise puhul.")