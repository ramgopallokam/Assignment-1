#Author : Ram Gopal Lokam
#block3
def str_op():
    try:
        input_str = input("Enter your sentence here:")
        if input_str != '' and input_str is not None and input_str.isspace() != True and input_str.isnumeric() != True: 
            input_str = input_str.replace('python','pythons')
            print(input_str)
        else:
            print("please enter a valid sentence")
    except Exception as error:
        print("Error occured {}".format(error))
#end of block3
if __name__ == "__main__":
    str_op()