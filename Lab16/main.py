"""
## Task
"""


def order(words):
	"""
    orders the words in the given set in alphabetical order
    INPUT: words - set of strings
    OUTPUT: list of strings
    """
	wordSet = list(words)
	asciiVals = []
	ans = []
    
	for i in range(len(wordSet)):
		wordSet[i] = wordSet[i].lower()
	for word in wordSet:
		for ch in word: 
			asciiVals = [tuple(ord(ch) for ch in word) for word in wordSet]
	while asciiVals:
		minn = asciiVals[0]
		for i in asciiVals:
			if i < minn:
				minn = i
		ans.append(minn)
		asciiVals.remove(minn)
	lastArray = []
	for i in ans:
		charString = ""
		for k in i:
			charString += chr(k)
		lastArray.append(charString)
	return lastArray
words = {"All","Baby", "Allen", "Babe"}
print(order(words))