
import random,time
#allows the user to choose their difficulty
def Menu():
    global none #makes the variable global so that it can be used in other functions
    none = '' #a blank variable
    print ('***********************')#-
    print ('*Press 1 for Easy Mode*')#--
    print ('***********************')#--- displays the menu 
    print ('*Press 2 for Hard Mode*')#--
    print ('***********************')#-
    menuAnswer = input ('Make your choice:') 
    theWords = []
    if menuAnswer == '1':
        print ('Easy Mode:')
        print ('(-(-(-(-_-)-)-)-)')
        print (EasyMode(theWords))

    elif menuAnswer == '2':
        print ('Hard Mode:')
        print ('(-(-(-(-(-(-(-_-)-)-)-)-)-)-)')
        print (HardMode(theWords))
            

    else:
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('Invalid Answer')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return Menu()

#loads the file with 10 words (easy file)
def EasyMode(theWords):
    openFile = open ('Words.txt','r')
    for word in openFile:
        word = word.replace ('\n', '')
        theWords.append(word)
    openFile.close
    return subWord(theWords)

#loads the file with 17 words (hard file)   
def HardMode(theWords):
    openFile = open ('WordsExt.txt','r')
    for word in openFile:
        word = word.replace ('\n', '')
        theWords.append(word)
    openFile.close
    return repWord(theWords)

#making a grid for easy mode    
def subWord(theWords):
        global theSubWord
        newWords = theWords
        random.shuffle(newWords)
        #removes a random word from the 10 letter list and appends that word to a list
        theSubWord = []
        chosenWord = random.choice(newWords)
        theSubWord.append (chosenWord)
        newWords.remove (chosenWord)
        #display the 9 words into a grid
        print (EasyGrid(newWords))
        #displays the grid for 30 seconds
        time.sleep(30)
        print (Change())

        #replaces a random word with the removed word from before 
        theRemWord = []
        random.shuffle (newWords)
        chosenWord2 = random.choice (newWords)
        theRemWord.append(chosenWord2)
        newWords.remove (chosenWord2)
        newWords.append(theSubWord[0])
        random.shuffle (newWords)
        print (EasyGrid(newWords))
        return remQuestions(theRemWord)

#making a hard for easy mode
def repWord(theWords):
        global theSubWord
        newWords = theWords
        random.shuffle(newWords)
        #removes a random word from the 10 letter list and appends that word to a list
        theSubWord = []
        chosenWord = random.choice(newWords)
        theSubWord.append (chosenWord)
        newWords.remove (chosenWord)
        #display the 16 words into a grid
        print (HardGrid(newWords))
        #displays the grid for 30 seconds
        time.sleep(40)
        print (Change())

        #replaces a random word with the removed word from before 
        theRemWord = []
        random.shuffle (newWords)
        chosenWord2 = random.choice (newWords)
        theRemWord.append(chosenWord2)
        newWords.remove (chosenWord2)
        newWords.append(theSubWord[0])
        random.shuffle (newWords)
        print (HardGrid(newWords))
        return remQuestions(theRemWord)

#creates the grid for easy mode 
def EasyGrid(newWords):
    grid = [newWords[i:i + 3]for i in range(0,len(newWords),3)]
    for a,b,c in grid:
        print ('|'+ a,'|'+ b,'|' + c +'|')
    return none
#creates the grid for hard mode
def HardGrid(newWords):
    grid = [newWords[i:i + 4]for i in range(0,len(newWords),4)]
    for a,b,c,d in grid:
        print ('|'+a, '|'+ b,'|'+c,'|'+ d +'|')
    return none
    

#print out lines so that the user doesn't cheat and scroll up
def Change():
    for x in range(100):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return none

#asks the user for the REMOVED word and tells them they lose if they guessed wrong 3 times or they have guessed it correctly
def remQuestions(theRemWord):
    print ('---------------------------------------------------------------------')
    attempts = 0
    while attempts < 3:
        remAnswer = input ('What was the word that has been REMOVED onto the grid? : ')
        attempts = attempts + 1
        if remAnswer == theRemWord[0] or remAnswer == theRemWord[0].lower():
            print ('You have guessed the correct word')
            return subQuestions(theSubWord)
        else:
            print ('You have guessed the word incorrectly!')
    if attempts == 3:
        gameOver = ('You have guessed the word incorrectly 3 times. THE GAME IS OVER!')
        return gameOver
    else:
        pass


#asks the user for the REMOVED word and tells them they lose if they guessed wrong 3 times or they have guessed it correctly
def subQuestions(theSubWord):
    attempts = 0
    while attempts < 3:
        subAnswer = input ('What was the word that has been ADDED onto the grid? : ')
        attempts = attempts + 1
        if subAnswer == theSubWord[0] or subAnswer == theSubWord[0].lower():
            print ('You have guessed the correct word')
            print ('---------------------------------------------------------------------')
            #they win if they guessed both correctly
            print ('You have guessed BOTH words correctly. YOU WIN THE GAME!')
            return none
        else:
            print ('You have guessed the word incorrectly!')
    if attempts == 3:
        gameOver = ('You have guessed the word incorrectly 3 times. THE GAME IS OVER!')
        return gameOver
    else:
        pass

        

#main program
Menu()

    
    
    
