def sort_letters(s):
    words = s.split() 
    
    sorted_words = []  
    
    for word in words:
        sorted_word = ''.join(sorted(word))  
        sorted_words.append(sorted_word)  
    
    result = ' '.join(sorted_words) 
    
    return result


s = "курс основы программирования"
result = sort_letters(s)
print(result)
