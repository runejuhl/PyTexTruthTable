#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import product

def truthTable(f):
    """ Gives you a tex-formatted truth table for the boolean function f. """
    names = f.__code__.co_varnames
    num = len(names)
    combs = product(range(2), repeat=num)
    vals = ("\t" + " & ".join(str(x) for x in c) + " & " + ("1" if f(*c) else "0") + r"\\" for c in combs)

    return r"\begin{tabular}{" + "c "*num + "| c}\n" + \
            "\t" + " & ".join(r'\(' + n + r'\)' for n in names) + r" & \\" + "\n" + \
            "\t" + r"\hline" + "\n" + \
            "\n".join(vals) + "\n" + \
           r"\end{tabular}"

print (truthTable(lambda x,y,z: x and not (y and z) or not z))
