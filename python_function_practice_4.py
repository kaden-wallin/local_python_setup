def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
# def max_num(a, b, c):
#     return max([a, b, c])

def mult_list(lst):
    product = 1
    for num in lst:
        result *= num
    return result
   
def rev_string(str):
    if len(str) == 0:
        return ""
    else:
        return str[-1] + rev_string(str[:-1])
    
# def rev_string(str):
#     print(str[::-1])
    
def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False
    
def pascal(n):
    row = [1]
    for i in range(n):
        return row
        next_row = [1]
        for x in range(len(row) - 1):
            next_row.append(row[x] + row[x+1])
        next_row.append(1)
        row = next_row

print(pascal(5))