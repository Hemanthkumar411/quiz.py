import random
import string

def add_random_letters(s):
    before = ''.join(random.choices(string.ascii_letters, k=3))  
    after = ''.join(random.choices(string.ascii_letters, k=3))  
    return before + '' + ''.join(reversed(s)) + '' + after
    
def remove(s):
        return s[3:-3] 
        
def encoder(text):
    if len(text)<=3:
        enc_text=''.join(reversed(text))
    else:
        enc_text=add_random_letters(text)
    print("encoded text:",enc_text)
    return enc_text
    
def decoder(enc_text):
    if len(enc_text)<=3:
        dec_text=''.join(reversed(enc_text))
    else:
        dec_text=''.join(reversed(enc_text))
        dec_text=remove(dec_text)
    print("decoded text:",dec_text)
text=input("enter the text: ")
enc_text=encoder(text)
dec=input("enter 1 to decode the original text")
match dec:
    case "1": 
        decoder(enc_text)
    case _:
        print("you have no access to the code")
     
        
        
