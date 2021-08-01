a: str = input("Enter a sentence: ")
lower_case = a.lower()
vowel_count = {}
for i in "aeiou":
    count = lower_case.count(i)
    vowel_count[i] = count

print(vowel_count)

count = vowel_count.values()
total_vowels = sum(count)
print(f'The total number of vowels in the sentence is {total_vowels}')
