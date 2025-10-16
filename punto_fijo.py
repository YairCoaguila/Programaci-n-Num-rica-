def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = g(x0)
        print(f"Iteración {i+1}: x = {x1:.6f}")

        if abs(x1 - x0) < tol:
            print(f"\n✅ Convergió en {i+1} iteraciones.")
            return x1

        x0 = x1

    print("\n❌ No convergió después del máximo de iteraciones.")
    return None


if __name__ == "__main__":
    g = lambda x: (x + 2/x) / 2
    raiz = punto_fijo(g, x0=1)
    print("\nRaíz aproximada:", raiz)
