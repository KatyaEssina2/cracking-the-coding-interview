class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

#3.1
# (index - 1)/3 gives index of stack
# to pop get first index and shift all others into place
# to add to onto stack, add 3 to the front of the array and put new val into the right index'

# design a class

class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values = [None] * self.stack_capacity * self.number_of_stacks
        self.sizes = [0] * self.number_of_stacks

    def push(self, value, stack_number):
        if self.is_full(stack_number):
            raise Exception(f'stack number {stack_number} is full.')

        self.sizes[stack_number] += 1
        self.values[self.index_of_top(stack_number)] = value

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            raise Exception(f'stack number {stack_number} is empty')

        top_index = self.index_of_top(stack_number)
        value = self.values[top_index]
        self.values[top_index] = None
        self.sizes[stack_number] -= 1
        return value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            raise Exception(f'stack number {stack_number} is empty')
        return self.values[self.index_of_top(stack_number)]

    def is_empty(self, stack_number):
        return self.sizes[stack_number] == 0

    def is_full(self, stack_number):
        return self.sizes[stack_number] == self.stack_capacity

    def index_of_top(self, stack_number):
        # split by stack capacity
        offset = stack_number * self.stack_capacity
        return offset + self.sizes[stack_number] - 1

    def __repr__(self):
        return f'[{", ".join(str(x) for x in self.values)}]'

multi_stack = MultiStack(2)
print(multi_stack)
multi_stack.push(1, 1)
multi_stack.push(1, 1)
print(multi_stack.pop(1))
print(multi_stack)

#3.2
from linked_list import LinkedList
class StackWithMin:
    def __init__(self):
        self.stack = LinkedList()

    def peek(self):
        if self.is_empty:
            raise Exception('stack is empty')

    def pop(self):
