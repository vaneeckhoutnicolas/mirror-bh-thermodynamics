import sympy as sp

NMAX = 8  # puissance max conservee

class Ser:
    __slots__ = ('c',)
    def __init__(self, c=None):
        self.c = dict(c) if c else {}
    @staticmethod
    def const(v):
        v = sp.sympify(v)
        return Ser({0: v}) if v != 0 else Ser()
    @staticmethod
    def x(p=1):
        return Ser({p: sp.Integer(1)})
    def _cl(self):
        self.c = {k: sp.expand(v) for k, v in self.c.items()
                  if k <= NMAX and sp.expand(v) != 0}
        return self
    def __add__(s, o):
        o = o if isinstance(o, Ser) else Ser.const(o)
        r = Ser(s.c)
        for k, v in o.c.items():
            r.c[k] = r.c.get(k, 0) + v
        return r._cl()
    __radd__ = __add__
    def __neg__(s):
        return Ser({k: -v for k, v in s.c.items()})
    def __sub__(s, o):
        o = o if isinstance(o, Ser) else Ser.const(o)
        return s + (-o)
    def __rsub__(s, o):
        return (-s) + o
    def __mul__(s, o):
        o = o if isinstance(o, Ser) else Ser.const(o)
        r = Ser()
        for k1, v1 in s.c.items():
            for k2, v2 in o.c.items():
                k = k1 + k2
                if k <= NMAX:
                    r.c[k] = r.c.get(k, 0) + v1*v2
        return r._cl()
    __rmul__ = __mul__
    def inv(s):
        p0 = min(s.c)
        u = {k - p0: v for k, v in s.c.items()}
        n = NMAX + abs(p0) + 2
        inv = {0: sp.expand(1/u[0])}
        for k in range(1, n + 1):
            acc = sp.Integer(0)
            for j in range(1, k + 1):
                if j in u and (k - j) in inv:
                    acc += u[j]*inv[k - j]
            inv[k] = sp.expand(-acc/u[0])
        return Ser({k - p0: v for k, v in inv.items()})._cl()
    def __truediv__(s, o):
        o = o if isinstance(o, Ser) else Ser.const(o)
        return s * o.inv()
    def __rtruediv__(s, o):
        return Ser.const(o) * s.inv()
    def __pow__(s, n):
        n = int(n)
        if n < 0:
            return s.inv()**(-n)
        r = Ser.const(1)
        b = s
        while n:
            if n & 1:
                r = r*b
            b = b*b
            n >>= 1
        return r
    def coeff(s, k):
        return sp.expand(s.c.get(k, sp.Integer(0)))
    def conj(s):
        return Ser({k: sp.conjugate(v) for k, v in s.c.items()})

def evaluate(expr, env):
    # evalue une expression sympy (Add/Mul/Pow/Symbol/Number) en series
    if not expr.free_symbols:
        return Ser.const(expr)
    if expr.is_Number:
        return Ser.const(expr)
    if expr.is_Symbol:
        return env[expr] if expr in env else Ser.const(expr)
    if expr.is_Add:
        r = Ser()
        for a in expr.args:
            r = r + evaluate(a, env)
        return r
    if expr.is_Mul:
        r = Ser.const(1)
        for a in expr.args:
            r = r * evaluate(a, env)
        return r
    if expr.is_Pow:
        b, e = expr.args
        if e.is_Integer:
            return evaluate(b, env)**int(e)
        raise ValueError(f"pow non entier: {expr}")
    if expr is sp.I:
        return Ser.const(sp.I)
    raise ValueError(f"noeud non gere: {expr}")

def implicit_partials(P, r, u, v, order=3):
    # P(r(u,v),u,v)=0 -> dict {(i,j): expr en (r,u,v,...)}
    rf = sp.Function('rf')(u, v)
    eq = P.subs(r, rf)
    sols = {}
    for tot in range(1, order + 1):
        for i in range(tot + 1):
            j = tot - i
            d = sp.diff(eq, u, i, v, j)
            for (ii, jj), val in sorted(sols.items(), key=lambda t: -(t[0][0]+t[0][1])):
                d = d.subs(sp.Derivative(rf, (u, ii), (v, jj)) if jj and ii else
                           (sp.Derivative(rf, (u, ii)) if ii and not jj else sp.Derivative(rf, (v, jj))), val)
            target = (sp.Derivative(rf, (u, i), (v, j)) if i and j else
                      (sp.Derivative(rf, (u, i)) if i else sp.Derivative(rf, (v, j))))
            sol = sp.solve(d, target)
            sols[(i, j)] = sp.together(sol[0])
    return {k: val.subs(rf, r) for k, val in sols.items()}

def S_partials(Sexpr, rpart, r, u, v, order=3):
    # partials totaux de S(r(u,v),u,v) en termes de (r,u,v)
    rf = sp.Function('rf')(u, v)
    Sf = Sexpr.subs(r, rf)
    out = {}
    rp = { (i,j): val.subs(r, rf) for (i,j), val in rpart.items() }
    for tot in range(2, order + 2):
        for i in range(tot + 1):
            j = tot - i
            if not (2 <= i + j <= 3):
                continue
            d = sp.diff(Sf, u, i, v, j)
            for (ii, jj), val in sorted(rp.items(), key=lambda t: -(t[0][0]+t[0][1])):
                target = (sp.Derivative(rf, (u, ii), (v, jj)) if ii and jj else
                          (sp.Derivative(rf, (u, ii)) if ii else sp.Derivative(rf, (v, jj))))
                d = d.subs(target, val)
            out[(i, j)] = d.subs(rf, r)
    return out

def brioschi_RS(Sp, Sser, sg=-1):
    # Sp: dict (i,j)-> Ser ; Sser: Ser de S ; renvoie Ser de R*S
    E, F, G = sg*Sp[(2,0)], sg*Sp[(1,1)], sg*Sp[(0,2)]
    Ex, Ey = sg*Sp[(3,0)], sg*Sp[(2,1)]
    Fx, Fy = sg*Sp[(2,1)], sg*Sp[(1,2)]
    Gx, Gy = sg*Sp[(1,2)], sg*Sp[(0,3)]
    def det3(a):
        return (a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
              - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0])
              + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]))
    m1 = [[Ser(), Ex*sp.Rational(1,2), Fx - Ey*sp.Rational(1,2)],
          [Fy - Gx*sp.Rational(1,2), E, F],
          [Gy*sp.Rational(1,2), F, G]]
    m2 = [[Ser(), Ey*sp.Rational(1,2), Gx*sp.Rational(1,2)],
          [Ey*sp.Rational(1,2), E, F],
          [Gx*sp.Rational(1,2), F, G]]
    K = (det3(m1) - det3(m2)) / (E*G - F*F)**2
    return 2*K*Sser

def newton_root(Pexpr, r, xsym, r0ser, env_base, steps=5):
    Pr = sp.diff(Pexpr, r)
    cur = r0ser
    for _ in range(steps):
        env = dict(env_base); env[r] = cur
        cur = cur - evaluate(Pexpr, env)/evaluate(Pr, env)
    return cur
