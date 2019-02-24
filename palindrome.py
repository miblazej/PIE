def palin_idea(x):
    if x < 0:
        return False
    else:
        temp_x = x
        leng = 0
        while temp_x:
            temp_x //= 10
            leng += 1
        i = 1
        if leng % 2 == 1:
            srodek = (leng // 2) + 1
            # zerowanie srodka
            wart_srod = x // (10 ** (srodek - 1)) % 10
            x -= (wart_srod * 10 ** (srodek - 1))
            i = 0
            while x:
                prawy = (x // (10 ** (srodek + i))) % 10
                lewy = (x // (10 ** (srodek - i - 2))) % 10
                if prawy == lewy:
                    x -= prawy * (10 ** (srodek + i))
                    x -= lewy * (10 ** (srodek - i - 2))
                    i += 1
                else:
                    return False
            return True
        else:
            temp = int(leng / 2)
            i = 0
            while x:
                prawy = (x // (10 ** (temp + i))) % 10
                lewy = (x // (10 ** (temp - i - 1))) % 10
                if prawy == lewy:
                    x -= prawy * (10 ** (temp + i))
                    x -= lewy * (10 ** (temp - i - 1))
                    i += 1
                else:
                    return False
            return True


print(palin_idea(-46456510015))
# Michal Blazej
