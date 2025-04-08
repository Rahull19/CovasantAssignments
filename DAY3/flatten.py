'''
Flattens the list
input = [1,2,3, [1,2,3, [3,4],2]] 
output = [1,2,3,1,2,3,3,4,2]
'''

def flatten(lst) :
    result = []
    for item in lst :
        if isinstance(item , list) :
            result.extend(flatten(item))
        else :
            result.append(item)
    return result
input1 = [1,2,3, [1,2,3, [3,4],2]]
output = flatten(input1)
print(f"Flattened output list : {output}")
