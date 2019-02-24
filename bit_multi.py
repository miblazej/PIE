def bit_multi(x, y):
        rs = 0
        while x:
                if x & 1:
                        rs = add_bit(rs, y)
                x, y = x >> 1, y << 1
        return rs


def add_bit(x, y):
        carry, temp_x, temp_y, k, running_sum = 0, x, y, 1, 0
        ak, bk = 0, 0
        while temp_x | temp_y:
                ak, bk = (x & k), (y & k)
                carryout = (ak & bk) | (bk & carry) | (ak & carry)
                running_sum |= ak ^ bk ^ carry
                carry, k, temp_x, temp_y = (carryout << 1, k << 1, temp_x >> 1,
                                            temp_y >> 1)

        return running_sum | carry

sum = bit_multi(10, 10)
print(str(sum))
