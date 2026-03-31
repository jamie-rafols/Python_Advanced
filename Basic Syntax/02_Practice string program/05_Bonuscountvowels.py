sen = "This is a sentencewe"
sum = 0
vowels = ['a', 'e','i','o','u']

for char in sen.lower():
   # print(char)
    if (char in vowels):
        sum+=1
        
print(f"There are {sum} vowels in this sentence")
print(vowels)