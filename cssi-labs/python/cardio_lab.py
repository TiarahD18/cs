#def count_spaces(s):
    #return s.count(" ")

#print(count_spaces("hello world"))
#print(count_spaces("wow wow wow"))

'''def longest_word(word1,word2,word3):
    word1 = "Hello"
    word2 = "Pie"
    word3 = "PizzaPie" #PizzaPie:

if len(word1) > len(word2) > len(word3):
    print word1
else if len(word2) > len(word1) and len(word2) > len(word3)
    print word2
else
    print word3
longest_word("Hello", "Pie", "PizzaPie")
'''
'''def reverse_string(word1):
    word2= ""
    for x in range(len(word1), 0, -1):
        word2 = word2 + word1[x-1]
        #print x
    return word2
print reverse_string("hello")
'''
'''def sum_to_n(n):
    total = 0
    for i in range(1 , n + 1):
        total = total + i
return total
'''

'''def isTriangle(a, b, c):
    sabc = a + b > c
    sacb = a + c > b
    sbca = b + c > a
if sabc and sacb and sbca:
    return True
else:
    return False
'''

def roll_dice(num):
    total = 0
    for i in range(num):
        total = total +
            random.randint(1,6)
return total
