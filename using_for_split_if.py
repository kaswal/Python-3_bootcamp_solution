# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

new_lst=st.split()
for words in new_lst:
    if words[0][0]=='s':
        print(f'this sentence starts with S: {words}')

