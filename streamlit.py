import streamlit as st
import pickle
import numpy as np

# extract the words from the file 
    '''f = open('word_list.js')
    stg = f.read()
    stg = stg.replace('\n','').replace(';','').split('=')[1].replace('[','').replace(']','').replace('"','').replace(' ','')
    words =str(stg).split(',')
    f.close()'''


if st.button('Generate Words'):
    file = open('state.txt')
    state = []
    for line in file:
        state.append(int(line.replace('\n','')))
        
    file.close()

    words = np.load('words.npy')

    n = len(words)

    i = 0
    while i <=10000 :
        if len(np.unique(state)) == 12 : 
            lst =  [words[j] for j in state]
            sentence = ' '.join(lst)
            st.write(sentence)
            i+=1
            print(i)

        state[0] += 1+n+n**2+n**3+n**4+n**5 
        for k in range(11):
            if state [k] >= n :
                state[k+1] += int(state[k]/n)
                 state[k] = int( state [k]%n)
            else: 
                break 
        if state[-1] > n:
            state = [12-i for i in range(1,13)]
    file = open('state.txt','w')
    for i in state:
        file.write(str(i)+'\n')
    file.close()
            
