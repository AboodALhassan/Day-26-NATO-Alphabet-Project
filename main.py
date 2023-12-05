import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(data)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}
print(alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")

word_list = [alphabet_dict[letter] for letter in word.upper()]

print(word_list)

