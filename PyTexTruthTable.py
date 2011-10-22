#!/bin/env python3
# -*- coding: utf-8 -*-

def truth(x,f):
    """ Return the values in set x where f(x) is true.
    """
    s = []
    for n in x:
        if f(n):
            s.append(n)
    return s

def makeTruthTable(x,f,n):
    """ Create a truth table in LaTeX from inputs x (with names n) and function f.
    """
    l = len(x[0])
    o = ""
    # begin tabular environment
    o = o + "\\begin{tabular}{c | " + "c " * l + "| c}\n"
    o = o + "$" + str(n).strip("'") + "$ & "
    # write column names
    for m in n:
        o = o + "$" + str(m) + "$ & "
    o = o + "$p" + str(n).strip("'") + "$" + " \\\\ \n \\hline \n"
    for y in x:
        o = o + "$" + str(y) + "$ & "
        for z in y:
            o = o + "$" + str(z) + "$ & "
        o = o + "$" + ("1" if f(y) else "0") + "$ \\\\ \n"
    o = o + "\\end{tabular}\n"
    return o
"""
Usage:

define set:
s = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1))

print truth table:
print(makeTruthTable(s, lambda (x,y,z): (x and not (y and z)) or not z, ("x","y","z")))
"""
