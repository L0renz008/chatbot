#!/usr/bin/env python
# coding: utf-8

# # Recommandation System

# In[178]:


import pandas as pd
import numpy as np
import random as rd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[179]:


plats = [
    {"id":"11","libélé":"pizza"},
    {"id":"12","libélé":"viande"},
    {"id":"13","libélé":"poisson"},
    {"id":"14","libélé":"burgers"},
]
entrees=[
    {"id":"01","libélé":"Tartinade au fromage de chèvre"},
    {"id":"02","libélé":"Salade jardinière"},
    {"id":"03","libélé":"Portobello Grillé"}
]
desserts=[
    {"id":"21","libélé":"cappuccino"},
    {"id":"22","libélé":"tiramisu"},
    {"id":"23","libélé":"fromages"}
]
vins=[
    {'id':"31",'libélé':'Blanc de Blanc'},
    {'id':"31",'libélé':'2016 Alsace Pinot Noir'},
    {'id':"31",'libélé':'rosé pétillant'},
    {'id':"32",'libélé':'2004 Bandol, Château de Pibarnon'},
    {'id':"32",'libélé':'2018 Côtes de Provence'},
    {'id':"32",'libélé':'2016 Bandol Tempier'},
]


# In[180]:


#les combinaisons :
x_train=[
    [entrees[rd.randrange(0,2)]["libélé"],plats[rd.randrange(0,3)]["libélé"]] for i in range(1000) 
]


# In[181]:


x_test=[
        [entrees[rd.randrange(0,2)]["libélé"],plats[rd.randrange(0,3)]["libélé"]] for i in range(100) 
]


# In[182]:


y_train=[]
for i in x_train:
    if(i[1]=="pizza"):
        if(rd.randrange(0,10)<=7):
            y_train.append("tiramisu")
        else:
            y_train.append("cappuccino")
    if(i[1]=="viande"):
         y_train.append(desserts[rd.randrange(0,2)]["libélé"])
    if(i[1]=="burger"):
        p=rd.randrange(0,10)
        if(p<5):
            y_train.append("cappuccino")
        if(p>=9):
            y_train.append("fromages")
        if(p>=5 and p<=8):
            y_train.append("tiramisu")
    if(i[1]=="poisson"):
        p=rd.randrange(0,10)
        if(p<3):
            y_train.append("cappuccino")
        if(p>=6):
            y_train.append("fromages")
        if(p>=3 and p<=5):
            y_train.append("tiramisu")


# In[183]:


y_test=[]
for i in x_test:
    if(i[1]=="pizza"):
        if(rd.randrange(0,10)<=7):
            y_test.append("tiramisu")
        else:
            y_test.append("cappuccino")
    if(i[1]=="viande"):
         y_test.append(desserts[rd.randrange(0,2)]["libélé"])
    if(i[1]=="burger"):
        p=rd.randrange(0,10)
        if(p<5):
            y_test.append("cappuccino")
        if(p>=9):
            y_test.append("fromages")
        if(p>=5 and p<=8):
            y_test.append("tiramisu")
    if(i[1]=="poisson"):
        p=rd.randrange(0,10)
        if(p<3):
            y_test.append("cappuccino")
        if(p>=6):
            y_test.append("fromages")
        if(p>=3 and p<=5):
            y_test.append("tiramisu")


# In[184]:


print("x_train =",len(x_train),"y_train =",len(y_train),"x_test =",len(x_test),"y_test =",len(y_test))


# In[185]:


for i in range(len(y_train)):
    y_train[i]=[y_train[i]]
for i in range(len(y_test)):
    y_test[i]=[y_test[i]]


# In[186]:


def prepare_inputs(X_train, X_test):
    ohe = OneHotEncoder()
    ohe.fit(X_train)
    X_train_enc = ohe.transform(X_train).toarray()
    X_test_enc = ohe.transform(X_test).toarray()
    return X_train_enc, X_test_enc


# In[187]:


def prepare_targets(y_train, y_test):
    le = OneHotEncoder()
    le.fit(y_train)
    y_train_enc = le.transform(y_train).toarray()
    y_test_enc = le.transform(y_test).toarray()
    return y_train_enc, y_test_enc


# In[188]:


def inverse_transforme_targets(y_enc, y_train):
    le = OneHotEncoder()
    le.fit(y_train)
    y = le.transform(y_enc).toarray()
    return y


# In[189]:


X_train_enc, X_test_enc = prepare_inputs(x_train, x_test)
y_train_enc, y_test_enc = prepare_targets(y_train, y_test)


# In[190]:


model = Sequential()
model.add(Dense(20, input_dim=X_train_enc.shape[1], activation='relu', kernel_initializer='he_normal'))
model.add(Dense(y_train_enc.shape[1], activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X_train_enc, y_train_enc, epochs=100, batch_size=1, verbose=2)


# In[191]:


predictions_enc=model.predict(X_test_enc)


# In[192]:


le = OneHotEncoder()
le.fit(y_train)
predictions=le.inverse_transform(predictions_enc)


# In[193]:


acc=0
for i in range(len(y_test)): 
    if(y_test[i][0]==predictions[i]):
        acc+=1
print("accuracy =",acc/len(y_test))


# In[ ]:





# In[ ]:





# In[ ]:





# In[194]:


y__vins_train_plat=[]
for i in x_train:
    vin=[]
    if(i[1]=="pizza"):
        if(rd.randrange(0,10)<6):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)==7):
            vin.append("Blanc de Blanc")
        elif(rd.randrange(0,10)==8):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)==6):
            vin.append("rosé pétillant")
        else:
            vin.append("2018 Côtes de Provence")
    if(i[1]=="viande"):
        if(rd.randrange(0,10)>8):
            vin.append("Blanc de Blanc")
        elif(rd.randrange(0,10)==4):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)<7):
            vin.append("2016 Alsace Pinot Noir")
        else:
            vin.append("2004 Bandol, Château de Pibarnon")
    if(i[1]=="poisson"):
        if(rd.randrange(0,10)<2):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)>=2 and rd.randrange(0,10)<=4):
            vin.append("2018 Côtes de Provence")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)<7):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)==7):
            vin.append("2004 Bandol, Château de Pibarnon")
        else:
            vin.append("Blanc de Blanc")
    if(i[1]=="burger"):
        if(rd.randrange(0,10)<4):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)>=4 and rd.randrange(0,10)<=6):
            vin.append("2018 Côtes de Provence")
        elif(rd.randrange(0,10)>6 and rd.randrange(0,10)<9):
            vin.append("2016 Bandol Tempier")
        else:
            vin.append("Blanc de Blanc")
    y__vins_train_plat.append(vin)


# In[195]:


y__vins_test_plat=[]
for i in x_test:
    vin=[]
    if(i[1]=="pizza"):
        if(rd.randrange(0,10)<6):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)==7):
            vin.append("Blanc de Blanc")
        elif(rd.randrange(0,10)==8):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)==6):
            vin.append("rosé pétillant")
        else:
            vin.append("2018 Côtes de Provence")
    if(i[1]=="viande"):
        if(rd.randrange(0,10)>8):
            vin.append("Blanc de Blanc")
        elif(rd.randrange(0,10)==4):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)<7):
            vin.append("2016 Alsace Pinot Noir")
        else:
            vin.append("2004 Bandol, Château de Pibarnon")
    if(i[1]=="poisson"):
        if(rd.randrange(0,10)<2):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)>=2 and rd.randrange(0,10)<=4):
            vin.append("2018 Côtes de Provence")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)<7):
            vin.append("2016 Bandol Tempier")
        elif(rd.randrange(0,10)>4 and rd.randrange(0,10)==7):
            vin.append("2004 Bandol, Château de Pibarnon")
        else:
            vin.append("Blanc de Blanc")
    if(i[1]=="burger"):
        if(rd.randrange(0,10)<4):
            vin.append("2016 Alsace Pinot Noir")
        elif(rd.randrange(0,10)>=4 and rd.randrange(0,10)<=6):
            vin.append("2018 Côtes de Provence")
        elif(rd.randrange(0,10)>6 and rd.randrange(0,10)<9):
            vin.append("2016 Bandol Tempier")
        else:
            vin.append("Blanc de Blanc")
    y__vins_test_plat.append(vin)


# In[196]:


y_train_vins_enc, y_test_vins_enc = prepare_targets(y__vins_train_plat, y__vins_test_plat)


# In[197]:


model_vins = Sequential()
model_vins.add(Dense(20, input_dim=X_train_enc.shape[1], activation='relu', kernel_initializer='he_normal'))
model_vins.add(Dense(y_train_vins_enc.shape[1], activation='sigmoid'))
# compile the keras model
model_vins.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model_vins.fit(X_train_enc, y_train_vins_enc, epochs=20, batch_size=1, verbose=2)


# In[198]:


predictions_vins_enc=model_vins.predict(X_test_enc)


# In[199]:


le = OneHotEncoder()
le.fit(y__vins_train_plat)
predictions_vins=le.inverse_transform(predictions_vins_enc)


# In[200]:


acc=0
for i in range(len(y_test)): 
    if(y__vins_test_plat[i][0]==predictions_vins[i]):
        acc+=1
print("accuracy =",acc/len(y_test))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




