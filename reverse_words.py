import string


# stworz funckje majaca za cel odwrocenie kolejnosci wyrazow
def odwroc_slowa(s):
    index = len(s) - 1
    # nowy string
    s2 = ''
    s_pomocniczy = ''
    # zmienne majace zadeklarowac w ktorym stanie jest petla
    # wyraz jezeli true dodaje kolejna litere do s_pomocniczy
    # jezeli false if is space
    wyraz = False
    while index >= 0:
        if s[index].isalpha():
            wyraz = True
        if s[index] == ' ' and s[index - 1].isalpha() and index > 0:
            wyraz = True
        if wyraz and s[index].isalpha():
            s_pomocniczy += s[index]
        if wyraz and s[index] == ' ' and index >= 0 or wyraz and index == 0:
            wyraz = False
            s2 = s2 + ' ' + s_pomocniczy[::-1]
            s_pomocniczy = ''
        index -= 1
    return s2

s = 'Andrzej Krupa Dupa'
s2 = odwroc_slowa(s)
print(s2)
