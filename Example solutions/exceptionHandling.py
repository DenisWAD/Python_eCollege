def div(x , y) :
    try :
        print(f"Calculating {x} / {y}")
        z = x / y
    except BaseException as err :
        print(f"Error occured." )
        print(repr(err))
    else :
        print(f"The function was successful. Result is {z}")

    finally :
        print("This will print either way")


div(10 , 2)