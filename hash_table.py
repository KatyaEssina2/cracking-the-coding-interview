import numpy as np
import copy

class HashTable(object):
    def __init__(self, length=4):
        self.array = [None]*length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kpv in self.array[index]:
                if kpv[0] == key:
                    kpv[1] = value
                    break

            else:
                self.array[index].append([key, value])
        else:
            self.array[index]= [[key, value]]

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kpv in self.array[index]:
                if kpv[0] == key:
                    return kpv[1]

            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array)/2

    def double(self):
        ht2 = HashTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for kpv in self.array[i]:
                ht2.add(kpv[0], kpv[1])
        self.array = ht2.array

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False


# Questions
# 1.1
def is_unique(test_string):
    str_ht = HashTable(length=len(test_string))
    for i in range(len(test_string)):
        if test_string[i] in str_ht:
            return False
        else:
            str_ht[test_string[i]] = i
    return True

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)

# 1.2
print(is_permutation('abcd', 'abs'))
print(is_permutation('abcd', 'bdca'))

#1.3
def url_ify(str_with_space, str_len):
    string_list = []

    for char in reversed(list(str_with_space.strip())):
        if char == ' ' and string_list[-1] != '%20':
            string_list.append('%20')
        elif char != ' ':
            string_list.append(char)

    return ''.join(reversed(string_list))

print(url_ify(' hello    this is a string', 29))

#1.4 palindrome permutation
def palindrome_permutation(test_string):
    # if its even there should be multiples of 2 of each letter (excluding white space)
    # if odd then multiples of 2 of each, and one 1
    str_list = sorted([i for i in test_string if ord(i) < 128 and i != ' '])
    chars = [0]*128

    for char in str_list:
        chars[ord(char)] += 1

    even = len(str_list) % 2 == 0
    odd_count = 0
    for freq in chars:
        if freq % 2 != 0:
            if not even and not odd_count:
                odd_count = 1
            else:
                return False
    return True

print(palindrome_permutation('helllo'))
print(palindrome_permutation('taco cat'))

#1.5
def compare_replace(str_1, str_2):
    # same length
    count_diff = 0
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            count_diff += 1
        if count_diff > 1:
            return False
    return count_diff <= 1

def compare_shift(str_1, str_2):
    long = max(str_1, str_2, key=len)
    short = min(str_1, str_2, key=len)
    for i in range(len(long)):
        if long[:i] + long[i + 1:] == short:
            return True
    else:
        return False

def one_away(str_1, str_2):
    if str_1 == str_2:
        return True
    elif abs(len(str_1) - len(str_2)) > 1:
        return False

    if len(str_1) == len(str_2):
        return compare_replace(str_1, str_2)
    else:
        return compare_shift(str_1, str_2)

print('pale', 'ple:', one_away('pale', 'ple'))
print('pale', 'pales:', one_away('pale', 'pales'))
print('pale', 'bale:', one_away('pale', 'bale'))
print('pale', 'bake:', one_away('pale', 'bake'))


#1.6
def string_compression(str_to_compress):
    # need 2 spaces one for letter, the other for count
    compressed = []
    count = 1
    for i in range(len(str_to_compress)):
        char = str_to_compress[i]
        if i < len(str_to_compress) - 1:
            prev_char = str_to_compress[i + 1]
            if char == prev_char:
                count = count + 1
            else:
                compressed.extend([char, str(count)])
                count = 1
        else:
            compressed.extend([char, str(count)])

    return str_to_compress if len(compressed) > len(str_to_compress) else ''.join(compressed)

print(string_compression('abbbaaaaccaa'))

#1.7
def rotate_layer(layer_no, matrix):
    n = matrix.shape[0] - layer_no - 1
    for i in range(layer_no, n):
        # shift col
        insert = matrix[layer_no, i] #1
        temp = matrix[i, n] #3
        matrix[i, n] = insert

        # shift row
        insert = temp #3
        temp = matrix[n, n-i + layer_no] #8
        matrix[n, n-i + layer_no] = insert

        # shift col
        insert = temp #8
        temp = matrix[n-i + layer_no, layer_no]
        matrix[n-i + layer_no, layer_no] = insert

        # shift row
        insert = temp
        matrix[layer_no, i] = insert

    return matrix



def rotate_matrix(matrix):
    no_layers = matrix.shape[0]/2 if matrix.shape[0] % 2 == 0 else (matrix.shape[0]-1)/2
    for layer in range(int(no_layers)):
        matrix = rotate_layer(layer, matrix)
    return matrix

print(rotate_matrix(np.array([[1,2, 3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])))

#1.8
def zero_matrix(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    zero_cols = set()
    zero_rows = set()

    for i in range(m):
        for j in range(n):
            if matrix[i,j] == 0:
                if j not in zero_cols:
                    zero_cols.add(j)
                if i not in zero_rows:
                    zero_rows.add(i)

    for row in zero_rows:
        for j in range(n):
            matrix[row, j] = 0
    for col in zero_cols:
        for i in range(m):
            matrix[i, col] = 0

    return matrix

print(zero_matrix(np.array([[1,1,1], [2,3,0], [1,0,0]])))

#1.9
def is_string_rotation(str_1, str_2):
    if sorted(str_1) != sorted(str_2):
        return False # not the same basic string so cant be a rotation

    concat_rotated = str_2 + str_2
    return str_1 in concat_rotated

print(is_string_rotation('waterbottle', 'erbottlewat'))
print(is_string_rotation('katya', 'atyak'))
print(is_string_rotation('abcd', 'dcba'))

