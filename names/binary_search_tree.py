"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# from queue import Queue
# from stack import Stack
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __add_left__(self, value):
        self.left = BSTNode(value)

    def __add_right__(self, value): #__ __ conventionally makes this a private method
        self.right = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.__add_left__(value)
                return
            self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.__add_right__(value)
                return
            self.right.insert(value)

        #left case?
        # check if value is less than the root value
            # move to the left and check if it is none?
            # if none, insert node here
        # otherwise
            # call insert on the root's left node
        
        # Right case?
        # otherwise
            # move to the right and check if it is none? 
                # if none, insert node here
            # otherwise
                # call insert on the root's right node



        # other / base case
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True

        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


        """
        Base case:
            check the root node value against the target 
            if the root node's value and the target are the same,
            return True
        
        Left case:
            check if the target value is less than the root's value
                check if there is no child to the left, if True:
                    return False
                otherwise
                    call contains on the left child

        Right case:
            otherwise
                check if there is no child to the right
                    return False
                otherwise
                    call contains on the right child


        """
        

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        current = self
        while current.right is not None:
            current = current.right
        return current.value
        

            

    # # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        fn(self.value)

        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.value is None:
            pass

        if self.left is not None:
            self.left.in_order_print()
        
        print(self.value)

        if self.right is not None:
            self.right.in_order_print()



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
#     def bft_print(self):
#         queue = Queue()
#         queue.enqueue(self)

#         while queue:
#             current = queue.dequeue()
#             print(current.value)

#             if current.left:
#                 queue.enqueue(current.left)

#             if current.right:
#                 queue.enqueue(current.right)

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self):
#         queue = Stack()
#         queue.push(self)

#         while queue:
#             current = queue.pop()
#             print(current.value)

#             if current.left:
#                 queue.push(current.left)

#             if current.right:
#                 queue.push(current.right)


#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self):
#         queue = Stack()
#         queue.push(self)

#         while queue:
#             current = queue.pop()
#             print(current.value)

#             if current.left:
#                 current.left.pre_order_dft()

#             if current.right:
#                 current.right.pre_order_dft()
#     # Print Post-order recursive DFT
#     def post_order_dft(self):
#         queue = Stack()
#         queue.push(self)

#         while queue:
#             current = queue.pop()

#             if current.left:
#                 current.left.post_order_dft()

#             if current.right:
#                 current.right.post_order_dft()

#             print(current.value)
# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
