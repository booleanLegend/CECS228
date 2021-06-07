#!/usr/bin/env python
# coding: utf-8

# # CECS 228: Coding Assignment #2
# 
# ### Submission Instructions:
# 
# Attach your coded solution to the programming tasks below. When you are finished...
# 
# 1. Rename this file so that your actual name replaces "YOUR NAME" in the current notebook name, and submit it to the dropbox by **Sunday 10/18 @ 11:59 PM**. For example, I would submit to the dropbox a file called  `CECS 228 Coded Assignment #2 - KATHERINE VARELA.ipynb`
# 
# 2. Submit **your code only to CodePost as `hw2.py` by Sunday 10/18 @ 11:59 PM**
# 
# 

# ## Problem 1:
# 
# Implement the triangle class as described in the recursion slides presented during Week 6 Lab Session 2.  Remember that the method returning the area must be implemented recursively.  Write a conditional statement in the constructor that raises an error in order to avoid an infinite recursion.
# 
# 

# In[1]:


class Triangle:
    
    def __init__(self, width):
        """
        constructor initializes a Triangle object with the given width
        INPUT: width - the width as a positive integer
        """
        if width <= 0:
            raise ValueError("Width too small.")
        self.width = width
        
    def get_area(self):
        """
        gets the area of this triangle
        OUTPUT: the area as an int
        """
        if self.width == 1: return 1
        else:
            smallerTriangle = Triangle(self.width - 1)
            smallerArea = smallerTriangle.get_area()
            return smallerArea + self.width
    
    def get_width(self):
        """gets the width of this triangle
        OUTPUT: the width as an int
        """
        return self.width
        
    def __str__(self):
        triangle_str = ""
        for i in range(1, self.width+1):
            triangle_str += i*"[] " + "\n"
                
        return triangle_str
    


# ## Problem 2:
# 
# Write a recursive function named `linear_search` that searches a list to find a given element.  If the element is in the list, the function returns the index of the first instance of the element, otherwise it returns -1000.
#     
#     
# 
#  
# **Sample Output** 
# 
# `>> linear_search(72, [10, 32, 83, 2, 72, 100, 32])`
# 
# `4`
# 
# `>> linear_search(32, [10, 32, 83, 2, 72, 100, 32])`
# 
# `1`
# 
# `>> linear_search(0, [10, 32, 83, 2, 72, 100, 32])`
# 
# `-1000`
# 
# `>> linear_search('a', ['c', 'a', 'l', 'i', 'f', 'o', 'r', 'n', 'i', 'a'])`
# 
# `1`
# 

# In[13]:


def linear_search(ele, array):
    """searches the given list for the given element
    INPUT:  
        * ele - the element
        * array - the list
    OUTPUT: the index of the first instance of the element in the list, or -1000 if it is not in the list.
    """
    index = 0
    if not array:
        return -1000
    if index <= len(array) - 1:
        if array[index] == ele:
            return index
        else:
            test = linear_search(ele, array[1:])
            if test == -1000:
                return test
            else:
                return test + 1
    else:
        return -1000


# In[14]:


linear_search(72, [10, 32, 83, 2, 72, 100, 32])


# In[15]:


linear_search(32, [10, 32, 83, 2, 72, 100, 32])


# In[16]:


linear_search(0, [10, 32, 83, 2, 72, 100, 32])


# In[17]:


linear_search('a', ['c', 'a', 'l', 'i', 'f', 'o', 'r', 'n', 'i', 'a'])


# ## Problem 3:
# 
# 
# 
# **Part I**
# 
# Write a recursive function named `merge_sort` that sorts a given list using the recursive algorithm of merge sort.  Implement and use the helper function `_merge`, which merges two sorted arrays.
#     
#     
# 
#  
# **Sample Output** 
# 
# `>> merge_sort([10, 32, 83, 2, 72, 100, 32])`
# 
# `[2, 10, 32, 32, 72, 83, 100]`
# 
# `>> merge_sort(['a','g','a','t','e'])`
# 
# `['a','a','g','e', 't']`

# In[7]:


def _merge(P, Q):
    """merges two sorted arrays
    INPUT:  
        * P, Q - the two sorted arrays
    OUTPUT: a sorted list consisting of elements in P and Q
    """
    i = j = 0
    result = []
    while i < len(P) or j < len(Q):
        if i >= len(P):
            result.append(Q[j])
            j += 1
        elif j >= len(Q):
            result.append(P[i])
            i += 1
        elif P[i] < Q[j]:
            result.append(P[i])
            i += 1
        else:
            result.append(Q[j])
            j += 1
    return result


# In[8]:


def merge_sort(array):
    """sorts a given list
    INPUT:  
        * array - the list
    OUTPUT: a sorted copy of the list.
    """
    if len(array) == 0:
        return array
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return _merge(left, right)


# In[9]:


merge_sort([10, 32, 83, 2, 72, 100, 32])


# **Part II**
# 
# Use a proof by induction to show that the function `merge_sort` will correctly sort any array of size $n$.
# 
# **Proof**
# 
# Type your answer here.  Use \$ \$ to type LaTeX math expressions, e.g. $p \land q$
# 
# 
# __Base case:__ Suppose that \$ n = 0\$, and also suppose that \$ n = 1\$.
# If n = 0, then in the first if branch, we return the empty array sorted. If n = 1, then in the second if branch, we return the only element in the array sorted.
# 
# __Inductive Hypothesis:__ merge_sort correctly sorts all lists with k elements, for any \$0 <= k < n\$.
# 
# __Inductive Step:__ Suppose \$n > 1\$. Since \$n > 1\$, we skip over the if branches and we return _merge(left, right)_, where _left_ and _right_ each have no more than \$(n / 2) + 1\$ elements and which togeher contain all the elements. By the indution hypothesis, each of merge_sort(left) and merge_sort(right) are sorted and by the correctness of _merge_, the returned list is a sorted list containing all the elements.
# 
# __Conclusion:__ By induction, the Inductive Hypothesis holds for a list of size \$n\$.
