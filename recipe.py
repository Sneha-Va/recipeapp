while True:
    print("select an option from the menu")
    print('1 add recipe details')
    print('2 view recipe details')
    print('3 search  recipe details')
    print('4 update recipe details')
    print('5 delete recipe details')
    print('6 exit')
    
    choice=int(input('enter the option:'))
    if(choice==1):
        print("add recipe")
    if(choice==2):
        print("view recipe")
    elif(choice==3):
        print('search recipe')
    elif(choice==4):
        print('update recipe')
    elif(choice==5):
        print('delete recipe')
    elif(choice==6):
        break  