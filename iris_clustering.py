import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("datasets/Iris_modified.csv")
df.drop('Species', inplace=True, axis=1)

# Selecting features for clustering
features = ['SepalLengthCm', 'SepalWidthCm']
X = df[features]

# Standardize the features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)

# Apply EM algorithm
em_model = GaussianMixture(n_components=3, random_state=42)
em_clusters = em_model.fit_predict(scaled_data)

# Apply k-means algorithm
kmeans_model = KMeans(n_clusters=3, random_state=42)
kmeans_clusters = kmeans_model.fit_predict(scaled_data)

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=em_clusters, cmap='viridis')
plt.title('EM Clustering')
plt.xlabel('Sepal Length (Cm)')
plt.ylabel('Sepal Width (Cm)')

plt.subplot(1, 2, 2)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=kmeans_clusters,cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('Sepal Length (Cm)')
plt.ylabel('Sepal Width (Cm)')

plt.tight_layout()
plt.show()