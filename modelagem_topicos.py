from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
from bertopic.representation import KeyBERTInspired

#https://maartengr.github.io/BERTopic/index.html#attributes
#@article{grootendorst2022bertopic,
#  title={BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
#  author={Grootendorst, Maarten},
#  journal={arXiv preprint arXiv:2203.05794},
#  year={2022}
#}

##documents = df['corpus'].tolist()
#preprocessed_corpus = prepare_text_for_topicmodel(documents)

#pt_stopwords = nltk.corpus.stopwords.words('portuguese')
#punctuation = r'[/.!$%^&#*+\'\"()-.,:;<=>?@[\]{}|]'

#def prepare_text_for_topicmodel(documents):
#    # remove punctuation
#    pp_documents = [re.sub(punctuation, ' ', doc)
#                    for doc in documents]
#    # convert to lowercase
#    pp_documents = [doc.lower() for doc in pp_documents]
#    # remove stopwords
#    pp_documents = [' '.join([w for w in doc.split() if 
#                    len(w) > 1 and w not in pt_stopwords])
#                    for doc in pp_documents]
#   return pp_documents
#embedding_model = load_embedding_model()
#embeddings = get_embedding(documents, embedding_model)
#model = BERTopic(embedding_model=embedding_model,
#                 n_gram_range=(1, 2))
#topics, probabilities = model.fit_transform(documents=documents, 
#                                            embeddings=embeddings)
##D. Vianna, E. Moura. Organizing Portuguese Legal Documents through Topic Discovery. Proceedings 
# of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, 2022.
docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']
#print(docs)

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)

topic_model.get_topic(0)
topic_model.get_document_info(docs)

# Fine-tune your topic representations
representation_model = KeyBERTInspired()
topic_model = BERTopic(representation_model=representation_model)
