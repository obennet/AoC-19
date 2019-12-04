def password_combs(lowest, highest):
    pw_list = []
    x = lowest
    while x < highest:
        x += 1
        if rules(str(x)):
            pw_list.append(x)
    print(pw_list)
    return len(pw_list)


def rules(i):
    ladder = True
    twins = False

    if len(i) == 6:
        for x in range(5):
            if i[x] > i[x + 1]:
                ladder = False
            if i.count(i[x]) == 2:
                twins = True
        if ladder and twins:
            return True
    return False


print(password_combs(382345, 843167))


