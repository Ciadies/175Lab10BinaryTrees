class BinaryTree:
    def __init__(self, rootElement):
        self.key = rootElement
        self.left = None
        self.right = None
        
    '''getters'''
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getKey(self):
        return self.key
    
    '''setters'''
    def setKey(self,key):
        self.key=key
        
    def setLeft(self,left):
        self.left=left        
  
    def setRight(self,right):
        self.right=right
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
  
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t 
            
    def _strHelper(self):
        """Returns list of strings,  total width of the tree, position of the middle node and the height"""
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.key
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper() 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
    
    
    def __str__(self):
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result
    


################################################################################
##  EXERCISE 1
################################################################################    

def preorder(tree):
    '''
    print the value of a tree in a Preorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    if tree != None:
        print(tree.getKey()) #processes root
        preorder(tree.getLeft()) #processes left subtree
        preorder(tree.getRight()) #processes right subtree
        
def inorder(tree):
    '''
    print the value of a tree in an Inorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    if tree != None:
        inorder(tree.getLeft()) #processes left subtree
        print(tree.getKey()) #processes root
        inorder(tree.getRight()) #processes right subtree

def postorder(tree):
    '''
    print the value of a tree in a Postorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''       
    if tree != None:
        postorder(tree.getLeft()) #processes left subtree
        postorder(tree.getRight()) #processes right subtree
        print(tree.getKey()) #processes root
        
################################################################################
##  EXERCISE 2
################################################################################ 

def findMinKey(tree):
    '''
    find the minimum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    if tree != None:
        small = tree.getKey()
        if tree.getLeft() != None:
            small = min(small,findMinKey(tree.getLeft()))
        if tree.getRight() != None:
            small = min(small,findMinKey(tree.getRight()))
    
        return small
    return None

def findMaxKey(tree):
    '''
    find the maximum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    if tree != None:
        big = tree.getKey()
        if tree.getLeft() != None:
            big = max(big,findMaxKey(tree.getLeft()))
        if tree.getRight() != None:
            big = max(big,findMaxKey(tree.getRight()))
        return big
    
    return None

################################################################################
##  EXERCISE 3
################################################################################ 

def buildTree(inOrder, preOrder): 
    '''
    Build a binary tree based on given Inorder and PreOrder traversals
    
    Parameters:
        - inOrder, preOrder (list of numbers)
    eg.
    inOrder 4,3,5,2,6,1,8,7,9
    preOrder 1,2,3,4,5,6,7,8,9
                            1
    inOrder     4,3,5,2,6        8,7,9
    preOrder    2,3,4,5,6        7,8,9
                       2           7
    inOrder     4,3,5    6       8   9
    preOrder    3,4,5    6       8   9
                  3
    inOrder     4   5    
    preOrder    4   5    
    
                    ____1____
                 __2__     __7__
              __3__   6   8     9
             4     5
    Returns: a BinaryTree object
    '''  
    
    #TODO delete pass and write your code
    #base case:
    if len(preOrder) == 0:
        return None
    
    #get the root value
    rootVal = preOrder[0]
    
    #find the index of root value in Inorder traversal
    idx = inOrder.index(rootVal)

    #build the tree recursively
    tree = BinaryTree(rootVal)
    tree.setLeft(buildTree(inOrder[:idx],preOrder[1:idx+1]))
    
    tree.setRight(buildTree(inOrder[idx+1:],preOrder[idx+1:]))
    
    return tree
    
################################################################################
##  Test your functions: you are encouraged to add other tests as well
################################################################################ 
def main():
    tree = BinaryTree(1)
    tree.insertLeft(2)
    tree.insertRight(7)
    tree.getLeft().insertLeft(3)
    tree.getLeft().insertRight(6)
    tree.getLeft().getLeft().insertLeft(4)
    tree.getLeft().getLeft().insertRight(5)
    tree.getRight().insertLeft(8)
    tree.getRight().insertRight(9)

    print("the tree:\n")
    print(tree)
    
    print("preorder traversal:")
    preorder(tree)
    print()
    print("inorder traversal:")
    inorder(tree)
    print()
    print("postorder traversal:")
    postorder(tree)
    print()

    print('Max value in tree:', findMaxKey(tree))
    print('Min value in tree:', findMinKey(tree))

    inor = [4,3,5,2,6,1,8,7,9]
    preor = [1,2,3,4,5,6,7,8,9]

    theTree = buildTree(inor,preor)
    
    print(theTree)
    
    inor2 = [3,2,4,1,5]
    preor2 = [1,2,3,4,5]

    theTree2 = buildTree(inor2,preor2)
    
    print(theTree2)  
    
    
if __name__ == "__main__":
    main()        