import random
from werkzeug.security import generate_password_hash

#los caracteres que se van a usar para generar la contraseña
minus="abcdefghijklmnopqrstuvwxyz"
mayus =minus.upper()
numeros="0123456789"
simbolos="!#$%&/()=?¿¡*+@"

#la estructura de la contraseña, se pueden modificar el orden los caracteres y la longitud
base=minus+mayus+numeros+simbolos
longitud=12

#generamos 10 contraseñas (range) aleatorias y las mostramos junto con su versión oculta
for i in range(10):

#en esta parte hace que se muestre en formato "contraseña → contraseña oculta"
 muestra=random.sample(base,longitud)
 password="".join(muestra)
 password_oculto=generate_password_hash(password)
 print("{} → {}".format(password, password_oculto))