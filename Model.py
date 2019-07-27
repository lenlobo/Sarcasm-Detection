
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


def parseJson(fname):
    for line in open(fname, 'r'):
        yield eval(line)


# In[4]:


data = list(parseJson('./tweets.json'))


# In[5]:


df=pd.DataFrame(data)


# In[6]:


import nltk


# In[7]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[8]:


sid = SentimentIntensityAnalyzer()


# In[9]:


newDF=df.values.T.tolist()


# In[10]:


newDF


# In[11]:


del(newDF[0])


# In[12]:


newnewDF=newDF[0]


# In[13]:


kek=[]
import textblob as TextBlob


# In[14]:


for sentence in newnewDF:
     kek.append(sid.polarity_scores(sentence))


# In[15]:


someDF=pd.DataFrame(kek)


# In[16]:


df=df.join(someDF)


# In[17]:


df.head()


# In[18]:


df=df.drop(['article_link'],axis=1)


# In[19]:


df


# In[22]:


from sklearn.model_selection import train_test_split


# In[23]:


X=df[['compound','pos','neu','neg']]


# In[24]:


y=df['is_sarcastic']


# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=111)


# In[26]:


from sklearn.tree import DecisionTreeClassifier


# In[27]:


dtree = DecisionTreeClassifier()


# In[28]:


dtree.fit(X_train,y_train)


# In[29]:


predictions = dtree.predict(X_test)


# In[30]:


from sklearn.metrics import classification_report,confusion_matrix


# In[33]:


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

