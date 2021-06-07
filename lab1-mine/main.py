def _get_groups(P):
    """
    returns the groups found in logical expression list P
    The groups are returned in a list, and each found group is itself a list.
    P can also be a string (but spaces must be removed), in which case each group will be a string.
    """
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

print("=======================SAMPLE USAGE 1====================\n")
list_Q = ['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ]
print("Original: ", list_Q)
groups_Q = _get_groups(list_Q) #function call
print("Function returns: ", groups_Q)

print("\nBy element:")
for group in groups_Q:
    print(group, "\t\t=====>", " ".join(group)) #converting each group list into a string for easy reading

def isSatisfiable(P):
	answer = True
	groups_Q = _get_groups(list_Q)
	logicalExpression = []
	for group in groups_Q:
		logicalExpression += (eval_logic(group))
		
	
	for booleans in logicalExpression:
		if logicalExpression[booleans]:
			answer = True
			print("1")
		elif not logicalExpression[booleans]:
			answer = False
			print("2")
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
			else:
				print("Not compatible")
			print("3")

	return answer


print("=======================SAMPLE USAGE 1====================\n")
list_Q = ['(', 'p', 'v', 'q', 'v' , 'r', ')',  '^', '(', '~', 'p', 'v', '~', 'q', 'v', '~', 'r', ')' ]
print("Original: ", list_Q)
groups_Q = _get_groups(list_Q) #function call
print("Function returns: ", groups_Q)

print("\nBy element:")
for group in groups_Q:
	print(group, "\t\t=====>"," ".join(group)) #converting each group list into a string for easy reading
print("\n\n\n=======================SAMPLE USAGE 2====================\n")
expression_P = "~ (p V (q ^ r)) @ ~ (p ^ r)"
print("Original:", expression_P)

string_groups_P = _get_groups(expression_P)
print("Function returns: ", string_groups_P)

print("\nBy element:")
for group in string_groups_P:
	print(group) #converting each group list into a string for easy readin

print("\n\n\n=======================SAMPLE USAGE 3====================\n")
list_P = [char for char in expression_P.replace(" ", "")]
print("\n\nOriginal: ", list_P)

list_groups_P = _get_groups(list_P)
print("\nFunction returns: ", list_groups_P)

print("\nBy element:")
for group in list_groups_P:
	print(group, "\t\t=====>"," ".join(group)) #converting each group list into a string for easy reading



print(isSatisfiable(list_Q))
print(isSatisfiable(expression_P))
print(isSatisfiable(list_P))