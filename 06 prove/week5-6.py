print("You are in the middle of the woods; you are tired and hungry in the distance you see a house")

start =input(" what should I do?-> a)walk to the house  b) climb a tree to view it better---")


if start.lower() == "walk to the house":

    
    a1 =input(" You knock at the door, but nobody answers -> a) open the door b)go to the back of the house---")
    if a1.lower() == "open the door":
        a2 = input("You decide to wait for some minutes just to see -> a)somebody will come   b)will never come--")
        if a2.lower() == "somebody will come":
            print("end of story")

        elif a2.lower()== "will never come":
            print("end of story")

    elif a1.lower() == "go to back of the house":
        a2 = input("Maybe  a) you will find someone b) no one might be there--")
        if a2.lower()== "you will find someone":
            print("end of story")

        elif a2.lower() == "no one might be there":
            print("end of story")


elif start.lower() == "climb a tree to view it better":
    b1=input("Fortunately, somebody lets you come in and ask you -> a) drink tea b)drink caffe ")
    if b1.lower()=="drink tea":
        b2= input("After deciding what to drink-> a): give the reason why you came for b)leave")
        if b2.lower()== "give the reason why you came for":
            print("end of story")

        elif b2.lower() == "leave":
            print("end of the story")

    elif b1.lower()=="drink caffe":
        print("go find your family") 
    


exit=input("press close to exit")
  


