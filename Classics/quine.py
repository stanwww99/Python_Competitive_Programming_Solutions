#a quine is a program that takes no input and outputs a copy of its own source code.
a = 'print("a = " + repr(a) + "\\neval(a)")'
eval(a)