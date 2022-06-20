from fileinput import close


def open_file() :
    try :
        f = open("filename1.txt")
        print( 1 / 0)
    except FileNotFoundError as err :
        print("Error: unable to find file\n", repr(err))
    except ValueError as err:
        print("Value incorrect: ", repr(err))
    except ZeroDivisionError as err :
        print("Cannot divide by zero", repr(err))
    except IOError as err:
        print("IOError", repr(err))
    else :
        for i in f :
            print(i.strip("\n"))
        close()
    finally :
        print("Finished program")


open_file()

