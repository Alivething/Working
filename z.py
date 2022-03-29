def longestEvenWord(sentence):
    words = sentence.split(" ")
    index = -1
    largest = 0
    
    for word in range(len(words)):    
        length = len(words[word])
        if(length > largest and lenght%2 == 0):
            largest = length
            index = word
        
    longestevenword = words[index]
    return longestevenword

if __name__ == '__main__':