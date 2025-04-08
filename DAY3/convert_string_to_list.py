'''
input = [[[ '(0,1,2)', '(3,4,5)'], ['(5,6,7)', '(9,4,2)']]]

output = [[[[0,1,2], [3,4,5]], [[5,6,7], [9,4,2]]]]
'''
def convert_string_to_list(inp) :
    final_result = []
    for outer in inp :
        outer_list = []
        for inner in outer :
            inner_list = []
            for item in inner :
                cleaned = item.replace("(" , "").replace(")","")
                str_num = cleaned.split(",")
                int_num = [int(x) for x in str_num]
                inner_list.append(int_num)
            outer_list.append(inner_list)
        final_result.append(outer_list)
    return final_result

inp = [[[ '(0,1,2)', '(3,4,5)'], ['(5,6,7)', '(9,4,2)']]]
out = convert_string_to_list(inp)
print(out)
