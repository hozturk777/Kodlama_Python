#Define
def Operation():
    print("1 - Öğrenci Ekle")
    print("2 - Birden Fazla Öğrenci Ekle")
    print("3 - Öğrencileri Listele")
    print("4 - Öğrenci Numaraları")
    print("5 - Öğrenci Sil")
    print("6 - Birden Fazla Öğrenci Sil")
    print("7 - Çıkış")
    inp = int(input())

    if inp == 1:
        return 1
    elif inp == 2:
        return 2
    elif inp == 3:
        return 3 
    elif inp == 4:
        return 4 
    elif inp == 5:
        return 5
    elif inp == 6:
        return 6
    elif inp == 7:
        return 7
    
def AddMultiple():
    students = []
    print("Kaç Adet Öğrenci Ekleyeceksiniz ?")
    val = int(input())
    for i in range(val):
        print(i + 1,". Öğrenciyi Giriniz")
        students.append(input())
        i += 1
    return students

def StudentNum():
    print("\n")
    for i in range(len(student)):
        std = str(student[i])
        print(f"Öğrenci: {student[i]} \t Numarası: {student.index(std)}")
    print("\n")

def DeleteMultiple():
    deleted = []
    print("\n")
    i = 0
    while i < len(student):
        std = str(student[i])
        print(f"Öğrenci: {student[i]} \t Numarası: {student.index(std)}")
        i += 1
    print("Kaç Adet Öğrenci Sileceksiniz ?")

    dltValue = int(input()) 
    i = 0
    while i < dltValue:
        print(f"{i + 1}. Öğrenciyi Silmek İçin Numarasını Giriniz")
        dlt = int(input())
        j = True
        while j == True:
            if dlt < len(student):
                std = str(student[dlt])            
                if dlt == student.index(std):
                    student.pop(dlt)
                    break
            else:
                print("Öyle Bir Öğrenci Yok")
                break
        j = True
        i += 1


    print("\n")

    
    


student = []

while True:
    print("Lüfen Yapmak İstediğiniz İşlemi Seçiniz")
    operation = int(Operation())


    
    #Add
    if operation == 1:
        student.append(input("Lütfen Eklemek İstediğiniz Öğrenci Adı Soyadı Giriniz : "))
        if True:
            print("\nÖğrenci Eklendi\n")
 


    #Add multiple
    elif operation == 2:
        students = [AddMultiple()]
        for i in range(len(students)):
            add = students[i]
            student.extend(add)
            i += 1
        print(student)
    
    #List Student
    elif operation == 3:
        print("\n")
        for i in range(len(student)):
            print(f"{i + 1}. Öğrenci = ",student[i])
            i += 1
        print("\n")


    #Student Number
    elif operation == 4:
        StudentNum()
    

    #Delete matching value
    elif operation == 5:
        print("Silmek İstediğin Öğrencinin İsim Ve Soyismini Giriniz")
        for i in range(len(student)):
            print("\t\t", i, ".", student[i])
            i += 1

        rmv = input()
        print("\n")
        for x in range(len(student)):      
            if rmv == student[x]:
                student.pop(x)
                print("Silme İşlemi Başarılı\n")
                break
            elif rmv != student:
                print("Lütfen geçerli isim giriniz")
            x += 1

    #Delete multiple value
    elif operation == 6:
        DeleteMultiple()

    #finish
    elif operation == 7:
        break




