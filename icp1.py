#Author : Ram Gopal Lokam
#block1
def string_op():
    try:
        inp_a = str(input("Enter your string here:"))
        if inp_a != '' and inp_a is not None and inp_a.isspace() != True and inp_a.isnumeric() != True:
            output = inp_a[:-2]
            output = output[::-1] #reversal of the string after truncating
            print(output)
            #end of block1
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))
#end of block1
if __name__ == "__main__":
    string_op()

