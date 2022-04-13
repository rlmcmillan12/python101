# # Accessing Data

# phonebook_dict = {
#     "Alice": "703-493-1834",
#     "Bob": "857-384-1234",
#     "Elizabeth": "484-584-2923",
# }

# # print(phonebook_dict["Elizabeth"])
# phonebook_dict["Kareem"] = "938-489-1234"
# phonebook_dict.pop("Alice")
# phonebook_dict["Bob"] = "986-345-2345"
# # print(phonebook_dict)

# for i in phonebook_dict:
#     print(i)
#     print(phonebook_dict[i])


# Nested Dictionaries


# ramit = {
#     "name": "Ramit",
#     "email": "ramit@gmail.com",
#     "interests": ["movies", "tennis"],
#     "friends": [
#         {
#             "name": "Jasmine",
#             "email": "jasmine@yahoo.com",
#             "interests": ["photography", "tennis"],
#         },
#         {"name": "Jan", "email": "jan@hotmail.com", "interests": ["movies", "tv"]},
#     ],
# }

# print(ramit["email"])
# print(ramit["interests"][0])
# print(ramit["friends"][0]["email"])
# print(ramit["friends"][1]["interests"][1])


## Letter Histogram
# #Write a letter_histogram program that asks the user for input,
# #and prints a dictionary containing the tally of
# #how many times each letter in the alphabet was used in the word


# def letter_history(user_word):
#     letter_count_dict = {}

#     for letter in user_word:
#         if letter not in letter_count_dict:
#             letter_count_dict[letter] = 0
#         letter_count_dict[letter] += 1
#     print(letter_count_dict)


# user_word = input("Enter a word and I will do my magic: ")

# letter_history(user_word)


## Word Histogram
## Write a word_histogram program that asks the user for a sentence as its input,
# and prints a dictionary containing the tally of how many
# times each word in the alphabet was used in the text.


# def word_histogram(user_sentence):
#     user_sentence_list = user_sentence.split()
#     word_count_dict = {}

#     for words in user_sentence_list:
#         if words not in word_count_dict:
#             word_count_dict[words] = 0
#         word_count_dict[words] += 1
#     print(word_count_dict)


# user_sentence = input("Type a sentence and I will so my magic: ")

# word_histogram(user_sentence)


## Bonus: Histogram Tally
## Given a histogram tally (one returned from either letter_histogram or word_summary),
# print the top 3 words or letters:


# def word_histogram(user_sentence, word_count_dict):
#     user_sentence_list = user_sentence.split()
#     word_count_dict = {}
#     for words in user_sentence_list:
#         if words not in word_count_dict:
#             word_count_dict[words] = 0
#         word_count_dict[words] += 1
#     return word_count_dict


# def top3Sorter(word_count_dict):
#     top3 = {}

#     sorted_word_count_dict = sorted(
#         word_count_dict, key=word_count_dict.get, reverse=True
#     )[:3]

#     # for word in sorted_word_count_dict:
#     #     top3[word] = sorted_word_count_dict[word]
#     print(sorted_word_count_dict)


# user_sentence = input("Type a sentence and I will so my magic: ")
# word_count_dict = {}
# word_histogram(user_sentence, word_count_dict)
# top3Sorter(word_count_dict)

# # top3Sorter(sorted_word_count_dict)
