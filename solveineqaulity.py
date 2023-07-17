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
