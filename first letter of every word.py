# create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
lst = st.split()
new_lst=[]
for word in lst:
    new_lst.append(word[0])
print(new_lst)