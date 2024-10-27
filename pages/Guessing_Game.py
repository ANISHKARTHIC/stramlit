import streamlit as st
import random

st.title("WELCOME TO GUESSING GAME")

if 'guessing_num' not in st.session_state:
    st.session_state.guessing_num = random.randint(1, 50)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.name = ""
    st.write('''
        **RULES**:  
        The rules are simple. The computer has chosen a random number between 1 and 50.  
        Try to guess the number! You’ll receive hints of "higher" or "lower" based on your input.  
        The game will keep track of your attempts.
    ''')

if not st.session_state.name:
    st.session_state.name = st.text_input("Enter your name:")
    if st.session_state.name:
        st.write("Let's start the game!")


if st.session_state.name:
    st.write("The Computer has guessed a number between 1 and 50.")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=50, step=1)

    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1  
        
        if guess < st.session_state.guessing_num:
            st.write("Try a higher number!")
        elif guess > st.session_state.guessing_num:
            st.write("Try a lower number!")
        else:
            st.write(f"Congratulations, {st.session_state.name}! You guessed it in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True

    if st.button("Restart Game"):
        st.session_state.guessing_num = random.randint(1, 50)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.write("Game restarted! Try to guess the new number.")
