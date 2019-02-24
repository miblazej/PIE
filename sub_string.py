import string


# Znajdz pierwsze pokazanie się substringa
def sub_str(s, sub):
    counter = 0
    sub_len = len(sub)
    for i in range(len(s)):
        if counter < sub_len:
            if s[i] == sub[counter]:
                counter += 1
        elif counter == sub_len:
            return i - counter
        else:
            counter = 0
    return 0

s = 'fgdgjdfgdgjdjgdha gjgkgshk'
sub = 'a'
Flag = sub_str(s, sub)
print(Flag)
