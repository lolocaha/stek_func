def calc(expr):
    stack = []
    i = 0
    n = len(expr)
    allowed = set("mM()," + "0123456789")
    if not expr or any(ch not in allowed for ch in expr):
        raise ValueError("Некорректное выражение")
    while i < n:
        ch = expr[i]
        if ch in 'mM':
            stack.append(ch)
            i += 1
        elif ch.isdigit():
            j = i
            while j < n and expr[j].isdigit():
                j += 1
            number = int(expr[i:j])
            stack.append(number)
            i = j
        elif ch in '(,':
            i += 1
        elif ch == ')':
            b = stack.pop()
            a = stack.pop()
            op = stack.pop()
            if op == 'm':
                result = min(a, b)
            else:
                result = max(a, b)
            stack.append(result)
            i += 1
    return f"Ответ:{stack.pop()}"
def main():
    n = int(input('Введите число:\n1 - Ввести строку и получить ответ\n0 - выход\n'))
    if n == 1:
        try:
            s = input('Введите строку:')
        except ValueError:
            print('Вы не ввели строку')
        print(calc(s))
        main()
    elif n == 0:
        return
    else:
        print('Некоректный ввод')
        main()
main()   
