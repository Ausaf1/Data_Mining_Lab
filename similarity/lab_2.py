import numpy as np
import pandas as pd
data = pd.read_csv(r'D:\data_mining_lab\similarity\\animal.txt')
attributes = data.iloc[:, 1:].values


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


num_observations = attributes.shape[0]
similarity_matrix = np.zeros((num_observations, num_observations))
for i in range(num_observations):
    for j in range(num_observations):
        if i != j:
            similarity_matrix[i, j] = cosine_similarity(
                attributes[i], attributes[j])

top_pairs = []
for i in range(num_observations):
    for j in range(i + 1, num_observations):
        top_pairs.append((i, j, similarity_matrix[i, j]))

top_pairs.sort(key=lambda x: x[2], reverse=True)
top_pairs = top_pairs[:10]

# Print the top 10 similar pairs along with their similarity scores
for idx1, idx2, similarity in top_pairs:
    observation1 = data.iloc[idx1, 0]
    observation2 = data.iloc[idx2, 0]
    print(f"Pair: {observation1} - {observation2}, Similarity: {similarity:.4f}")


