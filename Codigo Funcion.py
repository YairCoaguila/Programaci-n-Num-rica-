def analizar_funcion(funcion):
    variables = set()
    operaciones = []


    for char in funcion:
        if char.isalpha():  
            variables.add(char)
        elif char in "+-*/^":  
            operaciones.append(char)

    print("Función ingresada:", funcion)
    print("Variables detectadas:", list(variables))
    print("Operaciones detectadas:", operaciones)


analizar_funcion("3*x^2 + 2*x*y - y/4")
