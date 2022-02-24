#to write a program to generate a acronym for a given word
#acronym=creating a short word from a sentence

#taking the input from the user
user_input=input("Enter the word to generate an acronym:")
sentence_split=user_input.split()
a=" "
for i in sentence_split:
    a=a+str(i[0]).upper()     #upper()=generate output in upper case
print(a)
