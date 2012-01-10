#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import product
from inspect import getsource

def latexify_source(f):
    s = getsource(f).strip()
    s = s.split(":", 1)[-1].strip()
    s = s.replace(' and ', r' \land ')
    s = s.replace(' or ', r' \lor ')
    s = s.replace(' not ', r' \lnot ')
    return r"\(" + s + r"\)"

def truthTable(f, print_expr = False):
    """ Gives you a tex-formatted truth table for the boolean function f. """
    names = f.__code__.co_varnames
    num = len(names)
    combs = product(range(2), repeat=num)
    vals = ("\t" + " & ".join(str(x) for x in c) + " & " + ("1" if f(*c) else "0") + r"\\" for c in combs)
    if print_expr:
        f_expr = latexify_source(f)
    else:
        f_expr = ""

    return r"\begin{tabular}{" + "c "*num + "| c}\n" + \
            "\t" + " & ".join(r'\(' + n + r'\)' for n in names) + r" & " + f_expr + r" \\" + "\n" + \
            "\t" + r"\hline" + "\n" + \
            "\n".join(vals) + "\n" + \
           r"\end{tabular}"

print (truthTable(
    lambda x,y,z: x and not (y and z) or not z
, True))
