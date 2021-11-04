import timeit
init = 'temp1 = list(range(100)); temp2 = [i * 2 for i in range(50)]'
print timeit.timeit('list(set(temp1) - set(temp2))', init, number = 100000)
print timeit.timeit('s = set(temp2);[x for x in temp1 if x not in s]', init, number = 100000)
print timeit.timeit('[item for item in temp1 if item not in temp2]', init, number = 100000)
