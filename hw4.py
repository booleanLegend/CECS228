#!/usr/bin/env python
# coding: utf-8

# # CECS 228: Coding Assignment #4
# 
# ### Submission Instructions:
# 
# Attach your coded solution to the programming tasks below. When you are finished...
# 
# 1. Rename this file so that your actual name replaces "YOUR NAME" in the current notebook name, and submit it to the dropbox by **Wednesday 12/16 @ 11:59 PM**. For example, I would submit to the dropbox a file called  `CECS 228 Coded Assignment #4 - KATHERINE VARELA.ipynb`
# 
# 2. Submit **your code only to CodePost as `hw4.py` by Wednesday 12/16 @ 11:59 PM**
# 
# 

# 
# Create a class named `RelationMatrix` that represents relation $R$ using an $m \times n$ matrix with bit entries.  E.g. 
# 
# $R = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 1 & 1 & 1\end{bmatrix}$
# 
# Your class must satisfy the following requirements:
# 
# **Instance attributes**
# 1. `self.rows` - a list of lists representing a list of the rows of this matrix
# 
# **Constructor**
# 1.  `__init__(self, rows)`  :  initializes this matrix with the given list of rows.
# 
# **Getter methods**
# 1. `getEntry(i, j)`  :  returns the $ij$-th entry of this matrix.  Raises an `IndexError` if $i < 1$,  $i > m$, $j < 1$ or $j > n$
# 2. `getRow(i)`  :  returns the $i$-th row of this matrix.  Raises an `IndexError` if $i < 1$ or $i > m$
# 3. `getCol(j)`  :  returns the $j$-th column of this matrix.  Raises an `IndexError` if $j < 1$ or $j > n$
# 4. `getDiag(k)`  :  returns the $k$-th diagonal of the matrix as a list, where 
#     * $k = 0$  :  returns the main diagonal beginning with element $a_{11}$
#     * $k = 1$  :  returns the diagonal beginning with element $a_{12}$
#     * $k = 2$  :  returns the diagonal beginning with element $a_{13}$
#     * ...
#     * $k = n-1$  :  returns the diagonal containing the single element $a_{1n}$
#     * $k = -1$  :  returns the diagonal beginning with element $a_{21}$
#     * $k = -2$  :  returns the diagonal beginning with element $a_{31}$
#     * ...
#     * $k = -(m-1)$  :  returns the diagonal containing the single element $a_{m1}$
#     Raises `IndexError` if $k > n-1 $ or $k < 1-m$
# 5. `isReflexive()`  :  returns `True` if the relation represented by this matrix is reflexive, `False` otherwise.
# 6. `isSymmetric()`  :  returns `True` if the relation represented by this matrix is symmetric, `False` otherwise.
# 7. `isAntisymm()`  : returns `True` if the relation represented by this matrix is antisymmetric, `False` otherwise.
# 8. `isAsymmetric()`  :  returns `True` if the relation represented by this matrix is asymmetric, `False` otherwise.
# 9. `isTransitive()`  :  returns `True` if the relation represented by this matrix is transitive, `False` otherwise.
# 10.  `isEqRelation()`  :  returns `True` if the relation represented by this matrix is an equivalence relation, `False` otherwise.
# 
#     
# **Setter methods**
# 1. `setEntry(i, j, b)`  :  sets the $ij$-th entry to bit $b$.  Raises `ValueError` if $b \neq 0$ and $b \neq 1$.
# 2. `deleteRow(i)`  :  deletes the $i$-th row of this matrix. Raises `IndexError` if $i < 1$ or $i > m$.
# 3. `deleteCol(j)`  :  deletes the $j$-th column of this matrix.  Raises `IndexError` if $j < 1$ or $j > n$.
# 
# 

# In[1]:


class RelationMatrix:
    
    def __init__(self, rows):
        self.rows = rows
    
    def getEntry(self, i, j):
        if i < 1 or j < 1 or i > len(self.rows[1]) or j > len(self.rows[1]):
            raise IndexError("Not within range.")
        return self.rows[i - 1][j - 1]
    
    def getRow(self, i):
        if i < 1 or i > len(self.rows):
            raise IndexError("Not within range.")
        return self.rows[i - 1]
    
    def getCol(self, j):
        if j < 1 or j > len(self.rows[1]):
            raise IndexError("Not within range.")
        return [i[j - 1] for i in self.rows]
    
    def getDiag(self, k):
        diag = []
        row = 0
        col = 0

        if k > 0:
            col = k
        elif k < 0:
            row = -k

        for index in range(abs(k), len(self.rows)):
            diag.append(self.rows[row][col])
            row += 1
            col += 1

        if len(diag) > 0:
            return diag
        raise IndexError()
    
    def isReflexive(self):
        if self.rows[0][0] == 0:
            return False
        else:
            i = self.rows[0][0]
            j = 1
            while j < len(self.rows) - 1:
                if self.rows[j][j] != i:
                    return False
                else:
                    j += 1
            return True            
    
    def isSymmetric(self):
        for i in range(len(self.rows[1]) - 1):
            for j in range(len(self.rows[1]) - 1):
                if self.rows[i][j] != self.rows[j][i]:
                    return False
        return True
    
    def isAsymmetric(self):
        for i in range(len(self.rows) - 1):
            for j in range(len(self.rows) - 1):
                if self.rows[i][j] == 1 and self.rows[i][j] == self.rows[j][i]:
                    return False
        return True
    
    def isTransitive(self):
        for i in range(len(self.rows) - 1):
            for j in range(len(self.rows) - 1):
                if self.rows[i][j] == 1:
                    if not self.rows[j][i] == 1 or not self.rows[i][i] == 1:
                        return False
        return True      
    
    def isEqRelation(self):
        return self.isSymmetric() and self.isReflexive() and self.isTransitive()
    
    def setEntry(self, i, j, b):
        if b != 0 and b != 1:
            raise ValueError(f"{b} must be 0 or 1.")
        self.rows[i - 1][j - 1] = b
    
    def deleteRow(self, i):
        if i < 1 or i > len(self.rows):
            raise IndexError("Not within range.")
        self.rows.pop(i - 1)

    def deleteCol(self, j):
        for i in range(self.rows):
            self.rows.pop(self.rows[j - 1][i])        


# In[ ]:




