def count_upper_lower_case_characters(input_string):
    upper_characters=0
    lower_characters=0
    for character in input_string:
        if character.isupper():
         upper_characters+=1
        elif character.islower():
         lower_characters+=1
    return upper_characters,lower_characters



input_string=input('enter a string:')
upper_characters,lower_characters=count_upper_lower_case_characters(input_string)
print(f"number of upper is{upper_characters}")
print(f"number of upper is{lower_characters}")




