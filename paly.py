def paly(word):
     dict = {}
     word = word.lower()
     count = 0
     #counting the characters and storing them and their counts in the dict
     for char in word:
         if ord(char) >= 97 and ord(char) <= 122:
             count+=1
             if char not in dict.keys():
                 dict[char] = 1
             elif char in dict.keys():
                 dict[char]+=1
     #if there are even number of characters
     if count%2 == 0:
         for key in dict.keys():
             #if there is an odd count, return false
             if dict[key]%2 != 0:
                 return False
         return True
     #if there are odd number of characters
     else:
         #there can only be 1 pivot character
         pivot = False
         for key in dict.keys():
             if pivot == False and dict[key]%2 != 0:
                 pivot = True
             #if there are more than 1 pivot character return false
             elif pivot == True and dict[key]%2 != 0:
                 return False
         #return true if found only 1 pivot
         return True

def main():
	a = input('Enter a string: ')
	print (paly(a))

if __name__ == "__main__":
	main()
