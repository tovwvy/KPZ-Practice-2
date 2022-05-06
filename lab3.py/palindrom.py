import platform

def palindrome(text):
  

    word_list = []
    temp = ''
    for i, v in enumerate(text):
        if v.isalpha():  
            temp += v
            if i == len(text) - 1 and temp.isalpha():
                word_list.append(temp)
        else:  
            word_list.append(temp)
            temp = ''

  

    pal_words = []
    for i in word_list:
        i = i.lower()
        reversed_word = i[::-1] 
        if len(i) < 3:
            continue
        if reversed_word == i:  
            pal_words.append(i)
    return pal_words


palindrome("Lol  kek  asdd  fdf")

