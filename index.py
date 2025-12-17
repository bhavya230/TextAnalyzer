#taking a textfile  as input 
with open("text.txt") as file :
    text= file.read()
    #GOAL- COUNT WORDS, CHARACTERS , SENTENCES , MOST FREQUENT WORDS 

    # 1) CHARCATERS : not counting tab, space, newline as character 
    char_count=0
    for i in text :
        if i=="\n" or i=="\t" or i==" ":
            continue
        char_count+=1

    print(f'character count is {char_count}')

    #2) WORDS : comination of letters 
    list_of_words=text.split()
    word_count=0
    for i in list_of_words:
        word_count+=1

    print(f"word count is {word_count}")

    # 3) SENTENCES : AFTER A FULL STOP 
    list_of_sentences=text.split(".")
    sentence_count=0
    for i in list_of_sentences:
        if i.strip() != "":
            sentence_count+=1

    print(f"sentence count is {sentence_count}")

    # # 4) Most frequent words : retrieving kth most frequent word
    # word_frequency={} # dictionary to store each word frequency
    # for word in list_of_words:
    #     word_frequency[word]=text.count(word) 

    # #sort the dictionary - desceasing order of word frequency
    # sorted_word_frequency=dict(sorted(word_frequency.items(),key=lambda item: item[1],reverse=True))

    # k=int(input("Enter no of most frequent words you want "))
    # for j in sorted_word_frequency:
    #     k+=1
    #     if(k==2):
    #         break
    #     print(f"{j} frequency is : {sorted_word_frequency[j]}")
            

    