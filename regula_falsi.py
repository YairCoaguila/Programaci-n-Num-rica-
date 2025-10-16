def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El intervalo no es válido. f(a) y f(b) deben tener signos opuestos.")
        return None

    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        print(f"Iteración {i+1}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6e}")

        if abs(fc) < tol or abs(b - a) < tol:
            print(f"\n✅ Convergió en {i+1} iteraciones.")
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    print("\n❌ No convergió después del máximo de iteraciones.")
    return None


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz = regula_falsi(f, a=1, b=2)
    print("\nRaíz aproximada:", raiz)
