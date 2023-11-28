# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from qna import questions, answers


# New question
new_question = input("Enter your question: ")

# Combine all text for vectorization
corpus = questions + answers + [new_question]

# BOW vectors
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)

# # Calculate cosine similarities
# cosine_similarities = cosine_similarity(X)


# # index of the closest answer to the new question
# new_question_index = len(corpus) - 1  # Index of the new question
# most_similar_answer_index = cosine_similarities[new_question_index].argsort()[-2]  # Index of the second highest similarity (excluding the question itself)

# # most similar answer
# most_similar_answer = answers[most_similar_answer_index]

# print("Question:", new_question)
# print("Answer:", most_similar_answer)

bow = {}
for sentence in corpus:
    for word in sentence.split():
        if word not in bow:
            bow[word] = len(bow)


vectors = []
for sentence in corpus:
    vector = [0] * len(bow)
    for word in sentence.split():
        vector[bow[word]] += 1
    vectors.append(vector)

# create a vector for the new question
new_question_vector = [0] * len(bow)
for word in new_question.split():
    new_question_vector[bow[word]] += 1

# calculate cosine similarity between the new question vector and all the other vectors
cosine_similarities = []
for vector in vectors:
    cosine_similarities.append(cosine_similarity(
        [new_question_vector], [vector]))

# find the index of the most similar answer
most_similar_answer_index = cosine_similarities[:-
                                                1].index(max(cosine_similarities[:-1]))

# print the answer
print("Question:", new_question)
print("Answer:", answers[most_similar_answer_index])

