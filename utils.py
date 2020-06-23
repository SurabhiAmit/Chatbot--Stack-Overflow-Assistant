import nltk
import pickle
import re
import numpy as np
import gzip

nltk.download('stopwords')
from nltk.corpus import stopwords

# Paths for all resources for the bot.
RESOURCE_PATH = {
    'INTENT_RECOGNIZER': 'intent_recognizer.pkl',
    'TAG_CLASSIFIER': 'tag_classifier.pkl',
    'TFIDF_VECTORIZER': 'tfidf_vectorizer.pkl',
    'THREAD_EMBEDDINGS_FOLDER': 'thread_embeddings_by_tags',
    'WORD_EMBEDDINGS': 'word_embeddings.tsv',
}


def text_prepare(text):
    """Performs tokenization and simple preprocessing."""

    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()


def load_embeddings(embeddings_path):
    """Loads pre-trained word embeddings from tsv file.

    Args:
      embeddings_path - path to the embeddings file.

    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """

    # Hint: you have already implemented a similar routine in the 3rd assignment.
    # Note that here you also need to know the dimension of the loaded embeddings.
    # When you load the embeddings, use numpy.float32 type as dtype

    
    # remove this when you're done
    #raise NotImplementedError(
       # "Open utils.py and fill with your code. In case of Google Colab, download"
        #"(https://github.com/hse-aml/natural-language-processing/blob/master/project/utils.py), "
       # "edit locally and upload using '> arrow on the left edge' -> Files -> UPLOAD")
   
    embeddings = {}
    #print ("EMBEDDING STARTED")
    file = open(embeddings_path,'r').read().split("\n")
    for text in file:
        if len(text) < 1 : continue
        #print ("finish vec:", text[-1])
        words = text.split("\t")
        words[-1] = words[-1].replace("\n","")
        embeddings[words[0]] = list(map(float,words[1:]))
        #if len(words)-1<100:
            #print (words)
    return embeddings, len(words)-1

 #embeddings={}
   # with open(embeddings_path) as f:
        #for line in f:
           # q, *ex = line.split('\t')
            #print (q,ex)
           # embeddings[q]= ex
   # embeddings_dim= len(ex)
    # return embeddings, embeddings_dim'''
    

def question_to_vec(question, embeddings, dim):
    """Transforms a string to an embedding by averaging word embeddings."""

    # Hint: you have already implemented exactly this function in the 3rd assignment.

    result = np.zeros(dim)
    """
        question: a string
        embeddings: dict where the key is a word and a value is its' embedding
        dim: size of the representation

        result: vector representation for the question
    """
   
    words = question.split()
    count = 0
    for each in words:
        if each in embeddings:
            #print (len(embeddings[each]))
            result =  np.add(result, embeddings[each])
            count += 1
    # print ("TIME TAKEN 2:", time()-start)
    if count > 0:
        result = np.true_divide(result, count)
    # print ("SENTENCE VECTOR: ", result)
    # print ("TIME TAKEN 3:", time()-start)
    return result

    # remove this when you're done
    # raise NotImplementedError(
        #"Open utils.py and fill with your code. In case of Google Colab, download"
        #"(https://github.com/hse-aml/natural-language-processing/blob/master/project/utils.py), "
       # "edit locally and upload using '> arrow on the left edge' -> Files -> UPLOAD")


def unpickle_file(filename):
    """Returns the result of unpickling the file content."""
    with open(filename, 'rb') as f:
        return pickle.load(f)
