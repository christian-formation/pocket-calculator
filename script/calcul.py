import cgi 
import functools

form = cgi.FieldStorage()

calculTxt = form.getvalue("calcul")

if calculTxt !=None:
    multiple = calculTxt.split("*")
else:
    multiple = []

somme = 0
soustraction = 0
multiplication = 0
division = 0

for x in multiple:
    if len(x.split("+")) == 1 and len(x.split("-")) == 1 and len(x.split("/")) == 1:
        multiplication = functools.reduce(lambda a, b: a*b, list(map(float, multiple)))
    
    if len(x.split("/")) > 1 and len(x.split("+")) == 1 and len(x.split("-")) == 1:
        division = functools.reduce(lambda a, b: a/b, list(map(float, x.split("/"))))
    
    if len(x.split("/")) == 1 and len(x.split("+")) > 1 and len(x.split("-")) == 1:
        somme = functools.reduce(lambda a, b: a+b, list(map(float, x.split("+"))))
    
    if len(x.split("/")) == 1 and len(x.split("+")) == 1 and len(x.split("-")) > 1:
        soustraction = functools.reduce(lambda a, b: a-b, list(map(float, x.split("-"))))

total = multiplication + division + somme + soustraction 

print(total)