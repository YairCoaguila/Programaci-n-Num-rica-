def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("La derivada es cero. No se puede continuar.")
            return None
        
        x1 = x0 - fx / dfx 
        print(f"Iteración {i+1}: x = {x1:.6f}, f(x) = {f(x1):.6e}")
        
        if abs(x1 - x0) < tol or abs(fx) < tol:
            print(f"\n✅ Convergió en {i+1} iteraciones.")
            return x1
        
        x0 = x1

    print("\n❌ No convergió después del máximo de iteraciones.")
    return None


if __name__ == "__main__":
    f  = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1
    raiz = newton_raphson(f, df, x0=1.5)
    print("\nRaíz aproximada:", raiz)
