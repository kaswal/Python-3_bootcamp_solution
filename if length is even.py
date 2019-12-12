# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

new_lst = st.split()

for word in new_lst:
    if len(word) % 2 == 0:
        print(f'length is even for this word: {word}')