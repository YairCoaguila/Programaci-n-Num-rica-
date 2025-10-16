def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El intervalo no es válido. f(a) y f(b) deben tener signos opuestos.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        print(f"Iteración {i+1}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6e}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\n✅ Convergió en {i+1} iteraciones.")
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("\n❌ No convergió después del máximo de iteraciones.")
    return None


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz = biseccion(f, a=1, b=2)
    print("\nRaíz aproximada:", raiz)
