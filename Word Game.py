import random

def shuffleWorld(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)

def printPuzzleQuestion(word,score):
    problemWord=shuffleWorld(word)
    print("\nArrange the letters to form a valid word")
    print(problemWord)
    userWord=input()
    print()
    if userWord.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score

def main():
    score=0
    words=["FATHER","BREAK","COUNTRY"]
    words=random.sample(words,k=len(words))

    for word in words:
        score=printPuzzleQuestion(word,score)


    print("Your Score is", score)
    print()

main()