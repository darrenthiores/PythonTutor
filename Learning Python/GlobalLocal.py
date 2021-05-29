#variable global & local
"""
variable global dapat digunakan didalam variable local
namun variable local tidak dapat dipakai di global
"""

#variable global
name = 'darren'
age = 17
pintar = False

#variable local (yang berada didalam function)

def data() :
    name = 'maria'
    pintar = True
    print (name, ',', age, ', kepintaran : ', pintar)

data()

#pemanggilan variable global (untuk membandingkan)

print (name, ',', age, ', kepintaran : ', pintar)