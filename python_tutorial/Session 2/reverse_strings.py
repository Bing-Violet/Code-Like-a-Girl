#use list() function to reverse a string
sentence = 'Code like a girl is fun!'

#converting sentence into a list
sentence_list = list(sentence)
print(sentence_list)

#reverse the list
sentence_list.reverse()
print(sentence_list)

#join all the elements in the list on an empty string
reversed_sentence = ''.join(sentence_list)
print(reversed_sentence)
