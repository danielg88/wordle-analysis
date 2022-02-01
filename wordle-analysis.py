from collections import Counter

if __name__ == '__main__':

    positionCounters = []
    word_list = []

    with open('words.txt') as f:
      lines = f.readlines()
      for char_number in range(len(lines[0].split()[0])):
        positionCounters.append(Counter())

      for line in lines: 
        for idx in range(len(line.split()[0])):
            positionCounters[idx].update(line[idx])
        word_list.append(line.split()[0])
          

    f.close()
    
    
    position = 1
    for counter in positionCounters: 
        total = sum(counter.values())
        print ("Values for position: ", position)
        print ("{:<8} {:<15} {:<10}".format('Letter','Appeareances','Percent'))
        for key, value in counter.most_common():
            pct = value / total
            print ("{:<8} {:<15} {:.3%} ".format(key, value, pct))
        position += 1

    print ("")
    print ("")
    word_value = {}
    for word in word_list:
        value = 0
        letters = ""
        for letter_idx in range(len(word)):
            
            if word[letter_idx] not in letters:
                value += positionCounters[letter_idx][word[letter_idx]]
            letters += word[letter_idx]

        word_value[word] = value 

    word_rank = sorted(word_value, key=word_value.get, reverse=True)
    
    print ("")
    print ("Top Words by points")
    print ("")
    print ("{:<8} {:<8} ".format('Word','Points'))
    for idx in range(10):
        word = word_rank[idx]
        print ("{:<8} {:<8} ".format(word,word_value[word]))
    


    top_word = word_rank[0]
    repetida = False 

    print ("")
    print ("Top Words without repeating consonants")
    print ("")
    print ("{:<8} {:<8} ".format('Word','Points'))
    print ("{:<8} {:<8} ".format(top_word,word_value[top_word]))
    for idx in range(len(word_rank)):
        word = word_rank[idx]
        repetida = False

        for letter in word:
            if letter in top_word and letter not in "aeiou":
                repetida = True
        if not repetida:
            print ("{:<8} {:<8} ".format(word,word_value[word]))
            top_word += word
 
    top_word = word_rank[0]
    repetida = False 
    print ("")
    print ("Top Words without repeating letters")
    print ("")
    print ("{:<8} {:<8} ".format('Word','Points'))
    print ("{:<8} {:<8} ".format(top_word,word_value[top_word]))
    for idx in range(len(word_rank)):
        word = word_rank[idx]
        repetida = False

        for letter in word:
            if letter in top_word:
                repetida = True
        if not repetida:
            print ("{:<8} {:<8} ".format(word,word_value[word]))
            top_word += word
 