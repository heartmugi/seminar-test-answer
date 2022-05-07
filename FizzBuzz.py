for num in range(1, 101):
    string = ''

    # ここから記述

    # numが15の倍数のとき => "FizzBuzz"
    if num % 15 == 0:
        string += "FizzBuzz"
    # numが3の倍数のとき => "Fizz"
    elif num % 3 == 0:
        string += "Fizz"
    # numが5の倍数のとき => "Buzz"
    elif num % 5 == 0:
        string += "Buzz"
    # それ以外のとき => num
    else:
        string += str(num)

    # ここまで記述

    print(string)