import os
import re
def cleanText(inputData):
	inputString = re.sub(r'[^\w\s]',"",inputData).strip().lower()
	if re.match(r'^(hello|hi|hey)$',inputString):
		return [False,"Hello. Please enter something useful!"]
	elif re.match(r'^(how\s+are\s+you(\s+doing)?|hows\s+it\s+going|hows\s+everything|how\s+are\s+things|hows\s+life)$',inputString):
		return [False,"Good. Please enter something useful!"]
	elif re.match(r'^(whats\s+up|whats\s+new|whats\s+going\s+on|s+up|whaz+up)$',inputString):
		return [False,"Nothing. Please enter something useful!"]
	elif re.match(r'^good\s+(morning|afternoon|evening|night)$',inputString):
		return [False,re.findall(r'^(good\s+(morning|afternoon|evening|night))$',inputString)[0][0].upper()+"! Please enter something useful!"]
	elif len(inputString.split())<8:
		return [False,"Please make sure the text contains at least 8 characters"]
	else:
		return [True,inputData]

if __name__ == "__main__":
	returnData = cleanText("Good night!!")
	print(returnData)