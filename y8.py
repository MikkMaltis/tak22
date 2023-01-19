year = int(input('a: '))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} on liigaasta" .format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} on liigaasta" .format(year))

else:
    print("{0} ei ole liigaasta" .format(year))
  

