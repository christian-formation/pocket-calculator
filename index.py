# import cgi 

# form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

# print(eval(form.getvalue("calcul")))
from script import calcul

html = """<!DOCTYPE html>
<head>
    <title>Mini calculatrice</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="calcul" placeholder="0" />
        <input type="submit" name="send" value="Calculer">
    </form> 
</body>
</html>
"""

print(html)