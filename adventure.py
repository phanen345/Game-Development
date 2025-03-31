name = input("Type your Name:")
print("Welcome", name, "to this adventure")
answer = input ('you come to an middle of the Iland  where would you go to swim of or to the top of land').lower()


if answer == 'swim':
    print("your swimmin nice",name,)
    answer= int(input("You got stung by an jelly fish what would you need 1.Ice  2.Medicine  3.soap "))
    if answer== 1:
        print("yes, you are getting betteer for a while")
    elif answer ==2:
        print("yes you survive the death condition")
    elif answer ==3:
        print("ooh ! no you are dead now , game over'")
    else:
        print("Invalid option")
    
elif answer == 'top':
    print ("woo! You made it you can  see the osm view")
    print("you feel down suddenly from top save your self 1.Rope 2.jump 3.scream for help")
    answer= int(input())
    if answer== 1:
        print('yes you made it good choice', name, 'you are safe now')
    elif answer == 2:
        print("you looose dear, better luck next time")
    elif answer== 3:
        print("Noooo,  sooneer you died dear, don't seek anything from other be independent")
    else:
        print("Invalid input")
        
    
else:
    print('Invalid input ')