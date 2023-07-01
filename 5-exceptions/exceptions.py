

invalid = True
while invalid:
    try:
        number = int(input("Enter a number:"))
        print(10/number)
        invalid = False
    except ValueError:
        print("It is not a number")
        invalid = True
    except ZeroDivisionError:
        print("You can't enter zero")
        invalid = True
    except:
        break
    finally:
        print("no matter what happened; finally, I will occur on your console")