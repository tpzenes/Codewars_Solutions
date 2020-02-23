from collections import Counter
def scramble(s1, s2):
   fc=0
   s1 =Counter(s1)
   s2 =Counter(s2)
   print(s1,s2)
   for i in s2:
       if s2[i] <= s1[i]:
           pass
       else:
           return False
   return True