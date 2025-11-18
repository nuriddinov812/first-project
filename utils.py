from storage import user_results,load_results


def checking_user():
    while True:
        data = user_results()
        username = input("Username kiriting: ")
        password = input("Parol kiriting: ")
        for i in data:
            if i["username"] == username and i["password"] == password:
                print(f"Xush kelibsiz, {username.capitalize()}!")
                return
        
        print("Foydalanuvchi topilmadi")                                             


def get_id():
    data = load_results()
    if not data :
        return 1
    id = 0
    for  item in data :
         if 'id' in item and isinstance(item['id'], int):
            id = max(id, item['id'])
    return id + 1