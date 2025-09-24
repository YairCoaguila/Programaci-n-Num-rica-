import re

def arreglar(expr: str) -> str:

    expr = re.sub(r'(\d)(x)', r'\1*\2', expr)

    expr = re.sub(r'(x)(\d)', r'\1*\2', expr)

    expr = expr.replace("^", "**")
    return expr

fun1 = input("Ingrese f(x): ")   
fun2 = input("Ingrese g(x): ")   

expr1 = arreglar(fun1)
expr2 = arreglar(fun2)

xmin, xmax = -10, 10
ymin, ymax = -10, 10

print("\nGráfico")
print(f"f(x) = {fun1}   →   '*'")
print(f"g(x) = {fun2}   →   '#'\n")

for y in range(ymax, ymin - 1, -1):
    fila = ""
    for x in range(xmin, xmax + 1):
        try:
            y1 = eval(expr1, {"x": x})
        except:
            y1 = None
        try:
            y2 = eval(expr2, {"x": x})
        except:
            y2 = None

        if y1 == y:
            fila += "*"
        elif y2 == y:
            fila += "#"
        elif x == 0 and y == 0:
            fila += "+"
        elif x == 0:
            fila += "|"
        elif y == 0:
            fila += "-"
        else:
            fila += " "
    print(fila)
