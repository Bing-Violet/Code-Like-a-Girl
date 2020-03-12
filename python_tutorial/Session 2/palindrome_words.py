#use list() function to reverse a string
word = 'racecar'

#converting sentence into a list
word_list = list(word)
print(word_list)

#reverse the list
word_list.reverse()
print(word_list)

#join all the elements in the list on an empty string
reversed_word = ''.join(word_list)
print(reversed_word.lower() == word.lower())
