
# Decision Tree Program

# 1. Load the dataset
import pandas as pd
data = pd.read_csv('play_tennis_dataset.csv')

# 2. Separate features and target variable
features = data.drop('PlayTennis', axis=1)  # Features
target_column = data['PlayTennis']  # Target variable

# 3. Convert textual data into numerical data
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in features.columns:
    features[col] = encoder.fit_transform(features[col])
target_column = encoder.fit_transform(target_column)

# 4. Create and train the decision tree model
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(features,target_column)

# 5. Visualize the tree
from sklearn.tree import export_text
visualization = export_text(clf,feature_names=list(features),class_names=['No','Yes'])
print(visualization)

# 6. Predicting own values, if in case maam asks
print(clf.predict(features))