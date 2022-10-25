#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st 
import pickle
import pandas as pd
import numpy as np


# In[2]:


import requests
from streamlit_lottie import st_lottie


# In[3]:


st.set_page_config(page_title="My webpage", layout="wide")
st.title('Model Deployment' )
st.header("Book Recommendation System :books:")


# In[6]:


def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# In[5]:


lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ybiszbil.json")


# In[8]:


user_sim_df = pickle.load(open(r"C:\Users\vikra\EXCELER\project 1\user_sim_df.pkl","rb"))
data = pickle.load(open(r"C:\Users\vikra\EXCELER\project 1\data.pkl","rb"))


# In[9]:


def user_similar_to(user_id):
    if user_id in list(user_sim_df):
        sim_user = list(user_sim_df.sort_values([user_id],ascending=False).head(1).index)
        print("Similar User:",sim_user[0])
        print("User ID:",user_id)
    else:
        return 'Invalid Entry'    
    #data["Avg_Rating"]=data.groupby('ISBN')["Book_Rating"].transform('mean')
    #data["No_Of_users_Rated"]=data.groupby('ISBN')["Book_Rating"].transform('count') 
    book = data[data['User_ID'] == user_id]
    lis = pd.DataFrame(book.sort_values('Avg_Rating',ascending=False),columns=data.columns)
    list1= lis["Book_Title"].tolist()
    a1=list1
    book2 = data[data['User_ID'] == sim_user[0]]
    lis2 = pd.DataFrame(book2.sort_values('Avg_Rating',ascending=False),columns=data.columns)
    list2= lis2["Book_Title"].tolist()
    a2=list2 
    a3= list (set(a1).intersection(a2))
    #print(" Comman books read by both users :==================================","\n",a3)
    a4=[]
    for i in a2:
        if i not in a3:
            a4.append(i)
    #print("\n","Book Recommend to user :============================================","\n",a4[0:3])
    return a4[0:3]


# In[10]:


with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:        
        User_Id = st.number_input("Enter User ID")
        st.button('Enter')   
        st.write('Recommended Books are:')
        st.write(user_similar_to(User_Id))
    with right_column:
        st_lottie(lottie_coding, height=300 , key = "coding")


# In[ ]:




