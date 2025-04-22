def newton_raphson_numerical_recipes():
    """Pure Python implementation matching Numerical Recipes Script 2_3 with enhancements"""
    import math

    # Configuration matching the original
    MAX_ITER = 500
    TOL = 1e-6
    
    # Original equation: 4x + sin(x) - exp(x) = 0
    def f(x):
        return 4 * x + math.sin(x) - math.exp(x)
    
    def df(x):
        return 4 + math.cos(x) - math.exp(x)

    # Improved input handling
    print("Newton-Raphson Solver (Numerical Recipes Example)")
    print("Equation: 4x + sin(x) - exp(x) = 0")
    print(f"Tolerance: {TOL}\n")
    
    while True:
        try:
            x0 = float(input("Enter initial approximation: "))
            break
        except ValueError:
            print("Please enter a valid number")

    # Formatting matching original output
    print("\n{:<5} {:<16} {:<16} {:<12}".format(
        "Iter", "x_k", "f(x_k)", "Error"))
    print("-" * 55)

    xk = x0
    for k in range(1, MAX_ITER + 1):
        x_prev = xk
        fxk = f(x_prev)
        dfxk = df(x_prev)
        
        # Safeguard against zero derivative
        if abs(dfxk) < 1e-12:
            print("\nError: Zero derivative encountered")
            return None
            
        xk = x_prev - fxk / dfxk
        err = abs(xk - x_prev) / (abs(xk) + 1e-15)  # Prevent division by zero

        # Print iteration info with original spacing
        print("{:<5} {:<16.10f} {:<16.10f} {:<12.10f}".format(
            k, xk, f(xk), err))

        if err < TOL:
            print(f"\nConverged in {k} iterations")
            print(f"Root: {xk:.10f}")
            print(f"Final f(x): {f(xk):.10f}")
            return xk

    print("\nWarning: Max iterations reached without convergence")
    return xk

if __name__ == "__main__":
    newton_raphson_numerical_recipes()