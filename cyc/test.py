

val = 0
val_list = []

def change_val(n):
    '''varaible will not change outside the fuction.'''
    val = 1

def change_lis(n):
    '''list do expand outside the function.'''
    val_list.append(n)

change_val(3)
change_lis(3)

print(val)
print(val_list)