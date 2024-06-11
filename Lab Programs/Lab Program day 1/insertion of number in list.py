def insert_number(lst, num, pos):
    lst.insert(pos, num)
    return lst

# Example usage:
lst = [1, 2, 3, 4, 5]
num = 10
pos = 2
new_lst = insert_number(lst, num, pos)
print(new_lst)
