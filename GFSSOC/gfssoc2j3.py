expr = input()
expr = expr.replace('P', '+')
expr = expr.replace('M', '-')
expr = expr.removesuffix('=')
print(eval(expr)) #requires only evaluating expression by replacing P with + M with - and remove = and get expression and plug in
