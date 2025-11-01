# Day 40 Review Protocol - Natural Language Processing (NLP)



---

## Objective
To review and summarize the complete NLP workflow - from basic text preprocessing to modern transformer-based applications - and connect theoretical understanding with practical notebook exercises.

---

## Introduction - Why Care About Text?
- Text surrounds us: chatbots, search engines, translators, and voice assistants.
- Machines can’t “understand” words directly - they process **numbers**.
- NLP bridges human language → machine-readable numerical data.

**Applications:**
- Spam detection 📨  
- Sentiment analysis ❤️😠  
- Speech recognition 🗣️  

---

## Text Representation
### Local Representation
Each word → a unique number.  


![alt text](image.png)

### Statistical Encodings

Creating vectors of the size of the vocabulary

![alt text](image-1.png)


#### Differnt Kind of Test Preprocessing

### Tokenization

![alt text](image-2.png)

![alt text](image-3.png)

### CountVectorizer
CountVectorizer converts a collection of text documents into a matrix of token counts, showing how often each word appears in each document.

![alt text](image-4.png)

**Example Code:**
```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
corpus = ['This is the first document', 'This document is the second document']
cv = CountVectorizer()
X = cv.fit_transform(corpus)
```

### TF-IDF
TF-IDF stands for Term Frequency – Inverse Document Frequency.
It helps find which words are important in a document compared to all other documents.

#### 1. TF (Term Frequency):

→ How often a word appears in a single document.
- Example: In a sentence “I love NLP because NLP is fun”,

   - The word “NLP” appears 2 times,
   - So its TF = 2.

#### 2. IDF (Inverse Document Frequency):
→ How unique or rare a word is across all documents.
- If a word appears in every document (like “the”, “is”), it’s less important.
- If a word appears in few documents (like “NLP”), it’s more important.

#### 3. TF-IDF = TF × IDF
→ A word gets a high score if:
- It appears many times in one document (high TF),
- But appears in few other documents (high IDF).

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus (collection of documents)
corpus = [
    'This is the first document',
    'This document is the second document']

# Create the TF-IDF vectorizer
tfidf = TfidfVectorizer()

# Fit and transform the corpus
X = tfidf.fit_transform(corpus)

# Display the feature names (unique words)
print(tfidf.get_feature_names_out())

# Convert to array form (numerical TF-IDF matrix)
print(X.toarray())
```

### N-grams

To model sequences of words… for example ice and cream make more sense as a 2-gram when they appear together

1-gram → “ice”, “cream”

2-gram → “ice cream”

```python
from nltk import ngrams
text

n = 4

for i in range(1, n):
    print(f"{i} gram\n")
    ngram = ngrams(text.split(), i)
    for gram in ngram:
        print(gram)
    print("-"*10)
```



### Normalization
Think of this as cleaning and standardizing the text.

Goal: make the text uniform and easy to process

- Lowercases everything → “NLP” → “nlp”
- Removes punctuation, extra spaces, or numbers → “Hello!!!” → “hello”
- Can also include stemming or lemmatization as a step

![alt text](image-6.png)


### Stemming
This is a rule-based shortcut that cuts words to their base root form,
but it doesn’t care about real word meaning.

✅ Goal: reduce words to a simpler form to reduce complexity.

⚙️ How: removes common endings like -ing, -ed, -s.

![alt text](image-5.png)

⚠️ “studi” isn’t a real word — stemming just chops endings mechanically.

### Lemmatization

This one is smarter - it uses a dictionary (vocabulary + grammar rules) to find the real base form (lemma) of a word.

✅ Goal: get meaningful root words.

![alt text](image-7.png)

So, lemmatization understands context and grammar, unlike stemming.


#### Stemming or Lemmatization?
It depends…

- Stemming is faster
- Lemmatization preserves more information

### Stop Words

- some words do not provide meaningful information … they are not “content words”
- the list of non-content words is language specific and corpus specific

in example : “Apple **is** looking **at** buying U.K. startup **for** $1 billion”

```python
nltk.download("stopwords")
from nltk.corpus import stopwords

print(stopwords.words('english'))
```

['a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', "he'd", "he'll", 'her', 'here', 'hers', 'herself', "he's", 'him', 'himself', 'his', 'how', 'i', "i'd", 'if', "i'll", "i'm", 'in', 'into', 'is', 'isn', "isn't", 'it', "it'd", "it'll", "it's", 'its', 'itself', "i've", 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she'd", "she'll", "she's", 'should', 'shouldn', "shouldn't", "should've", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', "we'd", "we'll", "we're", 'were', 'weren', "weren't", "we've", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've"]



## Text similarity or Document Similarity
Each document is a vector of features.

Similarity between documents is the similarity between vectors

Usage:

- search engines: query to document
- clustering of documents: document to document
- Question & Answering platforms: query to query

## Text classification
You can use your favourite classifier with text

- Logistic Regression provides nice baseline
- AUC score as performance metric

Some applications:

- spam detection
- sentiment analysis
- hate speech analysis

## Word Embeddings
Relevant items for your task should be similar in the embedding space / i.e close to each other.

![alt text](image-8.png)

### How do we get Word Embeddings
Having lots of data and:

- Read the text
- Process text
- Create x, y data points - for example each 2 words appearing in a text
- Create one hot encodings
- Train a neural network
- Extract the weights from the input layer

### How do we get Word Embeddings
CBOW - Continuous Bag of Words - CBOW learns **from the surrounding words** to predict the **center word**.
- **Input (Context Words):** “word”, “was”, “in”, “all”  
- **Output (Target Word):** “missing”  
![alt text](image-9.png)

Skip-Gram - Skip-Gram learns **from the center word** to predict **the words around it**.
- **Input (Target Word):** “missing”  
- **Output (Context Words):** “word”, “was”, “in”, “all”  
![alt text](image-10.png)




---

### 🔹 What is Hugging Face?

**Hugging Face** is an open-source company and platform that provides:
- Thousands of **pre-trained AI models** for **Natural Language Processing (NLP)**, **Computer Vision**, and **Speech** tasks.
- An easy-to-use Python library called **`transformers`** that lets you use these models with just a few lines of code.
- A huge **model hub** (https://huggingface.co) where developers share and download models.

💡 Think of Hugging Face as **“GitHub for AI models”** — you don’t need to train models from scratch.  
You can just load and use them instantly.

---

### What are Transformers?

**Transformers** are a special kind of **deep learning architecture** designed to handle sequential data (like sentences) more efficiently than older models (like RNNs and LSTMs).

They are the **core technology** behind modern NLP models such as:
- **BERT** (understands text)
- **GPT** (generates text)
- **RoBERTa**, **DistilBERT**, **T5**, etc.

---

### Why Transformers Are Needed

Before Transformers, models like RNNs processed words **one-by-one**, which:
- Was **slow** for long sentences  
- **Forgot earlier words** as the sentence grew longer  
- Couldn’t capture long-distance relationships (like “The cat... it was tired.”)

Transformers solved these problems using a mechanism called **self-attention**, which allows the model to look at **all words at once** and understand their relationships.

For example:  
> In the sentence “The cat sat on the mat because it was tired,”  
> the word **“it”** refers to **“cat.”**  
> A transformer learns this relationship using **attention**.

---
###  Why We Use Hugging Face Transformers

Because training a large model like BERT or GPT from scratch needs:
- Billions of words of text  
- Expensive GPUs  
- Weeks of training  

💡 Hugging Face gives us **ready-made, pre-trained models** we can:
- **Use directly** for classification, summarization, sentiment analysis, etc.
- **Fine-tune** on our own data if we need to adapt them.

---

##  Zero-Shot Learning (ZSL)

### 🔹 What is Zero-Shot Learning?

**Zero-Shot Learning (ZSL)** is a technique where a model can **classify or understand something it has never been trained on before**.

In simple words:
> The model can handle **new tasks or categories** without having any training data for them.




### 🔧 Example — Zero-Shot Classification using Hugging Face

```python
from transformers import pipeline

# Load a pretrained model from Hugging Face Hub
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

text = "Amazon is the longest river in the world."
labels = ["geography", "shopping", "animals"]

result = classifier(text, labels, hypothesis_template="This text is about {}.")
print(result)
```
✅ Output:

{'labels': ['geography', 'shopping', 'animals'],

 'scores': [0.85, 0.10, 0.05]}


### References

Note - Fork it before you use
##### 1_Spam_Classifier.ipynb - https://github.com/neuefische/ds-intro-to-NLP/blob/main/1_Spam_Classifier.ipynb

##### 2_Spam_Zero_Shot.ipynb - https://github.com/neuefische/ds-intro-to-NLP/blob/main/2_Spam_Zero_Shot.ipynb

##### 3_Transformers_Zero_Shot_Pipeline.ipynb - https://github.com/neuefische/ds-intro-to-NLP/blob/main/3_Transformers_Zero_Shot_Pipeline.ipynb

##### 4_create_embeddings.ipynb - https://github.com/neuefische/ds-intro-to-NLP/blob/main/4_create_embeddings.ipynb
