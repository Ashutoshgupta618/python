import time
list=[]
while True :
  print("your task are -->")
  print("1 for show your list\n" 
  "2 for add into the list \n"
  "3 for delete item as you want \n"
  "4 for good bye or exit "
  )

  a= int(input("enter choice 1-4-->"))

  if (a == 1) :
    if not list :
         print("no task yet")
    else:
        print("yours tasks are -->")
        idx=1

        for idx,task in enumerate(list):
            print(idx+1,"> " ,task)
 
  elif (a == 2) :
     data= input("enter which you wnat to add-->")
     list.append(data)
     print('item added successfully')
 
  elif a==3:
                
    if len(list) == 0:
        print("your list is empty")
                
    else:
        data= int(input("enter position you wnat to remove-->") )
        if( data >= len(list)-1 ):
            print("position not exits")
        else:
            data=data-1
            list.pop(data)

  elif a==4 :
        print("good bye  ")
        break 
  else:
     print("enter a valid no. ")
  time.sleep(0.5)                  

      