letter = input('enter letters seperated by ' ' spaces: ')

letter_list = letter.split(' ')

with open("words.txt", "r") as filea:
    
    lines = filea.readlines()
    
    for word in lines:
        satisfy = True
        
        for letter in letter_list:
            
            if letter not in word:

                satisfy = False

        if satisfy:
            print(word)