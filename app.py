import streamlit as st
import pickle 

#loading model
model=pickle.load(open('sentiment_analysis.pkl','rb'))

#creating Title
st.title("IMDB review Sentiment Analysis AI Model")

review=st.text_input("Enter your Review")
submit=st.button("Predict")

if submit:
    prediction=model.predict([review])
    
    # print(prediction)
    # st.write(prediction)
    if prediction[0]=='positive':
        st.success("Positive Review")
    else:
        st.warning("Negative Review")