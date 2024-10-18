def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in s if char not in vowels)
    return result
input_string = "Hello, World!"
output_string = remove_vowels(input_string)
print(output_string)  
