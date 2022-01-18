import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import matplotlib
import matplotlib.pyplot as plt

##%matplotlib inline
##%config InlineBackend.figure_format = 'retina'

data = pd.read_csv("train.csv", header=[0])
print(data.head(2))
##print(data)
##print(data.shape)

