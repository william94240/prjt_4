import copy

import rich

trucs = [
    {'name': 'Paul', 'level': 3},
    {'name': 'Nadine', 'level': 5},
    {'name': 'Martin', 'level': 2},
    {'name': 'Denise', 'level': 1},
    {'name': 'Thierry', 'level': 4}
]

trucs_copy = copy.copy(trucs)


def func_key(x):
    return x['level']


# sorted(), créé une copie, la trie et la retourne
autres_trucs = sorted(trucs, key=func_key)
rich.print(trucs)
rich.print(autres_trucs)

# .sort trie directement la liste sur laquelle on l'utilise
trucs.sort(key=func_key)
rich.print(trucs)

# lambda
trucs_copy.sort(key=lambda x: x['level'])
rich.print(trucs_copy)





# L = [ ["marc", 24], ["paul", 38], ["jeanne", 15],
#    ["jean", 21], ["philippe", 42], ["mireille", 57]]

# # def clef_age(x):
# #     return x[1]

# # print(sorted(L, key=clef_age))

# LL = sorted(L, key=lambda x: x[1])
# print(LL)