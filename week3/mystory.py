print "\n\nMadLibs Assignment\n\n"
story = '''Baa Baa Black Sheep, have you any {0}'''

print (story.format("wool"))

noun = raw_input("Enter a noun: ")

print (story.format(noun))

story1 = '''Yes sir, yes sir, three bags {0}'''
print (story1.format("full"))
adjective = raw_input("Enter an adjective: ")
print (story1.format(adjective))


story2 = '''One for my master and one for my {0}'''
print story2.format("Dane")
noun = raw_input("Enter a noun: ")
print (story2.format(noun))

story3 = '''One for the little boy who lives down the {0}'''
print (story3.format("Lane"))
noun = raw_input("Enter a noun: ")
print (story3.format(noun))
