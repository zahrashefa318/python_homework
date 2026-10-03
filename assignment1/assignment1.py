# Task 1: Hello
def hello():
    return "Hello!"
#-------------------------------------------------------------------------------------------------

#Task 2: Greet with a Formatted String
def greet(name):
    return f'Hello, {name}!'
#--------------------------------------------------------------------------------------------------

#Task 3: Calculator
def calc(number1=None,number2=None,operator="Multiply"):
    try:
        if number1 is None or number2 is None or operator is None:
            raise ValueError("First number, second number and the operator is required.")
        if not isinstance(number1,(int,float)) or not isinstance(number2,(int,float)):
            return f"You can't {operator} those values!"
        operator=operator.lower()
        if operator == "multiply":
            return number1 * number2
        elif operator == "add":
            return number1 + number2
        elif operator == "divide":
            if number2 == 0:
                return"You can't divide by 0!"
            return number1 / number2
        elif operator == "subtract":
            return number1 - number2
        elif operator == "modulo":
            if number2 == 0:
                raise ZeroDivisionError("You can't divide by 0!")
            return number1 % number2
        elif operator =="int_divide":
            if number2 == 0:
                raise ZeroDivisionError("You can't divide by 0!")
            return number1 // number2
        elif operator == "power":
            return number1 ** number2
        else:
            return "Allowed operators in this function: Divide,Subtract,Multiply,Add,Modulo,Int_divide,Power"
    except ValueError:
        raise
    except ZeroDivisionError:
        raise
    
#--------------------------------------------------------------------------------------------------

#Task 4: Data Type Conversion
def data_type_conversion(value=None,target_type=None):
    try:
        if value is None or target_type is None:
            raise ValueError("There are two arguments required: value and target type")
        if target_type not in ["str","int","float"]:
            raise AttributeError(f"{target_type} is not in['int','sting','float'].")
        target_type=target_type.lower()
         
        if target_type =="float":
            value2=float(value)
            return value2
        elif target_type =="int":
            value2= int(value)
            return value2
        elif target_type =="str":
            value2= str(value)
            return value2
        else:
           return "The value should be number(integer or float) and the target type should be string,int,and float."
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
    except AttributeError:
        raise
    
         


#Task 5: Grading System, Using *args --------------------------------------------------------------
def grade(*args):
    try:
        if not all(isinstance(score,(int,float))for score in args):
            raise ValueError("Invalid data was provided.")
        total=0
        average=0
        grade=""
        for score in args:
            total += score
        if len(args) == 0:
            raise ZeroDivisionError("Zero score")
        average= total/len(args)
        if average in range(90,101):
            grade="A"
        elif average in range(80,89):
            grade="B"
        elif average in range(70,79):
            grade="C"
        elif average in range(60,69):
            grade="D"
        elif average < 60:
            grade="F"
        else:
            return"Not standard records"
        return grade
    except ValueError:
        return "Invalid data was provided."
    except ZeroDivisionError:
        raise


#Task 6: Use a For Loop with a Range---------------------------------------------------------------
def repeat(word=None,count=None):
    try:
        if word is None or count is None:
            raise TypeError("Two arguments required: word and count")
        if not isinstance(count,int):
            raise TypeError("The count of loop should be an integer")
        repeated_words=""
        for _ in range(count):
            repeated_words +=word

        return repeated_words

    except TypeError:
        raise


            
#Task 7: Student Scores, Using **kwargs -----------------------------------------------------------
def student_scores(meanOrbest,**student_score):
    try:
        for key,val in student_score.items():
            if not isinstance(key,str) or not isinstance(val,(int,float)):
                raise TypeError("The key should be string and the value should be integer or float.")
        if not isinstance(meanOrbest,str):
            raise TypeError("The first argument should be a string.")
        meanOrbest=meanOrbest.lower()
        if meanOrbest not in ["mean","best"]:
            raise ValueError("Enter mean or best.")
        if meanOrbest == "mean":
            total=0
            average=0

            for key,val in student_score.items():
                total += val

            average=total/len(student_score)
            return average
        elif meanOrbest == "best":
            max_value=0
            for key,val in student_score.items():
                if val > max_value:
                    max_value=val
            for key,value in student_score.items():
                if value == max_value:
                   return key
    except TypeError:
        raise
    except ValueError:
        raise


#Task 8: Titleize, with String and List Operations ------------------------------------------------
def titleize(some_string):
    try:
        words=some_string.split()
        capitalized_words=[]
        small_words=["a", "on", "an", "the", "of", "and", "is","in"]

        capitalized_words.append(words[0].capitalize()) #First word

        for word in words[1:-1]:                         #Middle words
            if word not in small_words:
                capitalized_words.append(word.capitalize())
            else:
                capitalized_words.append(word)

        capitalized_words.append(words[-1].capitalize())  #Last word

        return " ".join(capitalized_words) 
    
    except Exception:
        raise


#Hangman, with more String Operations ------------------------------------------------------------
def hangman(secret,guess):
    try:
        if not isinstance(secret,str) or not isinstance(guess,str):
            raise TypeError("The secret and guess should be string")
        secret=secret.lower()
        guess=guess.lower()
        answer=[]
        for s in secret:
            if s in guess:
                answer.append(s)
            else:
                answer.append("_")
        return "".join(answer)
    except TypeError:
        raise


#Task 10: Pig Latin, Another String Manipulation Exercise------------------------------------------
def pig_latin(word):
    try:
        splited_sentence=word.split()
        latin_sentence=[]
        vowels=['a','e','i','o','u']
        
        for w in splited_sentence:
            splitted_word=list(w)
            first_consonents_in_word=[]
            previous_letter=""
            if splitted_word[0] in vowels:
                return w + "ay"
            else:
                for letter in splitted_word:
                    if (letter not in vowels) or (letter =="u" and previous_letter=="q"):
                        previous_letter=letter
                        first_consonents_in_word.append(letter)
                        
                    else:
                        break
        
                    
            consonent_count=len(first_consonents_in_word)       
            result=splitted_word[consonent_count:] + first_consonents_in_word
            result="".join(result) + "ay"
            latin_sentence.append(result)

        return " ".join(latin_sentence)
    except Exception:
        raise



                    

            




                
                
            


        




        
        