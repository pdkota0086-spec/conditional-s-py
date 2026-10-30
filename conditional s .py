homeworktime = int(input("enter today's homework time :"))
freetime = int(input("enter today's freetime :"))
play = int(input("enter today's ply time :"))

if homeworktime < freetime  :
    print("you can easily do your homework in freetime!")
elif freetime < play :
    print("do your work")

else:
    print("give extra time to do your homwork!")    