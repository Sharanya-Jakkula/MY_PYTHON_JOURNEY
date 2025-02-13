#to check whether the given character is vowel or not 
ch=input("Enter the character  : ")
if((ch<='z' and ch>='a') or (ch<='Z' and ch>='A')):
    if ch in 'aeoiuAEIOU':
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is not a vowel\nIt is a consonant")
else:
    print("Please enter alphabet!!")