a = [{1: 11}, {2: 22}, {5: 55}]
for e, idx in enumerate(a):
    # print(list(idx.values())[0], idx)
    print(idx)
#     print(e[idx], idx) # fails
#           ~^^^^^
# TypeError: 'int' object is not subscriptable

# print(type(ed[0]))  # <class 'dict'>
# print(e, type(e), idx)  # works OK
b = [1, 6]
c = [4, 7]
