# Solution 1

def transfer(num,arr):
    i=1
    while i<num+1:
        last_item = arr[-1]
        arr=arr[:-1]
        arr.insert(0,last_item)
        i+=1
    return arr 

#############################

# Solution 2

def intersected_arrays(arr1,arr2):
    arr1_without_duplicates = []
    intersection_arr = []
    [arr1_without_duplicates.append(x) for x in arr1 if x not in arr1_without_duplicates]
    for i in arr1_without_duplicates:
        if i in arr2:
            intersection_arr.append(i)
    return intersection_arr

###############################

# Solution 3

def arr_sum(arr):
    s=0
    new = []
    for i in range(0, len(arr)-1):
        s+=arr[i]
        new.append(s)
    return  new

################################

# Solution 4

def valid_parentheses(expr):

    new = []
    for char in expr:
        if char in ["(", "{", "["]:
            new.append(char)
        else:
            if not new:
                return False
            current_char = new.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if new:
        return False
    return True