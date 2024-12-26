def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    d = b ** 2 - 4 * a * c
    return d


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if d > 0:
        return(x1, x2)

    elif d == 0:
        return(- b / (2 * a))
    else:
        return('корней нет')




def solve(receipts: list):
    result = receipts[2::3] # получите правильный срез списка receipts
    return result, len(result)# этот код менять не нужно



def vote(votes):
    rez = {}
    for i in votes:
        if rez.get(i, None):
            rez[i] += 1
        else:
            rez[i] = 1
    sorted_rez = sorted(rez.items(), key=lambda item: item[1], reverse=True)
    return sorted_rez[0][0]
