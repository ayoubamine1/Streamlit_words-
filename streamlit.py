import streamlit as st
import pickle
import numpy as np



if st.button('Generate Words'):
    file = open('state.txt')
    state = []
    for line in file:
        state.append(int(line.replace('\n','')))
    file.close()

    # extract the words from the file 
    f = open('word_list.js')
    stg = f.read()
    stg = stg.replace('\n','').replace(';','').split('=')[1].replace('[','').replace(']','').replace('"','').replace(' ','')
    words =str(stg).split(',')
    f.close()

    n = len(words)

    i = 0
    while i <=10000 :
        if len(np.unique(state)) == 12 : 
            lst =  [words[j] for j in state]
            sentence = ' '.join(lst)
            st.write(f"The words are : {sentence}")
            i+=1

        state[0] += 1
        for k in range(11):
            if state [k] == n :
                state[k] = 0
                state[k+1] += 1
            else: 
                break 
        if state[-1] == n:
            state = [12-i for i in range(1,13)]
    file = open('state.txt','w')
    for i in state:
        file.write(str(i)+'\n')
    file.close()
            
