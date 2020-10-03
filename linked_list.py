class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node= Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('empty')
        for current_node in self:
            if current_node.data == target_node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
        raise Exception(f'Node with data {target_node_data} not found')

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception(f'Node with data {target_node_data} not found')

    def __len__(self):
        if not self.head:
            return 0
        node = self.head
        node_count = 0
        while node.next:
            node_count += 1
            node = node.next
        return node_count

    def tail(self):
        if not self.head:
            raise Exception('empty')

        if not self.head.next:
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next

        return current


# test
llist = LinkedList(['5','2', '2', '3'])
llist.add_after('2', Node('5'))

#2.1
def remove_dupes(llist):
    unique = set()
    if llist.head is None or llist.head.next is None:
        return llist

    prev_node = llist.head
    node = llist.head
    while node.next is not None:
        if node.data in unique:
            prev_node.next = node.next
            node = prev_node.next
        else:
            unique.add(node.data)
            prev_node = node
            node = node.next

    return llist

print(remove_dupes(llist))


def remove_dupes_no_buffer(llist):
    if llist.head is None or llist.head.next is None:
        return llist
    # sort list
    slow = llist.head

    while slow.next is not None:
        fast = slow
        prev = slow
        while fast.next is not None:
            if fast.data == slow.data:
                prev.next = fast.next
                fast = prev.next
            else:
                fast = fast.next
            prev = fast
        slow = slow.next
    return llist

print(remove_dupes_no_buffer(llist))


def get_list_length(llist):
    if llist.head.next is None:
        return 1

    node = llist.head
    count = 1
    while node.next is not None:
        node = node.next
        count += 1

    return count


def get_kth_last(llist, k):
    if llist.head is None:
        raise Exception('empty list')

    llist_length = get_list_length(llist)

    if llist_length - k == 1:
        return llist.head

    if k >= llist_length:
        raise Exception('k is greater than the list length')

    # loop until kth element and return
    count = 1
    node = llist.head
    while count != llist_length - k:
        count += 1
        node = node.next

    return node.data

print(llist)
print(get_kth_last(llist, 0))


#recursive
def get_kth_last_recursively(head, k):
    if head is None:
        return 0

    index = get_kth_last_recursively(head.next, k) + 1
    if index == k:
        print(head.data)
    return index

get_kth_last_recursively(llist.head, 1)


def get_kth_last_element(head, k):
    #update a global variable
    global index
    index = 0

    def get_kth_last(head, k):
        global index
        if head.next is None:
            # the end node, i = 1
            return head
        node = get_kth_last_recursively(head, k)
        index += 1
        if index == k:
            return head
        return node

    get_kth_last(head, k)

get_kth_last_element(llist.head, 2)


#2.3
def delete_middle_node(node_to_delete):
    if node_to_delete.next is None:
        return

    next_data = node_to_delete.next.data
    node_to_delete.data = next_data
    node_to_delete.next = node_to_delete.next.next

    return

print(llist)
delete_middle_node(llist.head.next)
print(llist)


#2.4
def partition_x(llist, partition):
    if llist.head is None:
        raise Exception('not a valid list')

    before = LinkedList()
    after = LinkedList()
    node = llist.head
    before_node = None

    while node is not None:
        if int(node.data) < int(partition):
            before_node = Node(node.data)
            before.add_last(before_node)
        else:
            after.add_last(Node(node.data))
        node = node.next

    if before_node is not None:
        before_node.next = after.head
        llist.head = before.head


llist = LinkedList(['5', '2', '7', '2', '11', '3'])
print(llist)
partition_x(llist, '11')
print(llist)

#2.5
def sum_digits(a, b, carry):
    a_data = int(a.data) if a is not None else 0
    b_data = int(b.data) if b is not None else 0

    sum = str(a_data + b_data + carry)
    carry = int(sum[:-1]) if len(sum) > 1 else 0
    return int(sum[-1:]), carry


def sum_lists(llist_1, llist_2):
    llist_total = LinkedList()
    if llist_1.head is None and llist_2.head is None:
        raise Exception('invalid')

    node_1 = llist_1.head
    node_2 = llist_2.head
    carry = 0

    while node_1 is not None or node_2 is not None:
        sum, carry = sum_digits(node_1, node_2, carry)
        llist_total.add_last(Node(str(sum)))
        if node_1 is not None:
            node_1 = node_1.next
        if node_2 is not None:
            node_2 = node_2.next

    return llist_total

print('sum')
print(sum_lists(LinkedList(['8', '2', '1']), LinkedList(['3', '1'])))
# to do this for non reversed lists - call sum recursively, passing back carry

# 2.6
def palindrome(llist):
    global reversed_list
    reversed_list = LinkedList()

    def add_reversed_nodes(head):
        global reversed_list
        if head.next is None:
            return head
        node = add_reversed_nodes(head.next)
        reversed_list.add_last(Node(node.data))
        return head

    add_reversed_nodes(llist.head)
    reversed_list.add_last(Node(llist.head.data))
    node = llist.head
    reverse_node = reversed_list.head

    while node is not None:
        if reverse_node is None or node.data != reverse_node.data:
            return False
        reverse_node = reverse_node.next
        node = node.next
    return True

llist = LinkedList(['8', '4', '1', '4', '8'])
print(palindrome(llist))


# 2.7
def intersection(llist_1, llist_2):
    # how to define by reference relationship?

    if llist_1.tail() != llist_2.tail():
        # dont end in the same place so cant possibly intersect
        return False

    len_1 = len(llist_1)
    len_2 = len(llist_2)

    short = llist_2 if len_1 > len_2 else llist_1
    long = llist_2 if len_2 > len_1 else llist_1
    long_start = long.head
    short_start = short.head
    for i in range(int(len_1-len_2)):
        long_start = long_start.next

    #start at the same place and look for an intersection
    while long_start.next:
        if long_start == short_start:
            return long_start
        long_start = long_start.next
        short_start = short_start.next

    return False


intersecting_node = Node('1')
intersecting_node.next = Node('2')
long_list = LinkedList(['1', '3'])
long_list.add_last(intersecting_node)
short_list = LinkedList(['5'])
short_list.add_last(intersecting_node)

print(long_list)
print(short_list)
print(intersection(long_list, short_list))


# 2.8
def loop_detection(llist):
    if llist.head is None or llist.head.next is None:
        return False

    # head cant be the start of the loop by definition
    slow = llist.head
    fast = llist.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return False

print(loop_detection(llist))

llist = LinkedList(['1', '2'])
node = Node('3')
node_2 = Node('4')

node_2.next = node
node.next = node_2
llist.add_last(node_2)

print(loop_detection(llist))