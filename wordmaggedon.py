#/bin/python3
# Created by Clement Loiselet
import urllib.request

letters = "abcdef"
word_size = 5
word_pattern = "ex_mpl_"

word_list_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

def findWordsByLetters(letters, word_size):
    with urllib.request.urlopen(word_list_url) as response:
        line = response.readline().decode("utf-8").strip().lower()
        while len(line) > 0:
            if len(line) == word_size:
                letters_ok = 0
                for i in letters:
                    if i in line:
                        letters_ok+=1
                if len(letters) >= word_size :
                    #test if the selected word doesn't use more letters
                    for i in line:
                        if line.count(i) > letters.count(i):
                            letters_ok = -1
                            break
                if letters_ok == min(len(letters), word_size):
                    print(line)
            line = response.readline().decode("utf-8").strip().lower()        

def findWordsByPattern(pattern):
    pattern = pattern.lower()
    with urllib.request.urlopen(word_list_url) as response:
        line = response.readline().decode("utf-8").strip().lower()
        while len(line) > 0:
            if len(line) == len(pattern):
                letters_ok = 0
                for i in range(len(pattern)):
                    if pattern[i] == "_" or pattern[i] == line[i]:
                        letters_ok+=1
                if letters_ok == len(pattern):
                    print(line)
            line = response.readline().decode("utf-8").strip().lower()

# usage :
# findWordbyPattern("test___")
# findWordsByLetters("ttes", 4)
