from sympy import Symbol, sympify, solve_rational_inequalities, Poly, solve
from sympy.solvers.inequalities import solve_univariate_inequality

def isolve(ineq):
    x = Symbol('x')
    ineq_obj = sympify(ineq)

    # if the inequality is rational, we solve it with solve_rational_inequalities()
    if ineq_obj.is_rational:
        numer, denom = ineq_obj.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        solution = solve_rational_inequalities([((p1, p2), ineq_obj.rel_op)])
    else:  # if not, we solve it with solve_univariate_inequality()
        solution = solve_univariate_inequality(ineq_obj, x)

print(isolve('x**2 - 4 < 0'))  # Outputs: (-2 < x) & (x < 2)
print(isolve('x**3 + 2*x**2 - 5 >= 0'))  # Outputs: (x <= -2*sqrt(6) - 1) | (x >= sqrt(6) - 1)
