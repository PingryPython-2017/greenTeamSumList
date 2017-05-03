# Imports

import sumList

# Tests:

print("0 + 0 + 1 = {}".format(sumList.sum_list([0, 0, 1])))

print("Nothing = {}".format(sumList.sum_list([])))

print("17 + 25 + 43 + 17 = {}".format(sumList.sum_list([17, 25, 43, 17])))

print("1 = {}".format(sumList.sum_list([1])))

print("0 = {}".format(sumList.sum_list([0])))

print("1.4 + 2.6 + 8 = {}".format(sumList.sum_list([1.4, 2.6, 8])))

print("1.4 + 2.6 + -8 = {}".format(sumList.sum_list([1.4, 2.6, -8])))

print("1 - 1 = {}".format(sumList.sum_list([1, -1])))