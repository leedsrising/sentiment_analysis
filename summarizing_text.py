from gensim.models import word2vec
from sklearn.manifold import TSNE
from sklearn.cluster import AffinityPropagation
import nltk
from nltk.corpus import words
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import averaged_word_vectorizer

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(MONGO_URI, ssl_cert_reqs=ssl.CERT_NONE)

db=client.ios_app_store_reviews
cursor = db.collection.find({})
reviews =  pd.DataFrame(list(cursor))

# tokenize sentences in corpus
wpt = nltk.WordPunctTokenizer()
# tokenized_corpus = [wpt.tokenize(word) for word in words.words()]
tokenized_corpus = []

#tokenizing based off of reviews
for review in reviews['review'].values:
    for word in review.split():
        tokenized_corpus.append(wpt.tokenize(word))

# Set values for various parameters
feature_size = 100    # Word vector dimensionality  
window_context = 30          # Context window size                                                                                    
min_word_count = 1   # Minimum word count                        
sample = 1e-3   # Downsample setting for frequent words

w2v_model = word2vec.Word2Vec(tokenized_corpus, size=feature_size, 
                          window=window_context, min_count=min_word_count,
                          sample=sample, iter=50)

# view similar words based on gensim's model
similar_words = {search_term: [item[0] for item in w2v_model.wv.most_similar([search_term], topn=5)]
                  for search_term in ['photo', 'cheap', 'David']}

words = sum([[k] + v for k, v in similar_words.items()], [])
wvs = w2v_model.wv[words]

tsne = TSNE(n_components=2, random_state=0, n_iter=10000, perplexity=2)
np.set_printoptions(suppress=True)
T = tsne.fit_transform(wvs)
labels = words

# get document level embeddings
w2v_feature_array = averaged_word_vectorizer(
    corpus=tokenized_corpus,
    model=w2v_model,
    num_features=feature_size
)
corpus_df = pd.DataFrame(w2v_feature_array)

ap = AffinityPropagation()
ap.fit(w2v_feature_array)
cluster_labels = ap.labels_
cluster_labels = pd.DataFrame(cluster_labels, columns=['ClusterLabel'])
print(pd.concat([corpus_df, cluster_labels], axis=1))