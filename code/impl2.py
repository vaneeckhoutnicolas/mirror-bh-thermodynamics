import sympy as sp

def dcount(atom, u, v):
    i = j = 0
    for var, cnt in atom.variable_count:
        if var == u: i += cnt
        elif var == v: j += cnt
    return (i, j)

def _subs_desc(expr, sols, rfmap, u, v):
    # substitue les derivees par ordre total decroissant (valeurs sans Derivative)
    while True:
        atoms = sorted(expr.atoms(sp.Derivative),
                       key=lambda a: -sum(c for _, c in a.variable_count))
        if not atoms:
            return expr
        a = atoms[0]
        expr = expr.subs(a, sols[dcount(a, u, v)])

def implicit_partials(P, r, u, v, order=3):
    rf = sp.Function('rf')(u, v)
    eq = P.subs(r, rf)
    sols = {}
    for tot in range(1, order + 1):
        for i in range(tot + 1):
            j = tot - i
            d = sp.diff(eq, u, i, v, j)
            target = None
            for a in d.atoms(sp.Derivative):
                if dcount(a, u, v) == (i, j):
                    target = a
            sol = sp.solve(d, target)[0]
            sols[(i, j)] = sp.together(_subs_desc(sol, sols, rf, u, v))
    return sols, rf

def S_partials_expr(Sexpr, r, u, v, sols, rf):
    Sf = Sexpr.subs(r, rf)
    out = {}
    for (i, j) in [(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3)]:
        d = sp.diff(Sf, u, i, v, j)
        out[(i, j)] = _subs_desc(d, sols, rf, u, v).subs(rf, r)
    return out
