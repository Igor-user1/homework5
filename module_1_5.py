immutable_var = (1, 15.3, 'Hi', True, [1, 2])
print(immutable_var)
immutable_var[2] = 10
print(immutable_var) #кортежи относятся к неизменяемым типам данных, поэтому изменить элемент в нутри картежа не получится
mutable_list = [1, 1.2, 'yes']
mutable_list[1]='no'
mutable_list[0]=4.8
mutable_list[2]=7
print(mutable_list)