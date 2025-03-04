# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_avl

import unittest
import time
from avl import AVLTree


class TestAVLTree(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        Test 1: A AVLTree exists.
        """
        try:
            AVLTree()
        except NameError:
            self.fail("Could not instantiate AVLTree.")

    def test_initial_attributes(self):
        """
        Test 2: A AVL Tree is a recursive structure. When we refer to an object that "is a avl_tree,"
        we are referring to a root node of an AVL tree.
        Every node has a left child, right child, key, height, and balance factor.
        A new AVLTree has a left, right, key, that are each None, a height set to 1 and a balance factor set to 0.
        Hint: Define an initializer.
        """
        avl_tree = AVLTree()
        self.assertIsNone(avl_tree.left)
        self.assertIsNone(avl_tree.right)
        self.assertIsNone(avl_tree.key)
        self.assertEqual(0, avl_tree.height)
        self.assertEqual(0, avl_tree.balance_factor)

    """
    Cute, single-level trees. (Depth of zero.)
    Insertion
    When inserting a node, calculate the height of each node 
    """

    def test_height_single_smaller(self):
        """
        Test 3: Inserting a node into a single-level tree appends the new node as the
        left child, when the new node key is less than the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        The height of each node is equal to the height of its largest child + 1
        """
        avl_tree = AVLTree(5)
        child = AVLTree(1)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.left)
        self.assertEqual(1, avl_tree.height)
        self.assertEqual(0, avl_tree.left.height)
        
    def test_height_single_equal(self):
        """
        Test 4: Inserting a node into a single-level tree appends the new node as the
        left child, when the new node value is equal to the the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        The height of each node is equal to the height of its largest child + 1
        """
        avl_tree = AVLTree(5)
        child = AVLTree(5)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.left)
        self.assertEqual(1, avl_tree.height)
        self.assertEqual(0, avl_tree.left.height)

    def test_height_single_greater(self):
        """
        Test 5: Inserting a node into a single-level tree appends the new node as the
        right child, when the new node key is greater than the parent's key.
        (A new node whose key is > parent key becomes the right child.)
        The height of each node is equal to the height of its largest child + 1
        """
        avl_tree = AVLTree(5)
        child = AVLTree(7)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.right)
        self.assertEqual(1, avl_tree.height)
        self.assertEqual(0, avl_tree.right.height)

    """
    Cute, single-level trees. (Depth of zero.)
    Insertion
    When inserting a node, calculate the balance factor of each node 
    """

    def test_balance_factor_single_smaller(self):
        """
        Test 6: Inserting a node into a single-level tree appends the new node as the
        left child, when the new node key is less than the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        The balance factor of each node is equal to the height of its left sub-tree 
        minus the height of its right subtree
        """
        avl_tree = AVLTree(5)
        child = AVLTree(1)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.left)
        self.assertEqual(1, avl_tree.balance_factor)
        self.assertEqual(0, avl_tree.left.balance_factor)
        
    def test_balance_factor_single_equal(self):
        """
        Test 7: Inserting a node into a single-level tree appends the new node as the
        left child, when the new node value is equal to the the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        The balance factor of each node is equal to the height of its left sub-tree 
        minus the height of its right subtree
        """
        avl_tree = AVLTree(5)
        child = AVLTree(5)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.left)
        self.assertEqual(1, avl_tree.height)
        self.assertEqual(0, avl_tree.left.height)

    def test_balance_factor_single_greater(self):
        """
        Test 8: Inserting a node into a single-level tree appends the new node as the
        right child, when the new node key is greater than the parent's key.
        (A new node whose key is > parent key becomes the right child.)
        The balance factor of each node is equal to the height of its left sub-tree 
        minus the height of its right subtree
        """
        avl_tree = AVLTree(5)
        child = AVLTree(7)
        avl_tree.insert(child)
        self.assertEqual(child, avl_tree.right)
        self.assertEqual(1, avl_tree.height)
        self.assertEqual(0, avl_tree.right.height)

    """
    Toddler, two-level trees. (Depth of one.)
    Insertion
    Calculate height and balance factor
    Assume NO rotation machinery yet
    """

    # def test_height_insert_two_smaller_left(self):
    #     """
    #     Test 9: Inserting a node with a key that is less than the left child's key appends
    #     the new node as the left child's left child. 
    #     The height of each node is equal to the height of its largest child + 1
    
    #       5             5          
    #      /     =>      /           
    #     3             3           
    #                  /
    #                 1
       
    #     """
    #     avl_tree = AVLTree(5)
    #     three = AVLTree(3)
    #     one = AVLTree(1)
    #     avl_tree = avl_tree.insert(three)
    #     avl_tree = avl_tree.insert(one)
    #     self.assertEqual(three, avl_tree.left)
    #     self.assertEqual(one, avl_tree.left.left)
    #     self.assertEqual(2, avl_tree.height)
    #     self.assertEqual(1, avl_tree.left.height)
    #     self.assertEqual(0, avl_tree.left.left.height)
       

    # def test_balance_factor_insert_two_smaller_left(self):
    #     """
    #     Test 10: Inserting a node with a key that is less than the left child's key appends
    #     the new node as the left child's left child. 
    #     The height of each node is equal to the height of its largest child + 1
    
    #       5             5          
    #      /     =>      /           
    #     3             3           
    #                  /
    #                 1
       
    #     """
    #     avl_tree = AVLTree(5)
    #     three = AVLTree(3)
    #     one = AVLTree(1)
    #     avl_tree.insert(three)
    #     avl_tree.insert(one)
    #     self.assertEqual(three, avl_tree.left)
    #     self.assertEqual(one, avl_tree.left.left)
    #     self.assertEqual(2, avl_tree.balance_factor)
    #     self.assertEqual(1, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.left.left.balance_factor)
       

    #********************************************
    # !!!!!IMPORTANT!!!!!
    #**********************************************
    # COMMENT OUT TESTS 9 & 10 BEFORE PROCEEDING
    #************************************************
   
    def test_return_root_insert_two_smaller(self):
        """
        Test 11: Insert returns the root of the three
    
           5             5           
                 =>     /     
                       3           
                      
                     
        """
        avl_tree = five = AVLTree(5)
        three = AVLTree(3)
        avl_tree_root=avl_tree.insert(three)
        self.assertEqual(five, avl_tree_root)

    
    # """
    # Toddler, two-level trees.
    # Insertion
    # Left Imbalance, right rotation
    # # """    
    def test_right_rotate_insert_two_smaller(self):
        """
        Test 12: Inserting a node with a key that is less than the left child's key 
        causes a right rotation
    
                  5           3
                 /    =>     / \  
                3           1   5
               /
              1
       
        HINT:  create a right_rotate method
        """
        avl_tree = five = AVLTree(5)
        three = AVLTree(3)
        one = AVLTree(1)
        avl_tree=avl_tree.insert(three)
        avl_tree=avl_tree.insert(one)
        self.assertEqual(three, avl_tree)
        self.assertEqual(one, avl_tree.left)
        self.assertEqual(five, avl_tree.right)


    # def test_height_right_rotate_insert_two_smaller(self):
    #     """
    #     Test 13: Inserting a node with a key that is less than the left child's key 
    #     causes a right rotation
    #     The height of each node is equal to the height of its largest child + 1
    
    #               5           3
    #              /    =>     / \  
    #             3           1   5
    #            /
    #           1
       
    #     """
    #     avl_tree = five= AVLTree(5)
    #     three = AVLTree(3)
    #     one = AVLTree(1)
    #     avl_tree=avl_tree.insert(three)
    #     avl_tree=avl_tree.insert(one)
    #     self.assertEqual(1, avl_tree.height)
    #     self.assertEqual(0, avl_tree.left.height)
    #     self.assertEqual(0, avl_tree.right.height)

    # def test_balance_factor_right_rotate_insert_two_smaller(self):
    #     """
    #     Test 14: Inserting a node with a key that is less than the left child's key 
    #     causes a right rotation
    #     The balance factor of each node is equal to the difference between the height
    #     of the left subtree and the right subtree
    
    #               5          3
    #              /    =>    / \  
    #             3          1   5
    #            /
    #           1
                     
    #     """
    #     avl_tree = five= AVLTree(5)
    #     three = AVLTree(3)
    #     one = AVLTree(1)
    #     avl_tree=avl_tree.insert(three)
    #     avl_tree=avl_tree.insert(one)
    #     self.assertEqual(0, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)

    # # """
    # # Toddler, two-level trees.
    # # Insertion
    # # Right Imbalance, Left rotatation
    # # # """    
    # def test_left_rotate_insert_two_smaller_left(self):
    #     """
    #     Test 15: Inserting a node with a key that is less than the right child's key 
    #     causes a left rotation
    
    #        5                 7
    #         \     =>        / \  
    #          7             5   9
    #           \        
    #            9      
       
    #     HINT:  create a left_rotate method
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     nine = AVLTree(9)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(nine)
    #     self.assertEqual(seven, avl_tree)
    #     self.assertEqual(five, avl_tree.left)
    #     self.assertEqual(nine, avl_tree.right)


    # def test_height_left_rotate_insert_two_smaller(self):
    #     """
    #     Test 16: Inserting a node with a key that is less than the right child's key 
    #     causes a left rotation
    #     The height of each node is equal to the height of its largest child + 1
    
    #        5                 7
    #         \     =>        / \  
    #          7             5   9
    #           \        
    #            9      
       
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     nine = AVLTree(9)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(nine)
    #     self.assertEqual(1, avl_tree.height)
    #     self.assertEqual(0, avl_tree.right.height)
    #     self.assertEqual(0, avl_tree.left.height)

    # def test_balance_factor_left_rotate_insert_two_smaller(self):
    #     """
    #     Test 17: Inserting a node with a key that is less than the right child's key 
    #     causes a left rotation
    #     The balance factor of each node is equal to the difference between the height
    #     of the left subtree and the right subtree
    #        5                 7
    #         \     =>        / \  
    #          7             5   9
    #           \        
    #            9      
       
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     nine = AVLTree(9)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(nine)
    #     self.assertEqual(0, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
 
    # # """
    # # Toddler, two-level trees.
    # # Insertion
    # # Left Subtree Right Imbalance. Left Rotation Followed By Right rotation
    # # # """    
    # def test_left_right_rotate_insert_two_smaller(self):
    #     """
    #     Test 18: Inserting a node with a key that is greater than the left child's key 
    #     causes a left rotation followed by a right rotation
    
    #               5           5           4
    #              /    =>     /    =>     / \ 
    #             3           4           3   5
    #              \         /
    #               4       3
       
    #     HINT:  left rotate around node 3 followed by right_rotate around node 5
    #     """
    #     avl_tree = five = AVLTree(5)
    #     three = AVLTree(3)
    #     four = AVLTree(4)
    #     avl_tree=avl_tree.insert(three)
    #     avl_tree=avl_tree.insert(four)
    #     self.assertEqual(four, avl_tree)
    #     self.assertEqual(three, avl_tree.left)
    #     self.assertEqual(five, avl_tree.right)


    # def test_height_left_right_rotate_insert_two_smaller(self):
    #     """
    #     Test 19: Inserting a node with a key that is greater than the left child's key 
    #     causes a left rotation followed by a right rotation
    #     The height of each node is equal to the height of its largest child + 1
    
    #               5           5           4
    #              /    =>     /    =>     / \ 
    #             3           4           3   5
    #              \         /
    #               4       3
       
    #     """
    #     avl_tree = five = AVLTree(5)
    #     three = AVLTree(3)
    #     four = AVLTree(4)
    #     avl_tree=avl_tree.insert(three)
    #     avl_tree=avl_tree.insert(four)
    #     self.assertEqual(1, avl_tree.height)
    #     self.assertEqual(0, avl_tree.left.height)
    #     self.assertEqual(0, avl_tree.right.height)


    # def test_balance_factor_left_right_rotate_insert_two_smaller(self):
    #     """
    #     Test 20: Inserting a node with a key that is greater than the left child's key 
    #     causes a left rotation followed by a right rotation
    #     The balance factor of each node is equal to the difference between the height
    #     of the left subtree and the right subtree
    
    #               5           5           4
    #              /    =>     /    =>     / \ 
    #             3           4           3   5
    #              \         /
    #               4       3
                     
    #     """
    #     avl_tree = five = AVLTree(5)
    #     three = AVLTree(3)
    #     four = AVLTree(4)
    #     avl_tree=avl_tree.insert(three)
    #     avl_tree=avl_tree.insert(four)
    #     self.assertEqual(0, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)

    # # """
    # # Toddler, two-level trees.
    # # Insertion
    # # Right Subtree Left Imbalance. Right Rotation Followed By Left rotation
    # # # """    
    # def test_right_left_rotate_insert_two_smaller(self):
    #     """
    #     Test 21: Inserting a node with a key that is less than the right child's key 
    #     causes a right rotation followed by a left rotation

    #        5              5             6
    #         \     =>       \   =>      / \
    #          7              6         5   7 
    #         /                \
    #        6                  7      
       
    #     HINT:  right rotate around node 7 followed by left rotate around node 5
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     six = AVLTree(6)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(six)
    #     self.assertEqual(six, avl_tree)
    #     self.assertEqual(five, avl_tree.left)
    #     self.assertEqual(seven, avl_tree.right)


    # def test_height_right_left_rotate_insert_two_smaller(self):
    #     """
    #     Test 22: Inserting a node with a key that is less than the right child's key 
    #     causes a right rotation followed by a left rotation
    #     The height of each node is equal to the height of its largest child + 1

    #        5              5             6
    #         \     =>       \   =>      / \
    #          7              6         5   7 
    #         /                \
    #        6                  7      
       
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     six = AVLTree(6)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(six)
    #     self.assertEqual(1, avl_tree.height)
    #     self.assertEqual(0, avl_tree.left.height)
    #     self.assertEqual(0, avl_tree.right.height)


    # def test_balance_factor_right_left_rotate_insert_two_smaller(self):
    #     """
    #     Test 23: Inserting a node with a key that is less than the right child's key 
    #     causes a right rotation followed by a left rotation
    #     The balance factor of each node is equal to the difference between the height
    #     of the left subtree and the right subtree
    
    #        5              5             6
    #         \     =>       \   =>      / \
    #          7              6         5   7 
    #         /                \
    #        6                  7      
                     
    #     """
    #     avl_tree = five = AVLTree(5)
    #     seven = AVLTree(7)
    #     six = AVLTree(6)
    #     avl_tree=avl_tree.insert(seven)
    #     avl_tree=avl_tree.insert(six)
    #     self.assertEqual(0, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)


    # """
    # Teen-age, three-level trees. (Depth of two.)
    # Hint: Don't just curse - be recursive.
    # """

    # def test_three_level_tree_height(self):
    #     """
    #     Test 24: Height of each node is one bigger than tha max of its child's heights
    #          10                
    #         /  \            
    #       5      15    
    #      / \                    
    #     2   7                  
                         
                        
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """
    #     avl_tree = AVLTree(10)
    #     avl_tree.insert(AVLTree(5))
    #     avl_tree.insert(AVLTree(15))
    #     avl_tree.insert(AVLTree(2))
    #     avl_tree.insert(AVLTree(7))
    #     self.assertEqual(2, avl_tree.height)
    #     self.assertEqual(1, avl_tree.left.height)
    #     self.assertEqual(0, avl_tree.left.left.height)
    #     self.assertEqual(0, avl_tree.left.right.height)
    #     self.assertEqual(0, avl_tree.right.height)

    # def test_three_level_tree_balance_factor(self):
    #     """
    #     Test 25: Balance factor of each node is the difference between its heights
    #          10                
    #         /  \            
    #       5      15    
    #      / \                    
    #     2   7                  
                         
                        
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """
    #     avl_tree = AVLTree(10)
    #     avl_tree.insert(AVLTree(5))
    #     avl_tree.insert(AVLTree(15))
    #     avl_tree.insert(AVLTree(2))
    #     avl_tree.insert(AVLTree(7))
    #     self.assertEqual(1, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.left.left.balance_factor)
    #     self.assertEqual(0, avl_tree.left.right.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)

    # def test_insert_three_level_tree(self):
    #     """
    #     Test 26: Inserting a key results in a left imbalance and a right rotation

    #          10                10                5
    #        /    \            /    \             / \
    #       5      15    =>   5      15  =>      2   10
    #      / \               / \                /    / \
    #     2   7             2   7              1    7   15
    #                      /
    #                     1
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """
        
    #     one=AVLTree(1)
    #     two=AVLTree(2)
    #     five=AVLTree(5)
    #     seven=AVLTree(7)
    #     ten=AVLTree(10)
    #     fifteen=AVLTree(15)
    #     avl_tree = ten
    #     avl_tree = avl_tree.insert(five)
    #     avl_tree = avl_tree.insert(fifteen)
    #     avl_tree = avl_tree.insert(two)
    #     avl_tree = avl_tree.insert(seven)
    #     avl_tree = avl_tree.insert(one)

    #     self.assertEqual(five, avl_tree)
    #     self.assertEqual(two, avl_tree.left)
    #     self.assertEqual(one, avl_tree.left.left)
    #     self.assertEqual(ten, avl_tree.right)
    #     self.assertEqual(seven, avl_tree.right.left)
    #     self.assertEqual(fifteen, avl_tree.right.right)

    # def test_three_level_tree_height_right_heavy(self):
    #     """
    #     Test 27: Height of each node is one bigger than than max of its child's heights
    #          10                
    #         /  \            
    #        5    15    
    #             / \                 
    #            12  20               
                         
                        
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """
    #     avl_tree = AVLTree(10)
    #     avl_tree.insert(AVLTree(5))
    #     avl_tree.insert(AVLTree(15))
    #     avl_tree.insert(AVLTree(12))
    #     avl_tree.insert(AVLTree(20))
    #     self.assertEqual(2, avl_tree.height)
    #     self.assertEqual(0, avl_tree.left.height)
    #     self.assertEqual(1, avl_tree.right.height)
    #     self.assertEqual(0, avl_tree.right.left.height)
    #     self.assertEqual(0, avl_tree.right.right.height)

    # def test_three_level_tree_right_heavy_balance_factor(self):
    #     """
    #     Test 28: Balance factor of each node is the difference between its children's heights
    #         10                
    #         /  \            
    #        5    15    
    #             / \                 
    #            12  20              
                                          
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """
    #     avl_tree = AVLTree(10)
    #     avl_tree.insert(AVLTree(5))
    #     avl_tree.insert(AVLTree(15))
    #     avl_tree.insert(AVLTree(12))
    #     avl_tree.insert(AVLTree(20))
    #     self.assertEqual(-1, avl_tree.balance_factor)
    #     self.assertEqual(0, avl_tree.left.balance_factor)
    #     self.assertEqual(0, avl_tree.right.balance_factor)
    #     self.assertEqual(0, avl_tree.right.left.balance_factor)
    #     self.assertEqual(0, avl_tree.right.right.balance_factor)
       

    # def test_insert_three_level_tree_right_heavy(self):
    #     """
    #     Test 29: Inserting a key results in a left imbalance and a right rotation

    #          10                
    #         /  \            
    #        5    15    
    #             / \                 
    #            12  20  
        

    #          10                10                15
    #        /    \              / \               / \
    #       5      15    =>     5   15    =>      10   20
    #             / \               / \           / \    \
    #            12   20           12  20        5   12   25
    #                                   \
    #                                    25
    #     Hint: Recursion, if you didn't already, makes this easy.
    #     """

    #     five=AVLTree(5)
    #     ten=AVLTree(10)
    #     twelve=AVLTree(12)
    #     fifteen=AVLTree(15)
    #     twenty=AVLTree(20)
    #     twentyfive=AVLTree(25)
    #     avl_tree = ten
    #     avl_tree = avl_tree.insert(five)
    #     avl_tree = avl_tree.insert(fifteen)
    #     avl_tree = avl_tree.insert(twelve)
    #     avl_tree = avl_tree.insert(twenty)
    #     avl_tree = avl_tree.insert(twentyfive)

    #     self.assertEqual(fifteen, avl_tree)
    #     self.assertEqual(ten, avl_tree.left)
    #     self.assertEqual(five, avl_tree.left.left)
    #     self.assertEqual(twelve, avl_tree.left.right)
    #     self.assertEqual(twenty, avl_tree.right)
    #     self.assertEqual(twentyfive, avl_tree.right.right)


if __name__ == '__main__':
    unittest.main()
    
