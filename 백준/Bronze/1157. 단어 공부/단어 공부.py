word = list(input().lower())
letters = list(set(word))
counts = []
for letter in letters:
  counts.append(word.count(letter))

if counts.count(max(counts)) > 1:
  print('?')
else:
  print(letters[counts.index(max(counts))].upper())