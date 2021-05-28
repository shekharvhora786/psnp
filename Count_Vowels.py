def count_vowels(string):
    count=0
    string.lower()
    for char in string:
        if char in "aeiou":
           count = count+1
    print(count,"vowel available in given text")

input_string =input("enter text to check vowel count\n")
count_vowels(input_string)