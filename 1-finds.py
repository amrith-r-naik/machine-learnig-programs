import pandas as pd

# Load Data
data = pd.read_csv('enjoy_sport.csv')

# Initialize the hypothesis
hypothesis = ['%' for _ in range(len(data.columns)-1)]

# Filter positive examples(where EnjoySport is 'Yes')
positive_examples = data[data['EnjoySport'] == 'Yes'].iloc[:,:-1].values.tolist()

# Apply FIND-S algorithm
for example in positive_examples:
	for i in range(len(example)):
		if hypothesis[i] != '%' and hypothesis[i] != example[i]:
			hypothesis[i] = '?'
		else:
			hypothesis[i] = example[i]

# Print the maximally specific hypothesis
print("The maximally specific Find-s hypothesis for the given training examples is :")
print(hypothesis)
