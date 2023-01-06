import time
import sys
score=0
print("welcome to your weekly test")
time.sleep(1)
question_one = input("what is 100+100")
if  question_one == "200":
    print("correct")
    print("+2")
    score = score + 2

elif question_one== "199" or question_one== "198" or question_one== "197" or question_one== "201" or question_one== "202" or question_one== "203":
    print("almost there")
    print("+1")
    score = score + 1
else:
     print("wrong loser")
     print("-1")
     score = score - 1

question_two =  input("what is the best team in the epl")
time.sleep(1)
if question_two == "man city":
    print("correct")
    print("+2")
    score = score + 2

elif question_two== "chelsea" or question_two== "liverpool" or question_two== "manchester united" or question_two== "manchester city" or question_two== "tottenham":
    print("almost there")
    print("+1")
    score = score + 1
else:
    print("wrong")
    print("-1")
    score = score - 1

question_three =  input("what is the best subject")
time.sleep(1)
if question_three == "computer science":
    print("correct")
    print("+2")
    score = score + 2

elif question_three== "food" or question_three== "physics" or question_three== "d and t":
    print("almost there")
    print("+1")
    score = score + 1
else:
    print("wrong")
    print("-1")
    score = score - 1

print ("your score is-",int( score/6*100),"%")

