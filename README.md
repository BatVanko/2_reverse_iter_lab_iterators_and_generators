# 2_reverse_iter_lab_iterators_and_generators
Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.

Test Code

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


Output

4
3
2
1

