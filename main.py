from utils import checking_user,get_id
from manager import ToDoManager
from datetime import datetime

td = ToDoManager()

checking_user()   

while True:  
    print("""
****  TO DO MANAGER  ****        
    1.Vazifa qo'shish
    2.Vazifalarni ko'rsatish
    3.Vazifa o'chirish
    4.Vazifalarni qidirish 
    5.Chiqish                 
    """)
    choice = input("Tanlov kiriting : ")

    if choice == '1':
        id = get_id()
        name = input("Ismizni kiriting : ")
        task = input("Vazifa kiriting : ")
        sana = datetime.now()
        date = str(sana)
        td.add_todo(id,name,task,date)

    elif choice == '2':
        td.show_all()    
    elif choice == '3':
        td.delete()
    elif choice == '4':
        td.search()    
    elif choice == '5':
        break
    else:
        print("(1-5)-oraliqda son kiriting")

