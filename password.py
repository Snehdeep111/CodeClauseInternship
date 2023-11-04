#this is my first project as an intern at CODECLAUSE 
import random
import string
print('-----I know you are here to generate a random password-----')
print("\n")
def main():

     length=int(input('enter the length of password you want: '))
     lowerD=string.ascii_lowercase
     upperD=string.ascii_uppercase
     digitD=string.digits
     symbolsD=string.punctuation
     combine=lowerD+upperD+digitD+symbolsD
     x=random.sample(combine,length)
     password="".join(x)
     print(password)
     main()

main()
    

