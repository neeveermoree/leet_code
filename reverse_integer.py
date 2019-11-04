# Faster than 85% of Python3 solutions
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        char_list = [char for char in s]
        if char_list[0] == '-':
            char_list = char_list[1:]
        if char_list[0] == '0':
            char_list = char_list[1:]
        reverse_list = reversed(char_list)
        string_reversed_int = ''
        for integer in reverse_list:
            string_reversed_int += integer
        if string_reversed_int == '':
            string_reversed_int = '0'
        reversed_int_wo_sign = int(string_reversed_int)
        sign = -1 if x < 0 else 1
        reversed_int = reversed_int_wo_sign * sign
        if reversed_int < -(2**31) or reversed_int > 2**31 + 1:
            reversed_int = 0
        return reversed_int
