# -*- coding: utf-8 -*-
"""
@author: bastian
"""

from sympy import *
x, x1, x2 = symbols("x x1 x2")
f = 1/ (1 + exp(-(x)))
f11 = x1
f12 = x2
f21 = f.subs(x, 5*f11 + f12)
f22 = f.subs(x, 2*f11 -3*f12)
f31 = f.subs(x, 3*f21 - f22)
f32 = f.subs(x, 4*f21 + 6*f22)
f41 = f.subs(x, 2*f31 + f32)

print f41