import os
import numpy as np

print('Processing word vectors...')
structured = {}
f = open(os.path.join('.', 'glove.6B.100d.txt'), encoding="utf8")
for line in f:
    values = line.split()
    word = values[0]
    coefficients = np.asarray(values[1:], dtype='float32')
    structured[word] = coefficients
f.close()

print('Found %s word vectors.' % len(structured))


def closest(inp):
    similarity = []

    for w in structured.keys():
        cosine = np.dot(structured[inp], structured[w])/(np.linalg.norm(structured[inp])*np.linalg.norm(structured[w]))
        similarity.append((w, cosine))

    print(sorted(similarity, key=lambda x: x[1], reverse=True)[:5])


def sim(pos, neg):
    similar_words = []
    mean_vec = sum(np.array([structured[i] for i in pos]), np.array([-1 * structured[i] for i in neg]))
    mean = np.linalg.norm(mean_vec)
    for w in structured.keys():
        vector = structured[w]
        cosine_distance = np.dot(mean_vec, vector)/(mean*np.linalg.norm(vector))
        similar_words.append((w, cosine_distance.tolist()[0]))
    print(sorted(similar_words, key=lambda a: a[1], reverse=True)[:5])


sim(['paris', 'germany'], ['france'])
closest('compute')
