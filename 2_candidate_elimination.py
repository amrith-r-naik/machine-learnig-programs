import pandas as pd
import numpy as np

data = pd.DataFrame(pd.read_csv('enjoy_sport.csv'))
print("Dataset :\n", data)

concepts = np.array(data.iloc[:,0:-1])
print("\nConcepts :\n", concepts)

target = np.array(data.iloc[:,-1])
print("\nTarget :\n", target)

def learn(concepts,target):
	''' learn() function implements the learning method of the candidate elimination algoithm.
	Arguments:
		concepts - a datat frame with all the features
		target - a data frame with corresponding output values
	'''
	specific_h = concepts[0].copy()
	general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]
	print("\nInitialization of specific_h and general_h :")
	print(specific_h)
	print(general_h)
	
	for i,h in enumerate(concepts):
		if  target[i] == 'Yes':
			for x in range(len(specific_h)):
				if h[x] != specific_h[x]:
					specific_h[x] = '?'
					general_h[x][x] = '?'
		if target[i] == 'No':
			for x in range(len(specific_h)):
				if h[x] != specific_h[x]:
					general_h[x][x] = specific_h[x]
				else:
					general_h[x][x] = '?'
		print("\nStep of Candidate Elimination Algorithm",i+1)
		print(specific_h)
		print(general_h)
	indices = [i for i, val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
	for i in indices:
		general_h.remove(['?','?','?','?','?','?'])
	return specific_h, general_h
s_final, g_final = learn(concepts, target)
print("\nFinal specific_h : ", s_final, sep="\n")
print("\nFinal general_h : ", g_final, sep="\n")
	
