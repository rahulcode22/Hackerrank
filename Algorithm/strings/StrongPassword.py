'''
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length n in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
'''
n = int(raw_input())
password = raw_input()

numbers = set("0123456789")
lower_case = set("abcdefghijklmnopqrstuvwxyz")
upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = set("!@#$%^&*()-+")
passw=set(password)
count=0
if passw.intersection(numbers)== set():
    count+=1
if passw.intersection(lower_case)== set():
    count+=1
if passw.intersection(upper_case)== set():
    count+=1
if passw.intersection(special_characters)== set():
    count+=1

print max(6-len(password),count)
