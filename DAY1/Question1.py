"""
Question-2: 
Given:D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
Create below:
# union of keys, #value does not matter
D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
# intersection of keys, #value does not matter
D_INTERSECTION = {'ok': 1}
D1- D2 = {'nok': 2 }
#values are added for same keys
D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }
"""
D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
D_UNION = {}

for i in D1.keys() :
    D_UNION[i] = D1[i]
for i in D2.keys() :
    D_UNION[i] = D2[i]
print(D_UNION)

D_INTERSECTION = {}
for i in D1 :
    for j in D2 :
        if D2[j] == D1[i] :
            D_INTERSECTION[i] = D1[i]
print(D_INTERSECTION)

D_MERGE = D1.copy()
for i in D2 :
    if i in D_MERGE :
        D_MERGE[i] += D2[i]
    else :
        D_MERGE[i] = D2[i]
print(D_MERGE)
