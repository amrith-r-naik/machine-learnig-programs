import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def read_data(filename):
    df = pd.read_csv(filename)
    return df.drop(columns=['PlayTennis']), df['PlayTennis']

metadata, target = read_data("play_tennis_dataset.csv")

# Encode categorical variables using one-hot encoding
categorical_columns = metadata.select_dtypes(include=['object']).columns
preprocessor = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_columns)],
                                 remainder='passthrough')
metadata_encoded = preprocessor.fit_transform(metadata)

# Train the decision tree classifier
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(metadata_encoded, target)

# Print the decision tree
print(export_text(clf, feature_names=preprocessor.get_feature_names_out()))
