# pytools/linked_lists/linked_lists.py
#
# Author: Daniel Clark, 2016

'''
This module contains the class definitions for the linked list
'''

class Node(object):
    '''
    Node for use in LinkedList class
    '''

    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, new_next):
        self._next_node = new_next


class LinkedList(object):
    '''
    Linked list class (singly-linked)
    '''

    def __init__(self):
        '''
        Init list head
        '''
        self.head = None
        self.size = 0

    def insert(self, data):
        '''
        Insert node with data into list
        '''

        # Init Node obj and point head of list to it
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def size(self):
        '''
        Return the number of nodes in list
        '''

        # Init variables
        return self.size

    def find_node(self, data):
        '''
        Find node with specified data attribute
        '''

        # Init variables
        current_node = self.head
        found = False

        # Parse through list
        while current_node and not found:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.next_node

        # Node containing data is not in list
        if current_node is None:
            raise ValueError('node not found containing data: %s' % str(data))
        else:
            return current_node

    def delete_node(self, data):
        '''
        Delete node with specified data attribute
        '''

        # Init variables
        current_node = self.head
        prev_node = None
        found = False

        # Parse through list
        while current_node and not found:
            if current_node.data == data:
                found = True
            else:
                prev_node = current_node
                current_node = current_node.next_node

        # Node containing data is not in list
        if not current_node:
            raise ValueError('node not found containing data: %s' % str(data))
        # If prev_node stays None, data was in head - set to current's next
        if not prev_node:
            self.head = current_node.next_node
        # Otherwise, set prev_node's next to current's next
        else:
            prev_node.next_node = current_node.next_node

        # Decrement size
        self.size -= 1

    def reverse(self):
        '''
        Reverse linked list (self) in place
        '''

        # Get head node and set its next to None
        curr_node = self.head
        next_node = curr_node.next_node
        curr_node.next_node = None

        while next_node:
            tmp = next_node.next_node
            next_node.next_node = curr_node
            curr_node = next_node
            next_node = tmp

        self.head = curr_node


def linked_lists_equal(a_head, b_head):
    '''
    Test if two linked lists have the same contents

    :param a_head:
    :param b_head:
    :return:
    '''

    while a_head.next_node is not None:
        if a_head.data != b_head.data:
            return False
        a_head = a_head.next_node
        b_head = b_head.next_node

    return True


def merge_sorted_lists(a_head, b_head):
    '''
    Merge two sorted linked lists into one

    :param a_head:
    :param b_head:
    :return:
    '''

    if a_head is None:
        return b_head
    if b_head is None:
        return a_head

    merge = a_head
    other = b_head

    if b_head.data < a_head.data:
        merge = b_head
        other = a_head

    merge_head = merge
    while True:
        if merge.next_node is None:
            merge.next_node = other
            break
        if other is None:
            break
        if merge.next_node.data > other.data:
            mtmp = merge.next_node
            otmp = other.next_node
            merge.next_node = other
            other.next_node = mtmp
            other = otmp

        merge = merge.next_node

    return merge_head