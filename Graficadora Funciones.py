import re

def arreglar(expr: str) -> str:
    """Convierte notación matemática a sintaxis Python"""
    expr = expr.replace("^", "**")
    expr = expr.replace("≤", "<=").replace("≥", ">=")
    expr = expr.replace("S/", "").replace("s/", "")  
    return expr

def evaluar_restriccion(expr: str, x: int, y: int) -> bool:
    """Evalúa si el punto (x,y) satisface la restricción"""
    try:
        entorno = {"x": x, "y": y, "__builtins__": {}}
        return eval(expr, entorno)
    except:
        return False

def graficar_restricciones(nombre, restricciones, xmin, xmax, ymin, ymax):
    """Grafica la región factible de las restricciones"""
    print(f"\n{'='*60}")
    print(f"GRÁFICO: {nombre}")
    print(f"{'='*60}")
    
    print("RESTRICCIONES INGRESADAS:")
    for i, restr in enumerate(restricciones, 1):
        print(f"  {i}. {restr}")
    
    print(f"\nRegión factible ({xmin} ≤ x ≤ {xmax}, {ymin} ≤ y ≤ {ymax}):")
    print()
    

    restricciones_arregladas = [arreglar(restr) for restr in restricciones]
    
    for y in range(ymax, ymin - 1, -1):
        fila = f"{y:2d} | "
        for x in range(xmin, xmax + 1):
           
            cumple_todas = True
            for restriccion in restricciones_arregladas:
                if not evaluar_restriccion(restriccion, x, y):
                    cumple_todas = False
                    break
            
            if cumple_todas:
                fila += "·"  
            elif x == 0 and y == 0:
                fila += "+"  
            elif x == 0:
                fila += "|"  
            elif y == 0:
                fila += "-"  
            else:
                fila += " "  
        print(fila)
    
   
    print("    " + "-" * (xmax - xmin + 6))
    eje_x = "     "
    for x in range(xmin, xmax + 1):
        if x % 5 == 0 or x == 0:
            eje_x += str(x)
        else:
            eje_x += " "
    print(eje_x)
    
    return restricciones_arregladas

def analizar_soluciones(restricciones, xmin, xmax, ymin, ymax):
    """Analiza y muestra soluciones importantes"""
    print(f"\n{'='*60}")
    print("ANÁLISIS DE SOLUCIONES")
    print(f"{'='*60}")
    
    soluciones = []
    

    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            cumple_todas = True
            for restriccion in restricciones:
                if not evaluar_restriccion(restriccion, x, y):
                    cumple_todas = False
                    break
            
            if cumple_todas:
                soluciones.append((x, y))
    
    if soluciones:
        print(f"Se encontraron {len(soluciones)} soluciones enteras en la región factible")
        
        
        print("\nAlgunas soluciones importantes:")
        
        
        esquinas = []
        for x in [xmin, xmax]:
            for y in [ymin, ymax]:
                if (x, y) in soluciones:
                    esquinas.append((x, y))
        
        if esquinas:
            print("Esquinas de la región:", esquinas)
        
        
        print("\nPrimeras 10 soluciones (x, y):")
        for i, (x, y) in enumerate(soluciones[:10]):
            print(f"  {i+1}. ({x}, {y})")
        
        if len(soluciones) > 10:
            print(f"  ... y {len(soluciones) - 10} soluciones más")
    else:
        print("No se encontraron soluciones enteras en la región factible")
        print("Puede que las restricciones sean muy estrictas o los rangos muy pequeños")

def mostrar_leyenda():
    """Muestra la leyenda del gráfico"""
    print(f"\n{'='*60}")
    print("LEYENDA DEL GRÁFICO")
    print(f"{'='*60}")
    print("  · = Punto en la región factible (satisface TODAS las restricciones)")
    print("  + = Origen del sistema de coordenadas (0, 0)")
    print("  | = Eje Y (todos los puntos donde x = 0)")
    print("  - = Eje X (todos los puntos donde y = 0)")
    print("  Espacio en blanco = Punto fuera de la región factible")
    print("\nCONSEJOS:")
    print("• Cada '·' representa una combinación válida de x e y")
    print("• La forma de la región indica el tipo de restricciones")
    print("• Los vértices suelen ser soluciones importantes")

def mostrar_ejemplos():
    """Muestra ejemplos de restricciones"""
    print(f"\n{'='*60}")
    print("EJEMPLOS DE RESTRICCIONES")
    print(f"{'='*60}")
    print("1. Límites simples:")
    print("   x >= 5, y <= 10, x + y <= 15")
    print("2. Presupuesto o recursos:")
    print("   3*x + 5*y <= 20, 2*x + 3*y <= 18")
    print("3. Mínimos y máximos:")
    print("   x >= 2, y >= 3, x + y <= 12")
    print("4. Igualdades (usar <= y >=):")
    print("   x + y = 10  →  x + y <= 10 y x + y >= 10")
    print("\nSINTAXIS ACEPTADA:")
    print("• x + y <= 10, x ≥ 5, y ≥ 3")
    print("• 2*x + 3*y ≤ 15, x^2 + y^2 <= 25")
    print("• x >= 0, y >= 0 (siempre recomendado)")

def main():
    """Programa principal interactivo"""
    print("PROGRAMA INTERACTIVO PARA GRAFICAR RESTRICCIONES")
    print("="*60)
    print("Este programa grafica la región factible de un sistema de restricciones")
    print("con dos variables (x e y) usando caracteres ASCII.")
    
    while True:
        print(f"\n{'='*60}")
        print("MENÚ PRINCIPAL")
        print(f"{'='*60}")
        print("1. Ingresar nuevas restricciones")
        print("2. Ver ejemplos de restricciones")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            ingresar_restricciones()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

def ingresar_restricciones():
    """Función para ingresar restricciones interactivamente"""
    print(f"\n{'='*60}")
    print("INGRESO DE RESTRICCIONES")
    print(f"{'='*60}")
    
    nombre = input("Nombre del problema (ej: 'Planificación de tiempo'): ").strip()
    if not nombre:
        nombre = "Problema sin nombre"
    
    restricciones = []
    print(f"\nIngrese las restricciones una por línea.")
    print("Escriba 'fin' para terminar, 'ejemplo' para ver ejemplos:")
    
    i = 1
    while True:
        restr = input(f"Restricción {i}: ").strip()
        
        if restr.lower() == 'fin':
            break
        elif restr.lower() == 'ejemplo':
            mostrar_ejemplos()
            continue
        elif restr == "":
            continue
        
        
        if not ('x' in restr or 'y' in restr):
            print("   ⚠️  La restricción debe contener 'x' o 'y'")
            continue
            
        restricciones.append(restr)
        print(f"   ✅ Restricción {i} agregada: {restr}")
        i += 1
    
    if not restricciones:
        print("No se ingresaron restricciones.")
        return
    
   
    print(f"\n{'='*60}")
    print("CONFIGURACIÓN DEL GRÁFICO")
    print(f"{'='*60}")
    
    try:
        xmin = int(input("Valor mínimo para x (por defecto 0): ") or "0")
        xmax = int(input("Valor máximo para x (por defecto 20): ") or "20")
        ymin = int(input("Valor mínimo para y (por defecto 0): ") or "0")
        ymax = int(input("Valor máximo para y (por defecto 20): ") or "20")
        
        if xmin >= xmax or ymin >= ymax:
            print("Error: Los valores máximos deben ser mayores que los mínimos.")
            return
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")
        return
    
    
    restricciones_arregladas = graficar_restricciones(nombre, restricciones, xmin, xmax, ymin, ymax)
    
    
    mostrar_leyenda()
    
   
    analizar_soluciones(restricciones_arregladas, xmin, xmax, ymin, ymax)
    
    
    input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
