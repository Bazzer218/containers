'''
This file implements the AVL Tree data structure.
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        ret = True
        if AVLTree._balance_factor(node) in [-1, 0, 1]:
            if node.left:
                if AVLTree._balance_factor(node.left) in [-1, 0, 1]:
                    ret &= AVLTree._is_avl_satisfied(node.left)
                else:
                    ret = False
            if node.right:
                if AVLTree._balance_factor(node.right) in [-1, 0, 1]:
                    ret &= AVLTree._is_avl_satisfied(node.right)
                else:
                    ret = False
        else:
            ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.right is None:
            return old_root
        else:
            new_root = Node(old_root.right.value)
            new_root.left = Node(old_root.value)
            new_root.right = old_root.right.right
            new_root.left.right = old_root.right.left
            new_root.left.left = old_root.left
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.left is None:
            return old_root
        else:
            new_root = Node(old_root.left.value)
            new_root.right = Node(old_root.value)
            new_root.left = old_root.left.left
            new_root.right.left = old_root.left.right
            new_root.right.right = old_root.right
        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        and the textbook provides full python code.
        It is okay to add @staticmethod helper functions for this code.
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

    def insert_list(self, xs):
        for i in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, i)
            else:
                self.root = Node(i)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        use the textbook code
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right(node)
            else:
                return AVLTree._right_rotate(node)
        else:
            return node
