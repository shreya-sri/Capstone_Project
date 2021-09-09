import json
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import random
import numpy as np
import torch
from torch.utils.data import TensorDataset


data_file = open('intents.json').read()
intents = json.loads(data_file)

def create(intents):
    words=[]
    classes = []
    documents = []
    ignore_words = ['?', '!']
    for intent in intents['root']:    
        for pattern in intent['question']:
            #tokenize each word
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            #add documents in the corpus
            documents.append((w, intent['intent']))
            
            # add to our classes list
            if intent['intent'] not in classes:
                classes.append(intent['intent'])

    # lemmaztize and lower each word and remove duplicates
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    # sort classes
    classes = sorted(list(set(classes)))
    return words, classes, documents


def get_tensor_dataset(words, classes, documents):
    # create our training data
    training = []
    # create an empty array for our output
    output_empty = [0] * len(classes)
    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
        # create our bag of words array with 1, if word match found in current pattern
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
    
        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
    
        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training, dtype=object)
    # create train and test lists. X - patterns, Y - intents
    patterns = list(training[:,0])
    intents = list(training[:,1])
    return patterns, intents, TensorDataset(torch.Tensor(patterns), torch.Tensor(intents))
