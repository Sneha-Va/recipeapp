import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='recipedb')
mycursor = mydb.cursor()
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
        recipename=input('enter the recipename:')
        preparedby=input("enter preparedby:")
        ingredients=input('enter ingredients:')
        price=input("enter price:")
        sql='INSERT INTO `recipe`(`recipename`, `preparedby`, `ingredients`, `price`) VALUES (%s,%s,%s,%s)'
        data=(recipename,preparedby,ingredients,price)
        mycursor.execute(sql,data)
        mydb.commit()
        print("euccessfilly added")
    if(choice==2):
        print("view recipe")
        print("view blooddonor")
        sql='SELECT * FROM `recipe`' 
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search recipe')
        recipename=input("enter recipe :")
        sql="SELECT `id`, `recipename`, `preparedby`, `ingredients`, `price` FROM `recipe` WHERE `recipename`='"+recipename+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update recipe')
    elif(choice==5):
        print('delete recipe')
        recipename=input("enter recipename:")
        sql="DELETE FROM `recipe` WHERE `recipename`='"+recipename+"'"
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==6):
        break  