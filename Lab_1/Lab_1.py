import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = float(sys.argv[index])
    except:
        while(True):
            try:
                print(prompt)
                coef_str = float(input())
            except:
                continue
            break
    coef = float(coef_str)
    return coef

def Append(root, result):
    if root >= 0:
        root = math.sqrt(root)
        if root == 0:
            result.append(root)
        else:
            result.append(root)
            result.append(-root)

def get_roots(a, b, c):
    result = []
    D = b*b - 4*a*c

    if D == 0.0: 
        root = -b / (2.0*a)
        Append(root, result)

    elif D > 0.0:  
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        Append(root1, result)
        Append(root2, result)
        
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('3 корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('4 корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))    
    
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
