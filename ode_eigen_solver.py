import sympy as sp

def solve_system_of_odes():
    # 1. Define time (t) and constants (c1, c2, c3) as symbols
    t = sp.Symbol('t')
    c1, c2, c3 = sp.symbols('c1 c2 c3')
    constants = [c1, c2, c3]

    # 2. Define Matrix A
    A = sp.Matrix([
        [ 5, -4,  4],
        [ 0,  3,  0],
        [-2,  4, -1]
    ])

    print("--- Matrix A ---")
    sp.pprint(A)
    print("\n")

    # 3. Find Eigenvalues and Eigenvectors
    # eigenvects() returns a list of tuples: (eigenvalue, algebraic_multiplicity, [eigenvectors])
    eigen_info = A.eigenvects()
    
    print("--- Eigenvalues & Eigenvectors ---")
    general_solution_terms = []
    const_idx = 0

    for evalue, multiplicity, evectors in eigen_info:
        for evector in evectors:
            print(f"Eigenvalue (λ): {evalue}")
            print(f"Eigenvector (v):")
            sp.pprint(evector)
            print("-" * 30)
            
            # 4. Construct terms for the general solution
            # Term = c * v * e^(λ*t)
            term = constants[const_idx] * evector * sp.exp(evalue * t)
            general_solution_terms.append(term)
            const_idx += 1

    # 5. Form the General Solution Y(t) by summing the individual terms
    # This performs matrix addition across all generated terms
    Y_t = sum(general_solution_terms, sp.zeros(3, 1))

    print("\n=== GENERAL SOLUTION Y(t) ===")
    print("Y(t) = ")
    sp.pprint(Y_t)

if __name__ == "__main__":
    solve_system_of_odes()
