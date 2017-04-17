#task7
usadate = "04.17.2017"
day = (usadate [3:5])
month = (usadate [0:2])
year = (usadate [6:])
eurodate = (day+ month + year)
print (eurodate)

#task8
a = "789456789"
b = "dsgsdgwe"
c = (a [0:4] + b + a[5:])
print (c)

#task9
a = "niffler is awesome"
b = (a[8:10].upper())
print (a[0:7] + " " + b + " " + a[11:] )
