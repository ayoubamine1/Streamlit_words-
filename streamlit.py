

import streamlit as st
import pickle
import sqlite3
import random
import time 

f = open('word_list.js')
stg = f.read()
stg = stg.replace('\n','').replace(';','').split('=')[1].replace('[','').replace(']','').replace('"','').replace(' ','')
word =str(stg).split(',')


def select_unique_random_words(words, num_words):
    # Connect to the SQLite database
    conn = sqlite3.connect('selected_words.db')
    c = conn.cursor()
    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS selected_words
                (words text)''')
    size =  print(c.execute("SELECT COUNT(*) FROM selected_words").fetchone())
    selected_words = random.sample(words, num_words)
    while True:
        # Check if the selected words are already in the table
        c.execute("SELECT * FROM selected_words WHERE words = ?", (str(selected_words),))
        if c.fetchone() is None:
            # if not in table, insert the selected words and return
            c.execute("INSERT INTO selected_words (words) VALUES (?)", (str(selected_words),))
            conn.commit()
            return selected_words,size
        else:
            # if already in table, reselect words
            selected_words = random.sample(words, num_words),size
    conn.close()



#feel = st.text_input("Enter the Feeling: ",key="feeling")


if st.button('Generate Words'):
    
    for i in range(100000):  
        selected_words,size = select_unique_random_words(word, 12)
        sentence =  ', '.join(selected_words)
        st.write(f"The words are : {sentence}{ size}")

    






