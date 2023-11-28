
# import pandas as pd;
# import numpy as np;
# # import combinations from itertools
# from itertools import combinations;


# # read the data from data.txt
# df = pd.read_csv(r"D:\data_mining_lab\\freq_pattern\data.txt")

# # print the data
# print(df)
# print("\n")

# # create a list of candidates
# candidates = []
# # create a list of frequent itemsets
# frequent = []


# # create a list of unique items from the data
# items=pd.unique(df.values.ravel('K'))
# # remove the NaN values from the list
# items=items[~pd.isna(items)]

# # ask the user for the minimum support
# min_support=int(input("Enter minimum support: "))
# print("\n")

# # for each itemset
# for iterno in range(1,len(items)):
#     # create a dictionary of counts
#     count={}
#     # create a list of intermediate itemsets
#     intermediate=[]

#     # if it is the first itemset
#     if iterno == 1:
#         # add all items to the candidates list
#         candidates.append(items)
#         # for each item in the candidates list
#         for transaction in candidates[iterno-1]:
#             # count the number of times the item appears in the data
#             ctr=0
#             # for each row in the data
#             for value in df.values:
#                 # if the item is in the row
#                 if transaction in value:
#                     # increment the counter
#                     ctr+=1
#             count[transaction]=ctr
#     # if it is not the first itemset
#     else:
#         # create a list of combinations of items from the frequent itemsets
#         candidates.append(list(combinations(np.unique(np.array(frequent[iterno-2]).ravel('K')),iterno)))
#         # for each itemset in the candidates list
#         for transaction in candidates[iterno-1]:
#             # count the number of times the itemset appears in the data
#             ctr=0
#             # for each row in the data
#             for value in df.values:
#                 # if all of the items in the itemset are in the row
#                 if all(i in value for i in transaction):
#                     # increment the counter
#                     ctr+=1
#             # add the itemset and the count to the dictionary
#             count[transaction]=ctr

#     # for each itemset in the dictionary
#     for k in count.keys():
#         # if the count is greater than or equal to the minimum support
#         if count[k]>=min_support:
#             # add the itemset to the intermediate list
#             intermediate.append(k)

#     # if the intermediate list is empty
#     if intermediate == []:
#         # pretty print the frequent itemsets
#         print("Frequent itemsets are: ")
#         for item in frequent:
#             print(item)
#         # break out of the for loop
#         break

#     # add the intermediate list to the frequent itemsets
#     frequent.append(intermediate)


# Apriori Algorithm
# import pandas as pd
from collections import Counter
# min_sup = 2
print("Enter minimum support: ")
min_sup = int(input())
print("Enter minimum confidence: ")
min_con = float(input())
item_set = {}
with open("freq_pattern/data.txt", "r") as f:
    for line in f:
        line = line.strip().split(" ")
        item_set[int(line[0])] = " ".join(line[1:])



comb = []
single = Counter()  # storing single items
for val in item_set.values():
    for num in val.split(" "):
        if single.get(num) is None:
            single[num] = 0
        single[num] += 1
print("C1:")
for i in single:
    print(str(list(i))+": "+str(single[i]))
filtered = Counter()
for i in single:
    if single[i] >= min_sup:
        filtered[frozenset([i])] += single[i]
print("L1:")
for i in filtered:
    print(str(list(i))+": "+str(filtered[i]))
comb.append(filtered)

pos = 1
pl = filtered  # contains previous set

for count in range(2, 1000):
    nc = set()
    temp = list(filtered)
    for i in range(0, len(temp)):
        for j in range(i+1, len(temp)):
            t = temp[i].union(temp[j])
            if (len(t) == count):
                nc.add(t)
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for q in item_set.values():

            temp = set(q.split(" "))

            if (i.issubset(temp)):
                c[i] += 1
    if (len(c) == 0):
        continue
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    filtered = Counter()
    for i in c:
        if (c[i] >= min_sup):
            filtered[i] += c[i]
    comb.append(filtered)
    print("L"+str(count)+":")
    for i in filtered:
        print(str(list(i))+": "+str(filtered[i]))
    print()
    if (len(filtered) == 0):
        break
    pl = filtered
    pos = count
union, fin_set = list(comb[-1].values())[0], list(comb[-1].keys())[0]
rules = []
for i in range(0, len(comb)-1):
    for s in comb[i]:
        if s.issubset(fin_set) and float(union)/comb[i][s] >= min_con:
            rules.append(str(list(s))+" -> " + str(list(fin_set-s)))
print("Rules with minimum support "+str(min_sup)+" and minimum confidence "+str(min_con)+":")
print(rules)
