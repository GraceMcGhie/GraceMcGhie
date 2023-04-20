print ("hello there hooman")
repeat = True
while repeat == True:
    name = input("What is your name?")
    if name == 'Grace':
        print ("I like you")
    else: print ('I dislike you')
    lies = input ('Are you sure this is your name?')
    if lies == 'yes':
        repeat = False
    elif lies == 'no':
        repeat = True
    else:
        lies = input ("I wasn't listening so guess what you have to say your name again :)")
        repeat = True
