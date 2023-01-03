#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route('/')

def home():
    return render_template("Adults.html")


# In[4]:


# Prediction Function

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,14)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


# In[ ]:


# Output page and logic
@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list= request.form.to_dict()
        
        to_predict_list= list(to_predict_list.values())
        to_predict_list=list(map(int, to_predict_list))
        result= ValuePredictor(to_predict_list)
        if int(result)== 1:
            prediction = "Income more than 50K"
        else:
            prediction ="Income less than 50K"
        return render_template("result.html", prediction = prediction)
# Main function
if __name__ == "__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    

