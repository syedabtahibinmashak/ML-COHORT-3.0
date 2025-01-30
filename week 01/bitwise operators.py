a = 9
b = 12
ans_and = a & b
ans_or = a | b
a_not = ~ a
b_not = ~ b
print(ans_and)
print(ans_or)
print(a_not)
print(b_not)

"""
explanation for & and | operation
a = 9  >> 1001
b = 12 >> 1100
and    >> 1000 >> 8
or     >> 1101 >> 13

explanation for ~ operation
a =  9 >> 01001 >> 10110 (not operation) (negative number) >> 01001 (1's compliment) >> 01010 (2's compliment) >> 10 >> ~a = -10
b = 12 >> 01100 >> 10011 (not operation) (negative number) >> 01100 (1's compliment) >> 01101 (2's compliment) >> 13 >> ~b = -13
"""
