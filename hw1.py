#!/usr/bin/env python
# coding: utf-8

# # CECS 228: Coding Assignment #1
# 
# ### Submission Instructions:
# 
# Attach your coded solution to the programming tasks below. When you are finished...
# 
# 1. Rename this file so that your actual name replaces "YOUR NAME" in the current notebook name, and submit it to the dropbox by **Sunday 9/20 @ 11 AM**. For example, I would submit to the dropbox a file called  `CECS 229 Coded Assignment #1 - KATHERINE VARELA.ipynb`
# 2. Submit **your code only to CodePost as `hw1.py` by Sunday 9/20 @ 11:59 PM**
# 
# 

# ## Problem 1:
# 
# Create the following three functions: 
# 
# 1. `propOR(p_truthval, q_truthval)` - returns the truth value of $p \lor q$
#     
#    INPUT: 
#     * `p_truthval` - a boolean (i.e. True or False) describing the truth value of p
#     * `q_truthval` - a boolean (i.e. True or False) describing the truth value of q
#    
#    OUTPUT:
#     * boolean `True` or `False` 
#    
# 2. `propXOR(p_truthval, q_truthval)` - returns the truth value of $p \oplus q$
#     
#    INPUT: 
#     * `p_truthval` - a boolean (i.e. True or False) describing the truth value of p
#     * `q_truthval` - a boolean (i.e. True or False) describing the truth value of q
#     
#    OUTPUT:
#     * boolean `True` or `False`
#     
# 3. `propAND(p_truthval, q_truthval)` - returns the truth value of $p \land q$
#     
#    INPUT: 
#     * `p_truthval` - a boolean (i.e. True or False) describing the truth value of p
#     * `q_truthval` - a boolean (i.e. True or False) describing the truth value of q
#     
#    OUTPUT:
#     * boolean `True` or `False`
#     
#     
# 
#  
# **Sample Output** 
# 
# `>> propOR(True, False)`
# 
# `True`
# 
# `>> propXOR(True, False)`
# 
# `True`
# 
# `>> propAND(True, False)`
# 
# `False`
# 

# In[1]:


def propOR(p_truthval, q_truthval):
    return p_truthval or q_truthval


# In[2]:


propOR(True, False)


# In[3]:


def propXOR(p_truthval, q_truthval):
    return p_truthval ^ q_truthval


# In[4]:


propXOR(True, False)


# In[5]:


def propAND(p_truthval, q_truthval):
    return p_truthval and q_truthval


# In[6]:


propAND(True, False)


# ## Problem 2:
# 
# **Background**
# 
# A bit is a symbol that can only attain one of two values: 0 or 1.  Bits are often used in logic in the place of the usual truth values, where 1 is used for TRUE and 0 for false.  In such a case, 
# 
# | $p$ 	| $q$ 	| $p \lor q$ 	| $p \land q$ 	| $p \oplus q$ 	|
# |:---:	|:---:	|:----------:	|:-----------:	|------------:	|
# |  1  	|  1  	|      1     	|      1      	|       0      	|
# |  1  	|  0  	|      1     	|      0      	|       1      	|
# |  0  	|  1  	|      1     	|      0      	|       1      	|
# |  0  	|  0  	|      0     	|      0      	|       0      	|
# 
# 
# Information is often represented using bitstrings, which are strings consisting of 0's and 1's.  We make the following definitions for two bitstrings of the same length:  Consider the bit strings $P = p_{n-1} \cdots p_1 p_0$ and $Q = q_{n-1} \cdots q_1 q_0$, where $p_i$ and $q_i$ for $i = 0, 1, \dots n-1$ are bits.  Then,  and Q = 
# 
# 
# 
# 
# 
# |                Operation        | Rule                  ||E.g.  $P$   	    |  E.g. $Q$ 	| Result |
# |---	                          |---	                  |---|---	            |---	        |---               | 
# | <font color = blue> bitwise OR  | apply $p_i \lor q_i$  | for $i = 0$ to $ n-1$ |01010111	    | 00111000      |  01111111 	   | 
# | <font color = green> bitwise XOR  | apply $p_i \oplus q_i$  | for $i = 0$ to $ n-1$ |01010111	    | 00111000      |  01101111 	   | 
# | <font color = red>  bitwise AND | apply $p_i \land q_i$ |for $i = 0 $ to $ n-1$| 01010111	    | 00111000      |  00010000	       | 
# 
# 
# 
# **Directions**
# 
# Create three functions that compute bitwise operations on two bitstrings `P` and `Q`.  If the string lengths are not the same, then pad the shorter string with enough 0's at the beginning of the string so that `P` and `Q` have the same length. 
# 
# E.g. If `P = "1110"` and `Q = "11 0101", then pad `P` with two 0's so that `P = "00 1110"'.  Make sure to strip off any whitespaces the string may contain prior to attempting to apply the bitwise operation:
# 
# 1. `bitwiseOR(P, Q)` returns a bitstring that is the result of applying bitwise OR on bitstrings `P` and `Q`
#     * INPUT: `P, Q` - Python strings consisting of characters 0 and 1
#     * OUTPUT: a Python string consisting of characters 0 and 1
# 
# 2. `bitwiseXOR(P, Q)` returns a bitstring that is the result of applying bitwise XOR on bitstrings `P` and `Q`
#     * INPUT: `P, Q` - Python strings consisting of characters 0 and 1
#     * OUTPUT: a Python string consisting of characters 0 and 1
#     
# 3. `bitwiseAND(P, Q)` returns a bitstring that is the result of applying bitwise AND on bitstrings `P` and `Q`
#     * INPUT: `P, Q` - Python strings consisting of characters 0 and 1
#     * OUTPUT: a Python string consisting of characters 0 and 1
# 
# 
# **Sample Output:**  
#  
# `>> bitwiseOR("0101 0111", "11 1000 ")` 
# 
# `01111111`
# 
# `>> bitwiseXOR("0101 0111", "11 1000 ")` 
# 
# `01101111`
# 
# `>> bitwiseAND("0101 0111", "11 1000 ")` 
# 
# `00010000`
# 
# 
# 
# 

# In[7]:


def bitwiseOR(P, Q):
    newP = P.replace(" ", "")
    newQ = Q.replace(" ", "")
    newBitString = ""

    if len(newP) < len(newQ):
        for i in range(len(newQ)-len(newP)):
            newP = "0" + newP
    elif len(newP) > len(newQ):
        for i in range(len(newP) -len(newQ)):
            newQ = "0" + newQ
    else:
        pass

    for i in range(len(newP)):
        if (newP[i] == "1") or (newQ[i] == "1"):
            newBitString = newBitString + "1"
        else:
            newBitString = newBitString + "0"
    return newBitString


# In[8]:


bitwiseOR("0101 0111", "11 1000 ")


# In[9]:


def bitwiseXOR(P, Q):
    newP = P.replace(" ", "")
    newQ = Q.replace(" ", "")
    newBitString = ""

    if len(newP) < len(newQ):
        for i in range(len(newQ)-len(newP)):
            newP = "0" + newP
    elif len(newP) > len(newQ):
        for i in range(len(newP) -len(newQ)):
            newQ = "0" + newQ
    else:
        pass

    for i in range(len(newP)):
        if bool(newP[i] == "1") != bool(newQ[i] == "1"):
            newBitString = newBitString + "1"
        else:
            newBitString = newBitString + "0"
    return newBitString


# In[10]:


bitwiseXOR("0101 0111", "11 1000 ")


# In[11]:


def bitwiseAND(P, Q):
    newP = P.replace(" ", "")
    newQ = Q.replace(" ", "")
    newBitString = ""

    if len(newP) < len(newQ):
        for i in range(len(newQ)-len(newP)):
            newP = "0" + newP
    elif len(newP) > len(newQ):
        for i in range(len(newP) -len(newQ)):
            newQ = "0" + newQ
    else:
        pass

    for i in range(len(newP)):
        if (newP[i] == "1") and (newQ[i] == "1"):
            newBitString = newBitString + "1"
        else:
            newBitString = newBitString + "0"
    return newBitString


# In[12]:


bitwiseAND("0101 0111", "11 1000 ")


# ## Problem 3:
# 
# 
# **Background**
# 
# A compound proposition is ***satisfiable*** if there is an assignment of the truth values to its variables that makes it true.  
# 
# For example, 
# * $(p \lor q \lor r) \land (\neg p \lor \neg q \lor \neg r)$ is satisfiable because the compound proposition is true if at least one variable is true and one is false (e.g. if $p$ is true and $q$ is false).  
# 
# * $(p \lor \neg q) \land (q \lor \neg r) \land (r \lor \neg p) \land (p \lor q \lor r) \land (\neg p \lor \neg q \lor \neg r)$ is ***unsatisfiable*** because it is false for every combination of truth values for $p, q$, and $r$ (i.e. it is a fallacy).
# 
# 
# **Directions**
# 
# Create a function `isSatisfiable(P)` that returns `True` if the compound proposition is satisfiable or `False` otherwise.  The compound proposition `P` will be given as a list of the following possible characters 
# 
# * `(` or `)` - parentheses used for grouping
# * `v` - propositional OR (lowercase v)
# * `@` - propositional XOR
# * `^` - propositional AND
# * `~` - negation
# * `p`, `q`, `r`, `s` - propositional variables 
# 
# No other characters will be recognized beyond this.  For example,  $(p \lor q \lor r) \land (\neg p \lor \neg q \lor \neg r)$ would be given as the list 
# 
# `['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ]`
# 
#  INPUT: 
#     * `P` - a list of characters defined above.
# 
#  OUTPUT: True if `P` is satisfiable, `False` otherwise.
# 
# **Sample Output**:  
#  
# `>> isSatisfiable(['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ])` 
# 
# `True`

# In[15]:


def _get_groups(P):
    groups_idx = []
    
    temp_stack = []
    for i in range(len(P)):
        
        if P[i] == "(":
            temp_stack.append(i)

        if P[i] == ")":
            group = (temp_stack[-1], i)
            groups_idx.append(group)
            del temp_stack[-1]
            
    groups = []
    for (start, end) in groups_idx:
        group = P[start:end+1]
        groups.append(group)
    return groups   

def getMiddleOperator(P):
    for i in range(len(P)):
        if P[i] == ')':
            break
    return P[i+1]

def andfunc(p, q):
    return p and q

def orfunc(p, q):
    return p or q

def xorfunc(p, q):
    return p ^ q

# returns logic of strings of groups as boolean array
def eval_logic(string):
    booleanExpression = []
    for i, element in enumerate(string):
        if i == '^':
            booleanExpression.append(andfunc(string[i-1], string[i+1]))
        elif i == 'v':
            booleanExpression.append(orfunc(string[i-1], string[i+1]))
        elif i == '@':
            booleanExpression.append(xorfunc(string[i-1], string[i+1]))
        elif i == '~':
            booleanExpression.append(not(string[i+1]))
        else:
            next
    return booleanExpression
def isSatisfiable(P):
    answer = True
    groups_Q = _get_groups(P)
    logicalExpression = []
    for group in groups_Q:
        logicalExpression += (eval_logic(group))

    for booleans in logicalExpression:
        if logicalExpression[booleans]:
            answer = True
        elif not logicalExpression[booleans]:
            answer = False
        else:
            checkBools = len(group)
            for group in groups_Q:
                if groups_Q[group] == 'v':
                    next
                else:
                    --checkBools
            leftBool = logicalExpression[checkBools -1] 
            rightBool = logicalExpression[checkBools + 1]
            operator = getMiddleOperator(P)
            if operator == '^':
                answer = not (leftBool and rightBool)
            elif operator == 'v':
                answer = not (leftBool or rightBool)
            elif operator == '@':
                answer = not (leftBool ^ rightBool)

    return answer


# In[16]:


isSatisfiable(['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ])


# In[ ]:




