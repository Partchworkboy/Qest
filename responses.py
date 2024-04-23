import streamlit as st
import sqlite3

# Create an SQLite database connection
conn = sqlite3.connect("gym_membership.db")
cursor = conn.cursor()

# Example: Retrieve all responses
cursor.execute("SELECT * FROM responses")
all_responses = cursor.fetchall()

# Print the retrieved responses
for response in all_responses:
    print(f"ID: {response[0]}")
    print(f"Name: {response[1]}")
    print(f"Monthly Cost: ${response[2]}")
    print(f"Workout Days: {response[3]} days/week")
    print(f"Preferred Days: {response[4]}")
    print(f"Commitment Level: {response[5]}")
    print(f"Additional Comments: {response[6]}")
    print("-" * 30)

# Close the database connection
conn.close()
