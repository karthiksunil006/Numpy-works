import nltk

nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download("punkt")
nltk.download("punkt_tab")


sentence_1="earth is third planet from the sun"
sentence_2="jupiter is the largest planet"

stopwords=set(stopwords.words("english"))

def preprocess(text):

    tokens=word_tokenize(text.lower())

    new=[i for i in tokens if i not in stopwords]

    return " ".join(new)

new_sentence_1=preprocess(sentence_1)
new_sentence_2=preprocess(sentence_2)

print(new_sentence_1)
print(new_sentence_2)


obj=TfidfVectorizer()

result_matrix=obj.fit_transform([new_sentence_1,new_sentence_2])
print(result_matrix)
similarity=cosine_similarity(result_matrix[0],result_matrix[1])
print(f"Similarity between sentence_1 and sentence_2 = {similarity[0][0]}")