import math

text = input('Sisend: ').strip()

print(len(text))

if len(text) >= 7 and len(text) % 2 == 1:
    print('Vastab tingimustele')
    print(math.floor(len(text) /2))
else:
    print('Sisend ei vasta tingiumstele')
