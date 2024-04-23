import streamlit as st
import sqlite3
import pandas as pd

# Create an SQLite database connection
conn = sqlite3.connect("gym_membership.db")
cursor = conn.cursor()

# Create a table to store questionnaire responses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY,
        name TEXT,
        monthly_cost INTEGER,
        workout_days INTEGER,
        preferred_days TEXT,
        commitment_level TEXT,
        additional_comments TEXT

def home():
    st.title("Home")
    st.write("This is a questionnaire to be used for Team Naalya's Various surveys")

def questionnaire():
    st.title("Gym Membership Questionnaire")

    # Question 1: Person's name
    user_name = st.text_input("Enter your name:")
    st.write(f"Hello, {user_name}!")

    # Question 2: How much are you willing to pay per month?
    monthly_cost = st.slider("How much are you willing to pay per workout day?", min_value=5000, max_value=30000, step=1000, value=1000)

    # Question 3: How many days per week can you work out?
    workout_days = st.selectbox("How many days per week can you work out?", [1, 2, 3, 4, 5, 6, 7])

    # Question 4: Which days of the week do you prefer for workouts?
    preferred_days = st.multiselect("Select preferred workout days:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    # Question 5: How committed are you to working out?
    commitment_level = st.radio("How committed are you to working out?", ["Not very committed", "Moderately committed", "Highly committed"])

    # Question 6: Additional comments or preferences
    additional_comments = st.text_area("Any additional comments or preferences?")

    # Save responses to the database
    if st.button("Submit"):
        insert_response(user_name, monthly_cost, workout_days, preferred_days, commitment_level, additional_comments)
        st.success("Your responses have been saved!")

def insert_response(name, monthly_cost, workout_days, preferred_days, commitment_level, additional_comments):
    cursor.execute("""
        INSERT INTO responses (name, monthly_cost, workout_days, preferred_days, commitment_level, additional_comments)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, monthly_cost, workout_days, ', '.join(preferred_days), commitment_level, additional_comments))
    conn.commit()


def responses():
    st.title("Responses")
    # Create a connection to the SQLite database
    conn = sqlite3.connect("gym_membership.db")

    # Retrieve all responses from the 'responses' table
    df = pd.read_sql_query("SELECT * FROM responses", conn)

    # Close the database connection
    conn.close()

    # Display the responses in a Streamlit dataframe
    st.write("### Responses")
    st.dataframe(df)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select an option", ["Home", "Questionnaire", "Responses"])

    if page == "Home":
        home()
    elif page == "Questionnaire":
        questionnaire()
    elif page == "Responses":
        responses()

if __name__ == "__main__":
    main()
