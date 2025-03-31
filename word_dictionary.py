  # having a python dictonary that has a value pair that represents a word and it's definition
def main():
    word_dic = {
          'hi':'a way of greeting',
          'eyes' : 'an organ to see',
          'earch': 'a planet in space',
          }
    while True:
        word = input("Enter a word")
        if word =="":
            break
        if word in word_dic:
            print( word, ":", word_dic[word] )
                  
main()