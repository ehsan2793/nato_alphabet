import pandas as p

data = p.read_csv('nato-alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

nato = [phonetic_dict[item] for item in word ]

print(nato)