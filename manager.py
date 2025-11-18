from storage import load_results,save_results

class ToDoManager:
    def add_todo(self,id,name,task,date):
        data = load_results()
        data.append({
            "id":id,
            "name":name,
            "task":task,
            "date":date
        })
        save_results(data)
        print("Vazifa saqlandi")


    def show_all(self):
        data = load_results()
        if not data:
            print("Hozircha hech narsa yoq")
            return
        for item in data:
            print(f"{item['id']} ---> {item["name"]} ---> {item["task"]} --->{item["date"]}") 

    def delete(self):
        data = load_results()
        ochirish = input("Task ID kiriting: ")
        
        for item in data:
            if str(item['id']) == ochirish:
                data.remove(item)
                print(f"✅ ID {ochirish} bo'lgan task o'chirildi!")
                save_results(data)  # o‘chirilgan ma’lumotni saqlab qo‘yish
                break
        else:
            print("❌ O‘chirish uchun ID topilmadi.")

    def search(self):
        data = load_results()
        qidirish = input("Task ID kiriting: ")
        
        for item in data:
            if str(item['id']) == qidirish:
                print(f"{item['id']} ---> {item["name"]} ---> {item["task"]} --->{item["date"]}")
                print(f"✅ ID {qidirish} bo'lgan task topildi!")
                save_results(data)
                break
        else:
            print("❌ Qidiruv uchun ID topilmadi.")        