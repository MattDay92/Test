#use return functions more often than print()
#"Print is for humans.  Return is for computers"

#print odd numbers 1 - 100 - using a range going up by 2's

def odd_numbers():
    for i in range(1,101,2):
        print(i)

odd_numbers()

#range functions -- the number (stop) is not included in the list of numbers

x = range(6)
for n in x:
    print(n)

def max_num_in_list(a_list):
    return print(max(a_list))
max_num_in_list([1, 8, 6, 8, 3, 9, 11])