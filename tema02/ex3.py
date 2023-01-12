def function3():
    input_data = input("Enter an element: ")
    try:
        input_data = int(input_data)

    except ValueError:
        return 0
    else:
        return input_data
    finally:
        pass


print(function3())
