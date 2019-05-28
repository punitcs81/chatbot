import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

example_sent = "find the name of students have marks between 40 and 60"

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent.lower())

my_stop_words = ['a', 'an', 'the', 'select', 'find', 'which', 'whose', 'is', 'of', 'a', 'with',
                 'to', 'for', 'and', 'are', 'what']

Emap = {'between': 'BETWEEN', 'range': 'BETWEEN', 'ranges': 'BETWEEN', 'lies': 'BETWEEN'}
noun_list = ['student', 'Subject', 'Teacher', 'Marks', 'Age', 'roll_no', 'subject_code',
             'Name', 'taught_by', 'Details', 'Subjectwise', 'Id']

filtered_sentence = [w for w in word_tokens if not w in my_stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in my_stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
print(pos_tag(filtered_sentence))
