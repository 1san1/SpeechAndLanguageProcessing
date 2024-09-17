import re
import random 

corpus = """Run your n-gram program on two different small corpora of your choice (you
 might use email text or news groups). Now compare the statistics of the two
 corpora. What are the differences in the most common unigrams between the
 two? How about interesting differences in bigrams?"""

pattern0 = r"(\n)"
sentence0 = re.sub(pattern0, "", corpus)
pattern = r"([a-zA-Z0-9]+)([^a-zA-Z0-9\s])"
replacing = r"\1 \2"
sentence = re.sub(pattern, replacing, sentence0)
pattern2 = r"([^a-zA-Z0-9\s])([a-zA-Z0-9]+)"
sentence2 = re.sub(pattern2, replacing, sentence)
pattern3 = r"([^a-zA-Z0-9\s])([^a-zA-Z0-9\s])"
sentence3 = re.sub(pattern3, replacing, sentence2)
# pattern4 = r"(\))"
# sentence4 = re.sub(pattern, " \1", sentence3)

unigrams = sentence3.split(" ")

word_count = {}

# Iterate over each word in the list
for word in unigrams:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
# for word, count in word_count.items():
#     print(f"{word}: {count}")

vocab = [key for key in word_count]
# print(vocab)

bigrams = []
for i in range(len(vocab)-1):
    j = i + 1
    while j < len(vocab):
        bigrams.append(f"{vocab[i]} {vocab[j]}")
        bigrams.append(f"{vocab[j]} {vocab[i]}")
        j = j+1

# print(bigrams)

print(len(vocab))
print(len(bigrams))

bigram_count = {}

# Iterate over each word in the list
for word in bigrams:
    if word in word_count:
        bigram_count[word] += 1
    else:
        bigram_count[word] = 1

# # Print the word counts
# for word, count in bigram_count.items():
#     print(f"{word}: {count}")

bigram_vocab = [key for key in bigram_count]

u = ""

for i in range(5):
    a = random.randint(0, len(vocab))
    u += " "+vocab[a]

print(u)

bi = ""
for i in range(5):
    b = random.randint(0, len(bigram_vocab))
    bi += " "+bigram_vocab[b]

print(bi)