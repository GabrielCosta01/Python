import math

def delta(a, b, c):
    result_delta = pow(b, 2) - 4 * a * c
    return result_delta

def bhaskara(a, b, c):
    result_delta = delta(a, b, c)
    
    if result_delta < 0:
        return "Delta negativo"
    else:
        raiz_delta = round(math.sqrt(result_delta), 2)
        raiz_1 = round((-b + raiz_delta) / (2 * a), 2)
        raiz_2 = round((-b - raiz_delta) / (2 * a), 2)
        return f'x1={raiz_1}, x2={raiz_2}'
    
print(bhaskara(1, 5, 2))
