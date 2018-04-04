def first_last(start_list):
    return([start_list[i] for i in [0, len(start_list) - 1] if len(start_list) > 0])

a = [ 1, 2, 3, 4, 5, "end" ]
print(first_last(a))

b = [5]
print(first_last(b))

c = []
print(first_last(c))
