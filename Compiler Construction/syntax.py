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
StringOfcharacters = "ab=+ba "
lexeme=[]
lexemes=[]; operators=[]
for i in range (0, len(StringOfcharacters)):
    scan=StringOfcharacters[i]
    lexeme.append(StringOfcharacters[i])
    if StringOfcharacters[i]=='-' or StringOfcharacters[i]=='+'or StringOfcharacters[i]==' ':
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
            print("Invalid Token", ''.join(string))
            temp=+1
if temp !=0:
    print("Please rectify Lexcial Errors First")
    """
E --> TE'
E' --> +TE'| e
E' --> -TE'| e
T -->n
            """
else:
    print("All Tokens are valid ... \nNow scanning Syntax")
    StringOfTokens = re.sub('[\s]', '', StringOfcharacters)
    Operators = ['+', '-']
    E=(re.sub(r'\b\w+\b', lambda x: x.group() if x.group() in Operators else 'n', StringOfTokens))
    print("Expression is of the form: ", E)
    
    def Expr(E):
        Term(E); ExprDash(E);
    def Term(E):
            global counter;
            if E[counter] == 'n':
                counter=counter+1;

            else:
                counter=len(E)+1
    def ExprDash(E):
            global counter;
            if counter<len(E)-1 and (E[counter] == '-' or E[counter] == '+'):
                    counter=counter+1;Term(E); ExprDash(E);
            elif counter==len(E)-1 and (E[counter] == '-' or E[counter] == '+'):
                    print("Can not end with operator")
            elif counter==len(E):
                    print("syntax valid")
            else:
                print("Misuse operator")
                
    Expr(E)
  

