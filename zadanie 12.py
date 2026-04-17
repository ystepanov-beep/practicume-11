def count_word_holes(word):
    '''
    Count letters with holes in word
    '''
    holes_letters = "abdegopq"
    count = 0
    for char in word:
        if char in holes_letters:
            count += 1
    return count

def process_text(text):
    '''
    Processes text and print results
    '''
    words = text.split()
    
    total_holes = 0
    total_no_holes = 0
    special_words = []
    
    for word in words:
        holes_in_word = count_word_holes(word)
        no_holes_in_word = len(word) - holes_in_word
        
        total_holes += holes_in_word
        total_no_holes += no_holes_in_word
        
        if holes_in_word >= 2:
            special_words.append(word)
            
    print(total_holes, total_no_holes)
    print(special_words)

input_text = input()
process_text(input_text)