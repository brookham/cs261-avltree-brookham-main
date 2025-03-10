# AVL Tree: An AVL tree is a self-balancing tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_avl.py.

# IMPORTANT: For this implementation, starter code is provided.
# Do not modify the code provided 

# Name: Brook Hamilton
# Collaborators:
# Time spent:


class AVLTree:

    def __init__(self, key = None, height = 0, balance_factor = 0):
        self.left = None
        self.right = None
        self.key = key
        self.height = height
        self.balance_factor = balance_factor

    def insert(self, node_to_insert):
        if node_to_insert.key <= self.key:
            if not self._has_left_child():
                self.left = node_to_insert
            else:
                self.left.insert(node_to_insert)
        else:
            if not self._has_right_child():
                self.right = node_to_insert
            else:
                self.right.insert(node_to_insert)
        #You'll need to add code here
        self.height = self._max_of_child_heights() + 1
        self.balance_factor = self._rebalance()
        
        
        if self.balance_factor > 1:
            if self.left.balance_factor < 0:
                self.left = self.left._left_rotate()
            return self._right_rotate()
        if self.balance_factor < -1:
            if self.right.balance_factor > 0:
                self.right = self.right._right_rotate()
            return self._left_rotate()         
            
        return self
        
            
    # Here are some helper functions you may want to create
    # Right rotate around self
    def _right_rotate(self):
        new_root = self.left
        n2 = new_root.right

        new_root.right = self
        self.left = n2

        self.height = self._max_of_child_heights()
        new_root.height = new_root._max_of_child_heights() + 1

        self.balance_factor = self._rebalance()
        new_root.balance_factor = new_root._rebalance()
        
        return new_root


    # Left rotate around self
    def _left_rotate(self):
        new_root = self.right
        n2 = new_root.left

        new_root.left = self
        self.right = n2

        self.height = self._max_of_child_heights()
        self.balance_factor = self._rebalance()

        new_root.height = new_root._max_of_child_heights() + 1
        new_root.balance_factor = new_root._rebalance()
        
        return new_root
    
    # Return the largest height of self's children 
    def _max_of_child_heights(self):
        return max(self.left.height if self._has_left_child() else 0, self.right.height if self._has_right_child() else 0)
        
    # Return balance factor of self 
    def _rebalance(self):
        left_height = self.left.height if self._has_left_child() else -1
        right_height = self.right.height if self._has_right_child() else -1
        return left_height - right_height

   
    def search(self, key_to_find):
        if key_to_find == self.key:
            return self
        elif self._has_left_child() and key_to_find<=self.key:
            return self.left.search(key_to_find)
        elif self._has_right_child() and key_to_find>self.key:
           return self.right.search(key_to_find)
        else:
            return None
  
    def delete(self, key_to_delete):
        if key_to_delete < self.key:
            if self._has_left_child():
                self.left = self.left.delete(key_to_delete)       
        elif key_to_delete > self.key:
            if self._has_right_child():
                self.right = self.right.delete(key_to_delete)
        elif key_to_delete == self.key:
            if self._is_leaf():
                return None
            elif self._has_left_child() and not self._has_right_child():
                return self.left
            elif self._has_right_child() and not self.has_left_child():
                return self.right
            else:
                new_root = self.right.minimum()
                new_root.right = self.right.delete(new_root.key_to_delete)
                new_root.left = self.left
                return new_root
        return self
              

    def minimum(self):
        if self._has_left_child():
            return self.left.minimum()
        else:
            return self
    
    def _is_leaf(self):
        return not (self._has_left_child() or self._has_right_child())

    def _has_left_child(self):
        return not self.left is None

    def _has_right_child(self):
        return not self.right is None

    
           
