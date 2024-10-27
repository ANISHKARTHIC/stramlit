import streamlit as st
import random

st.markdown("""
    <style>
        .game-title {color: #FF6347; font-size: 40px; font-weight: bold; text-align: center; margin-bottom: 20px;}
        .rules {font-size: 18px;colour:; color: #f0f8ff; padding: 10px; border-radius: 10px; margin: 20px 0;}
        .result {font-size: 22px; font-weight: bold; color: #228B22;}
        .higher-lower {color: #FF4500; font-weight: bold;}
        .restart-button {margin-top: 20px; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='game-title'>Welcome to the Guessing Game!</div>", unsafe_allow_html=True)

if 'guessing_num' not in st.session_state:
    st.session_state.guessing_num = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.name = ""

if not st.session_state.name:
    st.write("""
        <div class='rules'>
            <strong>Rules:</strong><br>
            The computer has chosen a random number between 1 and 50.<br>
            Try to guess the number! You’ll receive hints of "higher" or "lower" based on your input.<br>
            The game keeps track of your attempts. Good luck!
        </div>
    """, unsafe_allow_html=True)

if not st.session_state.name:
    st.session_state.name = st.text_input("Enter your name:")
    if st.session_state.name:
        st.write(f"Welcome, {st.session_state.name}! Let's start the game!")

if st.session_state.name:
    st.write("The computer has selected a number between 1 and 50.")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1
        
        if guess < st.session_state.guessing_num:
            st.write("<div class='higher-lower'>Try a higher number!</div>", unsafe_allow_html=True)
        elif guess > st.session_state.guessing_num:
            st.write("<div class='higher-lower'>Try a lower number!</div>", unsafe_allow_html=True)
        else:
            st.write(f"<div class='result'>Congratulations, {st.session_state.name}! You guessed it in {st.session_state.attempts} attempts!</div>", unsafe_allow_html=True)
            st.session_state.game_over = True

    if st.button("Restart Game"):
        st.session_state.guessing_num = random.randint(1, 50)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.write("Game restarted! Try to guess the new number.")
