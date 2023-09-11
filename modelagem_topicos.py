from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import KeyBERTInspired
from bertopic.vectorizers import ClassTfidfTransformer
import pandas as pd
import PyPDF2
import nltk
from nltk.corpus import stopwords
import re
import string

#https://maartengr.github.io/BERTopic/index.html#attributes
#@article{grootendorst2022bertopic,
#  title={BERTopic: Neural topic modeling with a class-based TF-IDF procedure},
#  author={Grootendorst, Maarten},
#  journal={arXiv preprint arXiv:2203.05794},
#  year={2022}
#}
nltk.download('punkt')
nltk.download('stopwords')

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return [text]

def preprocess(docs):
    new_doc = []
    
    for doc in docs:
        tokens = nltk.word_tokenize(re.sub(f"[{re.escape(string.punctuation)}]", ' ', doc.lower()))
        filtered_tokens = [w for w in tokens if len(w) > 1 and w not in pt_stopwords]
        new_doc.extend(filtered_tokens)
        ## add feature para não separar palavras com hífen
    return new_doc

pt_stopwords = set(stopwords.words('portuguese'))
doc = preprocess(extract_text('./raw_data/portaria_rede_cegonha.pdf'))

#https://www.sbert.net/docs/pretrained_models.html
topic_model_emb = BERTopic(language='portuguese', embedding_model='multi-qa-MiniLM-L6-cos-v1', vectorizer_model=CountVectorizer(ngram_range=(1, 2)))
topics_emb, probs_emb = topic_model_emb.fit_transform(doc)

#https://maartengr.github.io/BERTopic/getting_started/ctfidf/ctfidf.html
topic_model_tfidf = BERTopic(language='portuguese', ctfidf_model=ClassTfidfTransformer(), vectorizer_model=CountVectorizer(ngram_range=(1, 2)))
topics_tfidf, probs_emb = topic_model_tfidf.fit_transform(doc)

# Modelagem - Embedings
topic_model_emb.visualize_topics
#Modelage TFIDF
topic_model_tfidf.visualize_documents

#topic_model.get_document_info(docs)

# Fine-tune your topic representations
#representation_model = KeyBERTInspired()
#topic_model = BERTopic(representation_model=representation_model)

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
# of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval, 2022