
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="☆")
st.title("Growth Mindset  Challenge: Web App with Streamlit")

st.header("Welcome to your Growth Journey!")
st.write("Embrace challanges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challanges, and achivements! ✨")

st.header("Today's Growth Mindset Qoute")
st.write("Success is not final, is not fatal: it is courage to continue that counts_winston Churchill")

st.header("🎀 What's Your Challenge TOday?")
user_input= st.text_input("Describe's a challenge your'e facing:")

if user_input:
    st.success(f"you re facing: {user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")
    
    #reflection
st.header("Reflection on your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" Great Insight! Your  reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")
    
#achiements
st.header("♥ Celebrate Your Wins!")
acheivment = st.text_input("share somthing you've accomplished:")

if acheivment:
    st.success(f" ✨  Amazing! You achieved: {acheivment}")
else:
    st.info("Big or small, every acheivement counts! Share one now😍")
    
    #footer
    st.write("- - -")
    st.write("Keep believing in yourself. Growth is a journey, not a destination!🤍")
    st.write("**❗  Created by Syeda Nameera***")
