# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:32:45 2019
E --> E+T | E-T | T
T--> n
----------------
E --> TE'
E' --> +TE'| e
E' --> -TE'| e
T -->n

@author: 1271
b, ab, aab, aaab, aaaab, .....
"""
import re
counter=0
#string = input("Enter a string    ")
StringOfcharacters = "ab-b-aaab+aab-+aaaab;"
lexeme=[]
lexemes=[]; operators=[]
for i in range (0, len(StringOfcharacters)):
    scan=StringOfcharacters[i]
    lexeme.append(StringOfcharacters[i])
    if StringOfcharacters[i]=='-' or StringOfcharacters[i]=='+'or StringOfcharacters[i]==' 'or StringOfcharacters[i]==';':
        lexemes.append(lexeme); lexeme=[]

for i in range (0, len(lexemes)):
    for j in range (0, len(lexemes[i])):
        if j==len(lexemes[i])-1:
            operators.append(lexemes[i][j])
            del lexemes[i][j]
lexemes = [i for i in lexemes if i]
temp=0; print("Checking for Lexical Errors if any .... ")
for a in range(0, len(lexemes)):
        string=lexemes[a];s=1;
        for i in range (0, len(string)):
            if s==1 and string[i]=='a':
                s=2; 
            elif  s==1 and string[i]=='b':
                    s=3
            elif s==2 and string[i]== 'a':
                    s=2; 
            elif s==2 and string[i] =='b':
                s=3;
            elif  (string[i] != 'a' or string[i] !='b'):
                s=4
        if s!=3:
            print("Error: Invalid Token", ''.join(string))
            temp=+1
def Term(E):
    global counter; 
    #if counter <=len(E):
    if E[counter]=='n':
        counter=counter+1;
        print("n")
    else:
        print("Error: n expected after operator")
    Endmark(E)
def Endmark(E):
    global counter
    if counter == len(E)-1:
        Endmarks(E)
    elif counter<len(E):
            if (E[counter]=='+' or E[counter]=='-'):
                Endmarke(E);
    else:
        print("Error: end with Semicolon \";\"")
def Endmarks(E):
    global counter
    if E[counter]==';':
        print("Ended with Semicolon");
def Endmarke(E):
    global counter;
def ExprDashplus(E):
    global counter; counter=counter+1;print("+ ");Term(E); ExprDash(E)
def ExprDash(E):
    global counter; 
    if counter < len(E):
        #print(counter, len(E))
        if E[counter]=='+':
            ExprDashplus(E);
        elif E[counter]=='-':
            ExprDashminus(E);
    elif counter==len(E):
        ExprDashe(E)
def ExprDashminus(E):
    global counter; counter=counter+1;print("-");Term(E); ExprDash(E)
def ExprDashe(E):
    global counter; #counter=counter+1; Term(E); 
def Expr(E):
    Term(E);ExprDash(E)
if temp !=0:
    print("Please rectify Lexcial Errors First")
    """
E --> TE'
E' --> +TE'|-TE'| e
T -->nF
F -->;|e
            """
else:
    print("All Tokens are valid ... \nNow scanning Syntax")
    StringOfTokens = re.sub('[\s]', '', StringOfcharacters)
    Operators = ['+', '-', ';']
    E=(re.sub(r'\b\w+\b', lambda x: x.group() if x.group() in Operators else 'n', StringOfTokens))
    print("Expression is of the form: ", E)
if E[counter]=='n':
    Expr(E);
else:
    print("Error: can't start with an operator or semicolon");
    """
                         PARSING TABLE
                         
       |     n      |       +     |      -      |      ;     |      $     
    ___|____________|_____________|_____________|____________|____________
    E  | E --> TE'  |             |             |            |
    E' |            | E' --> +TE' | E' --> -TE' |            | E' --> e
    T  | T --> nF   |             |             |            |
    F  |            |  F --> e    |  F --> e    | F --> ;    | F --> e
    """



#while counter<len(StringOfTokens)-1:


     
    #Expr(E)
  

