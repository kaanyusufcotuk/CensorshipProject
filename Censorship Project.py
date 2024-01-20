censored_list = ["hitler", "nazi", "fuck", "bitch", "dick"]

# Use input() function to get user input
a = input("Please enter a sentence: ")

# Split the input sentence into words
Sentence = a.split()

print("Here is the checked version with censorship:")

for i in Sentence:
    p = ""
    if i[-1] in ["!", "?", ".",","]:
        p = i[-1]
        i = i[:-1]

    for c in censored_list:
        if c.lower() == i.lower(): i = "*" * len(i)
    
    if i != Sentence[-1]: print(i, end=p + " ") 
    else: print(i, end=p)
