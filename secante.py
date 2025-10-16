def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("División por cero en la iteración. No se puede continuar.")
            return None

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        print(f"Iteración {i+1}: x0 = {x0:.6f}, x1 = {x1:.6f}, x2 = {x2:.6f}, f(x2) = {f(x2):.6e}")

        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            print(f"\n✅ Convergió en {i+1} iteraciones.")
            return x2

        x0, x1 = x1, x2

    print("\n❌ No convergió después del máximo de iteraciones.")
    return None


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz = secante(f, x0=1, x1=2)
    print("\nRaíz aproximada:", raiz)
