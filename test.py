def test_var_args(f_arg, *argv):
    # print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


def sortarray(arr1,arr2):
    i = 0
    j = 0
    arr3 = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    if i >= len(arr1):
        arr3 += arr2[j:]
    else:
        arr3 += arr1[i:]
    return arr3

# print sortarray([1,2,3,4,8],[4,5,7,9])


class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(10)
# a.ListNode(10)
# b.ListNode(20)
a.val = 10
a.next = b
print a.val, a.next.val