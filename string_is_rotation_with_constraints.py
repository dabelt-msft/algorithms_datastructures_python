"""Assume you have a method isSubstring which checks if one word is a substring of another. 

Given two strings, s1 and s2 write code to check if s2 is a rotation of s1 using only one call to isSubstring."""

#contraint - must be solved with one call to hypothetical is_substring - created here for testing.
def is_substring(str1, str2, str_i):
    chars = [None] * len(str2)
    for i in range(0, len(chars)):
        chars[i] = str2[str_i % len(chars)]
        if chars[i] != str1[i]:
            return False
        str_i += 1
    return True

#contraint that I must use a hypothetical
def is_string_rotation(str1, str2):
    second_i = 0
    chr1 = str1[0]
    chr2 = str2[second_i]
    while chr2 != chr1:
        second_i += 1
        if second_i >= len(str1):
            print('here')
            return False
        chr2 = str2[second_i]
    list1 = list(str1)
    return is_substring(list1, str2, second_i)


print(is_string_rotation("abce","dabc"))
print("12".isdigit())