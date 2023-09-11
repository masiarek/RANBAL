scores = """\
A,B,C,D,E,F
2,5,0,3,5,4
2,5,0,3,5,5
0,5,0,3,5,1
"""

lst = scores.split("\n")

k = lst[0].split(",")
print(*k, sep=",")

for row in lst[1:]:
    a = row.split(",")
    mapping = {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
    r = [mapping[int(x)] if x.strip() else "" for x in a]
    print(*r, sep=",")
"""
B>E>F>D>A>C
B>E>F>D>A>C
B>E>D>F>A>C

"""
