import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
	st.title(" Spam Classification ")
	st.subheader("Build With Python")
	msg=st.text_input("Enter the Text: ")
	if st.button("Predict"):
		 data=[msg]
		 vect=cv.transform(data).toarray()
		 prediction=model.predict(vect)
		 result=prediction[0]
		 if result==1:
		 	st.error("This is a spam mail")
		 	speak("This is a spam mail")
		 else:
		    st.success("This is a Ham mail")
		    speak("This is a Ham mail")	

main()	