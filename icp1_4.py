#Author : Ram Gopal Lokam
#block4
def grading():
    try:
        try:
            class_score = int(input("Enter your score here:"))
        except ValueError:
            print ("Please enter only number not strings")
            return None
        if class_score != '' and class_score is not None:
            if class_score > 100 or class_score < 0:
                print("Score not in range please enter a valid score")
            else:
                if class_score >= 90 and class_score <= 100: #Grade A score range
                    print("A")
                elif class_score >= 80 and class_score <= 89: #Grade B score range
                    print("B")
                elif class_score >= 70 and class_score <= 79: #Grade C score range
                    print("c")
                elif class_score >= 60 and class_score <= 69: #Grade D score range
                    print("D")
                else:
                    print("F") #Grade F score range
            
        else:
            print("please enter a valid number")
    except Exception as error:
        print("Error occured {}".format(error)) 
#end of block4
if __name__ == "__main__":
    grading()