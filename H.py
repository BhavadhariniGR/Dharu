s=input()
if((s>='a' and s<='z') or (s>='A' and s<='Z')):
  if(s== 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A'
       or s == 'E' or s == 'I' or s == 'O' or s == 'U'):
       print("Vowel")
  else:
       print("Consonant")
else:
  print("invalid")
