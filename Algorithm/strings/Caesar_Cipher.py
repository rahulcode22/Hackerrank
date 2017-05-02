n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
#final_string=''.join(map(lambda x: chr(ord(x)+k),s))
#print final_string

def shift_position(shift, letter):
    if shift > 90 and letter.isupper():
        shift -= 26
    elif shift > 122 and letter.islower():
        shift -= 26
    return shift


def encrypt(s, k):

    s = map(
        lambda x: chr(
            shift_position(ord(x) + k % 26, x)) if x.isalpha() else x, s)
    return ''.join(s)

print (encrypt(s, k))
