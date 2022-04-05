import frequency
possible_words = []
not_included_letters = ""
letters_pos_not_known = ""
letters_pos_known = {
    "letters":"",
    "position":"" #REMEMBER TO CONVERT THIS TO AN INT WHEN USING
}

with open ("wordle/words.txt","r") as file:
    words = file.read().splitlines()



def Word_Remover():
    global words,possible_words,not_included_letters,letters_pos_not_known,letters_pos_known
    for i in range (len(words)):
        if len(words[i]) == 5:
            possible_words.append(words[i])
            for k in range (len(not_included_letters)):
                if not_included_letters[k] in possible_words[len(possible_words)-1]:
                    possible_words.pop()
                    break
            if possible_words:
                
                for j in range (len(letters_pos_not_known)):
                    if letters_pos_not_known[j] not in possible_words[len(possible_words)-1]:
                        possible_words.pop()
                        break
                for j in range (len(letters_pos_known["letters"])):
                    position_of_known_letter=int(letters_pos_known["position"][j])
                    if letters_pos_known["letters"][j] not in possible_words[len(possible_words)-1][position_of_known_letter]:
                        possible_words.pop()
                        break
    possible_words.sort(key=frequency.of_word)


    #words = possible_words
    #new_not_included_letters = input("Please input the new letters that are not included.\n")
    #not_included_letters+=new_not_included_letters
    #not_included_letters = "".join(dict.fromkeys(not_included_letters))

Word_Remover()

print(possible_words)