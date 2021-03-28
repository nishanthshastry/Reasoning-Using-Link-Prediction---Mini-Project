import numpy as np
import pandas as pd
import random
import string
import pickle
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer 
# Convert a collection of raw documents to a matrix of TF-IDF features.

#df = pd.read_csv("final_dataset.csv")
# file = open("final_dataset.csv")

#ques = df["Questions"].values.astype(str).tolist()
#ans = df["Answers"].values.astype(str).tolist()

class link_predict:
	def __init__(self):
		self.vectorizer_path = ("vectorizer.pickle")
		self.train_matrix_path = ("training_matrix.pickle")

		df = pd.read_csv("final_dataset.csv")
		df = df.dropna()
		self.ques = df["Questions"].values.astype(str).tolist()
		self.ans = df["Answers"].values.astype(str).tolist()

		try:
			fp = open(self.vectorizer_path, 'rb')
			self.vectorizer = pickle.load(fp)
			fp.close()

			fp = open(self.train_matrix_path, 'rb')
			self.train_matrix = pickle.load(fp)
			fp.close()
		except:
			self.vectorizer, self.train_matrix = self.model(self.vectorizer_path, self.train_matrix_path)

	def model(self, vectorizer_path, train_matrix_path):
		i = 0
		sentences = []
		sentences.append(" eos")
		sentences.append(" eos")

		for row in self.ques:
			sentences.append(row)
			i += 1

		vectorizer = TfidfVectorizer()
		train_matrix = vectorizer.fit_transform(sentences)  

		# fit_transform(raw_documents, y=None) - Syntax
		# fit_transform(raw_documents[, y]) - Learn vocabulary and idf, return document-term matrix.
		
		# raw_documents - An iterable which yields either str, unicode or file objects.
		# y parameter in ignored
		
		# Returns X - sparse matrix of (n_samples, n_features)
		# (Tf-idf-weighted document-term matrix.)

		fp = open(vectorizer_path, 'wb')
		pickle.dump(vectorizer, fp)
		fp.close()

		fp = open(train_matrix_path, 'wb')
		pickle.dump(train_matrix, fp)
		fp.close()

		return vectorizer, train_matrix

	def ask_question(self, test_sentence):
		min_score = 0.8
		test = (test_sentence, "")
		test_matrix = self.vectorizer.transform(test)
       
		# transform(raw_documents, copy='deprecated') - Syntax
		# transform(raw_documents[, copy]) - Transform documents to document-term matrix.
		# Uses the vocabulary and document frequencies (df) learned by fit (or fit_transform).
		
		# raw_documents - An iterable which yields either str, unicode or file objects.
		# copy - bool, default=True - Whether to copy X and operate on the copy or perform in-place operations.
		# copy parameter is generally ignored
		
		# Returns X - sparse matrix of (n_samples, n_features)
		# (Tf-idf-weighted document-term matrix.)

		cosine = cosine_similarity(test_matrix, self.train_matrix)

		# cosine_similarity(X, Y=None, dense_output=True) - Syntax
		# computes similarity as the normalized dot product of X and Y,
		# K(X, Y) = <X, Y> / (||X||*||Y||)
		
		# X: ndarray or sparse array, shape: (n_samples_X, n_features) - Input data.
		# Y: ndarray or sparse array, shape: (n_samples_Y, n_features) - Input data. 
		# dense_output: boolean (optional), default True - ignored with respect our project
		# If None, the output will be the pairwise similarities between all samples in X.

		cosine = np.delete(cosine, 0)
		max_score = cosine.max()
		if (max_score > min_score):
			new_max_score = max_score - 0.01
			l = np.where(cosine > new_max_score)
			ans_index = random.choice(l[0])
		else:
			return "", 0
		j = 0

		for row in self.ans:
			j += 1
			if j == ans_index:
				return row, max_score

	def result(self, question):
		answer, score = self.ask_question(question)
		return answer


df = pd.read_csv("final_dataset.csv")
print(df.head())
print("\n")
print(df.tail())

check_list = []
for index, row in df.iterrows():
	check_list.append((row['Questions'], row['Answers']))

yes = 0
no = 0

link = link_predict()

for i in check_list:
	answer = link.result(i[0].lower())
	if answer == i[1]:
		yes = yes + 1
	else:
		no = no + 1

accuracy = (yes/len(check_list))*100

print("\n")
print("Q/A count: - ", len(check_list))
print("Passed Test cases: - ", yes)
print("Failed Test cases: - ", no)
print("Accuracy: - ", "{:.2f}".format(accuracy), "%")