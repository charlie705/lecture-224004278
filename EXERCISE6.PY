def number_to_words(n):
    if n == 0:
        return "zero"
    
    units = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    thousands = [
        "", "thousand", "million", "billion"
    ]

    def words(num):
        if num < 20:
            return units[num]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else units[num % 10])
        elif num < 1000:
            return units[num // 100] + " hundred" + ('' if num % 100 == 0 else ' ' + words(num % 100))
        else:
            for idx, word in enumerate(thousands):
                if num < 1000 ** (idx + 1):
                    return words(num // (1000 ** idx)) + " " + word + ('' if num % (1000 ** idx) == 0 else ' ' + words(num % (1000 ** idx)))

    return words(n).strip()


try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        raise ValueError("The number must be positive.")
    print(number_to_words(num))
except ValueError as e:
    print("Invalid input:", e)
   


    

