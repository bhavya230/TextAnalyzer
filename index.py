#taking a textfile  as input 
with open("text.txt") as file :
    text= file.read().lower()
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

    # unique words count 
    unique_words=set()
    for word in list_of_words:
        word=word.strip(",.")

        if word!= "":
            unique_words.add(word)
    print(f"unique word count is : {len(unique_words)}")

    # 3) SENTENCES : AFTER A FULL STOP 
    list_of_sentences=text.split(".")
    sentence_count=0
    for i in list_of_sentences:
        if i.strip() != "":
            sentence_count+=1

    print(f"sentence count is {sentence_count}")

    # 4) Most frequent words : retrieving kth most frequent word
    words_frequency={}

    #stopwords set 
    stopwords = {
    "the","is","am","are","was","were","and","or","but",
    "to","of","in","on","for","with","as","by","from",
    "that","this","it","an","a"
}

    for word in list_of_words:
        word=word.strip(".,")
        if word in stopwords:
            continue # skip stop words
        if word in words_frequency:
            words_frequency[word]+=1
        else:
            words_frequency[word]=1
    
    #SORT BY FREQUENCY
    sorted_word_frequency=sorted(words_frequency.items(),key=lambda item: item[1], reverse=True)
    

    k=int(input("enter number of most frequent words : "))

    print("\nMost Frequent Words: ")

    for i in range(k):
        print(sorted_word_frequency[i][0],":", sorted_word_frequency[i][1])

    file.close()
    