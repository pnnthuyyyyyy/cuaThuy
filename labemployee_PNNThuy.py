'''
Khai báo đối tượng Employee có: 
Các thuộc tính (fields, states) sau
- mã số (code)
- tên (name)
- tuổi (age)
- lương (salary)
Các phương thức (behaviors, methods)
- Tổng thu nhập hằng năm sau thuế (income) biết rằng tax = 10%
- In ra thông tin của nhân viên (display)
- Tăng lương cho nhân viên (increaseSalary), biết rằng số lương tăng phải lớn hơn 0
- (Sinh viên tự viết) Giảm lương cho nhân viên (decreaseSalary), biết rằng số lương giảm phải lớn hơn 0 và không vượt quá 20% lương hiện tại
============= YÊU CẦU CHƯƠNG TRÌNH==============
Khai báo biến danh sách (list) nhân viên (dsNhanVien) để lưu trữ các nhân viên và viết chương trình menu thực hiện các chức năng bên dưới 
- Opt-1: Tải danh sách nhân viên từ file dbemp_input.db
- Opt-2: Thêm nhân viên vào danh sách
- Opt-3: Hiển thị danh sách nhân viên
- Opt-4: Hiển thị thông tin của một nhân viên khi biết mã nhân viên
- Opt-5: Chỉnh sửa thông tin một nhân viên
- Opt-6: Xóa một nhân viên ra khỏi danh sách
- Opt-7: Tăng lương cho một nhân viên
- Opt-8: Giảm lương cho một nhân viên
- Opt-9: Tính số lượng nhân viên (countEmp) và xuất ra màn hình
- Opt-10: Tính tổng tiền lương của công ty phải trả hàng tháng (sumSalary) và xuất ra màn hình
- Opt-11: Tính trung bình lương của nhân viên (avgSalary) và xuất ra màn hình
- Opt-12: Tính độ tuổi trung bình của nhân viên (avgAge) và xuất ra màn hình
- Opt-13: Tính tuổi lớn nhất của các nhân viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
- Opt-14: Sắp xếp danh sách nhân viên tăng dần theo lương
- Opt-15: Vẽ biểu đồ tương quan lương theo độ tuổi
- Opt-16: Vẽ biểu đồ so sánh lương trung bình của các nhóm tuổi: nhỏ hơn 35, từ 35 đến 50, hơn 50 trở lên
- Opt-17: Vẽ biểu đồ thể hiện phần trăm tổng lương trên các nhóm tuổi như Opt-16
- Opt-18: Vẽ biểu đồ thể hiện phần trăm số lượng nhân viên theo các nhóm tuổi như Opt-16 
- Opt-19: Lưu danh sách nhân viên xuống file dbemp_output.db, biết rằng mỗi nhân viên là một dòng và các thông tin nhân viên được phân cách bởi dấu '-'
- Opt-Khác: Thoát chương trình
'''
from audioop import avg
from statistics import mean
from turtle import bye, color
import matplotlib.pyplot as plt
import Employee as emp
import array as arr

menu_options = {
    1:'Load data from file',
    2:'Add new employee',
    3:'Display list of employee',
    4:'Show employee details',
    5:'Update employee information',
    6:'Delete employee',
    7:'Increase salary of employee',
    8:'Decrease salary of employee',
    9:'Show total employee a month',
    10:'Show total salary a month',
    11:'Show average of salary a month',
    12:'Show average of age',
    13:'Show maximum age',
    14:'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16:'Draw average of salary chart by age group',
    17:'Draw percentage of salary by age group',
    18:'Draw percentage of total employee by age group',
    19:'Store data to file',
    'Others': 'Exit program'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Khai báo biến lưu trữ những nhân viên
dsNhanVien = []

while(True):
        print_menu()
        userChoice = ''
        try:
            userChoice = int(input('Input choice: '))
        except:
            print('Invalid input, try again')
            continue
        #Check what choice was entered and act accordingly
        if userChoice == 1:
            fr = open('dbemp_input.db',mode='r',encoding='utf-8')
            for line in fr:
                stripLine = line.strip('\n')
                ds = stripLine.split(',')
                maso = ds[0]
                ten = ds[1]
                tuoi = int(ds[2])
                luong = float(ds[3])
                nv = emp.Employee(maso,ten,tuoi,luong)
                dsNhanVien.append(nv)
            fr.close()
        #Thêm 1 nhân viên
        elif userChoice == 2:
           maso = input("Input code: ")
           ten = input("Input name: ")
           tuoi = int(input("Input age: "))
           luong = float(input("Input salary: "))
           nv = emp.Employee(maso,ten,tuoi,luong)
           dsNhanVien.append(nv)
        elif userChoice == 3:
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                for item in dsNhanVien:
                    item.display()
        elif userChoice == 4:
        #4:Show employee details
            maso = input("Input code: ")
            flag = 0
            for item in dsNhanVien:
                if (item.code == maso):
                    flag = 1
                    item.display()
            if flag == 0: print("Nothing here")
        #5:Update employee information
        elif userChoice == 5:
            maso = input("Input code: ")
            flag = 0
            for item in dsNhanVien:
                if (item.code == maso):
                    flag = 1
                    ten = input("Input name: ")
                    tuoi = int(input("Input age: "))
                    luong = float(input("Input salary: "))
                    item.code = maso
                    item.name = ten
                    item.age = tuoi
                    item.salary = luong
            if flag == 0: print("Nothing here")
            # if dsNhanVien.count==0:
            #     print('Danh sach rong')
            # else:
            #     ma =input("Input Code for Update:")
            #     for item in dsNhanVien:
            #         if(item.code ==ma):
            #             item.display()
            #             menu={
            #                 1:'1-Update Name',
            #                 2:'2-Update Age',
            #                 3:'3-Update luong',
            #                 'Others':'Thoat'
            #             }
            #             def Xuat_menu():
            #                 for key in menu.keys():
            #                     print(key,'--',menu[key])
            #             while (True):
            #                 Xuat_menu()
            #                 traloi=''
            #                 try:
            #                     traloi =int(input('Nhap cac tuy chon:'))
            #                 except:
            #                     print('Nhap sai dinh dang, nhap lai:')
            #                     continue
            #                 if traloi==1:
            #                    ten = input("Input name: ")    
            #                    item.name =ten
            #                    item.display()
            #                 elif traloi==2:
            #                    tuoi = input("Input age: ")    
            #                    item.age = tuoi
            #                    item.display()
            #                 elif traloi==3:
            #                    luong = float(input("Input salary: "))
            #                    item.salary =luong
            #                    item.display()
            #                 else:
            #                     break
        
        elif userChoice == 6:
        #6:'Delete employee'
            maso = input("Input code: ")
            flag = 0
            for item in dsNhanVien:
                if (item.code == maso):
                    flag = 1
                    dsNhanVien.remove(item)
            if flag == 0: print("Nothing here")
        elif userChoice == 7:
        #7:Increase salary of employee: Tăng lương 1 cho nhân viên 
            maso = input("Input code: ")
            flag = 0
            for item in dsNhanVien:
                if (item.code == maso):
                    flag = 1
                    tangluong = float(input("Input amount: "))
                    item = emp.Employee.increaseSalary(item,amount=tangluong)
            if flag == 0: print("Nothing here")
        elif userChoice == 8:
        #8:Decrease salary of employee: Giảm lương cho 1 NV
            maso = input("Input code: ")
            flag = 0
            for item in dsNhanVien:
                if (item.code == maso):
                    flag = 1
                    giamluong = float(input("Input amount: "))
                    item = emp.Employee.decreaseSalary(item,amount=giamluong)
            if flag == 0: print("Nothing here")
        elif userChoice == 9:
        #9:'Show total employee a month'
            countEmp=0
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                #for item in dsNhanVien:
                    countEmp=len(dsNhanVien)
            print("Number of employees: ",countEmp)
        
        #10: Tính tổng tiền lương của công ty phải trả hàng tháng (sumSalary) và xuất ra màn hình
        elif userChoice == 10:
            sumSalary = 0.0
            for item in dsNhanVien:
                sumSalary = sumSalary + item.salary
            print(f'Total salary a month: {round(sumSalary,2)}') 

        # #Opt-11: Tính trung bình lương của nhân viên (avgSalary) và xuất ra màn hình
        elif userChoice == 11:
            sumSalary = 0.0
            avgSalary = 0.0
            for item in dsNhanVien:
                sumSalary = sumSalary + item.salary
                avgSalary = sumSalary/len(dsNhanVien)
            print(f'Average of Salary: {round(avgSalary,2)}')

        #12: Tính độ tuổi trung bình của nhân viên (avgAge) và xuất ra màn hình
        elif userChoice == 12:
            sumAge = 0
            avgAge = 0
            for item in dsNhanVien:
                sumAge += item.age
                avgAge = sumAge/len(dsNhanVien)
            print(f'Average of Age: {round(avgAge,2)}')

        #13: Tính tuổi lớn nhất của các nhân viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
        elif userChoice ==13:
            maxAge=0
            for item in dsNhanVien:
               if(maxAge<item.age):
                    maxAge=item.age
            print(f'Maximum age: {maxAge}')
        #14: Sắp xếp tăng dần theo lương 
        elif userChoice ==14:
            #dsNhanVien.sort(key=lambda x: x.salary,reverse=False)
            item=emp.Employee.sortSalary(dsNhanVien)
        #15: Vẽ biểu đồ tương quan lương theo độ tuổi
        elif userChoice == 15:
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
            # Vẽ đồ thị
            plt.figure(figsize=(10,5))

            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")

            plt.scatter(arrTuoi,arrLuong, color='green')
            plt.show()
        #16: Vẽ biểu đồ so sánh lương trung bình của các nhóm tuổi: nhỏ hơn 35, từ 35 đến 50, hơn 50 trở lên
        elif userChoice == 16:
            row1 = []
            row2 = []
            row3 = []
            #Lọc lương theo độ tuổi
            for item in dsNhanVien:
                if(item.age<35):
                    row1.append(item.salary)
                elif(15<=item.age<=50):
                    row2.append(item.salary)
                elif(item.age>50):
                    row3.append(item.salary)
            #Kiểm tra số lượng phần tử       
            if(len(row1) ==0):
                row1.append(0)
            if(len(row2) ==0):
                row2.append(0)
            if(len(row3) ==0):
                row3.append(0)
            
            #Thêm tổng lương vào list Oy
            # Oy.append(mean(row1))
            # Oy.append(mean(row2))
            # Oy.append(mean(row3))
            Oy=[mean(row1), mean(row2), mean(row3)]
            #Định dạng cột Ox
            Ox=['Less than 35', 'From 35 to 50', 'More than 50']
            # vẽ biểu đồ cột:
            plt.title('Average of salary chart by age group')
            plt.xlabel('Level of Age')
            plt.ylabel('Averange of salary')
            plt.bar(Ox, Oy, color='green')
            plt.show()

        #17: Vẽ biểu đồ thể hiện phần trăm tổng lương trên các nhóm tuổi như Opt-16
        elif userChoice == 17:
            row1 = []
            row2 = []
            row3 = []
            #Lọc lương theo độ tuổi
            for item in dsNhanVien:
                if(item.age<35):
                    row1.append(item.salary)
                elif(15<=item.age<=50):
                    row2.append(item.salary)
                elif(item.age>50):
                    row3.append(item.salary)
            #Kiểm tra số lượng phần tử       
            if(len(row1) ==0):
                row1.append(0)
            if(len(row2) ==0):
                row2.append(0)
            if(len(row3) ==0):
                row3.append(0)
            
            #Thêm trung bình lương vào list Oy
            # Oy.append(sum(row1))
            # Oy.append(sum(row2))
            # Oy.append(sum(row3))
            Oy=[sum(row1), sum(row2), sum(row3)]
            #Định dạng cột Ox
            Ox=['Less than 35', 'From 35 to 50', 'More than 50']
            # vẽ biểu đồ tròn:
            plt.figure(figsize=(10,5))
            noibat=[0,0.1,0]
            plt.pie(Oy, explode=noibat, labels=Ox, shadow=True, startangle=45)
            plt.axis("equal")
            plt.title('Percentage of salary by age group')
            plt.legend(title='Level of Age')
            plt.show()
        #18: Vẽ biểu đồ thể hiện phần trăm số lượng nhân viên theo các nhóm tuổi như Opt-16 
        elif userChoice == 18:
            row1 = []
            row2 = []
            row3 = []
            #Lọc lương theo độ tuổi
            for item in dsNhanVien:
                if(item.age<35):
                    row1.append(item.salary)
                elif(15<=item.age<=50):
                    row2.append(item.salary)
                elif(item.age>50):
                    row3.append(item.salary)
            
            #Đếm số lượng nhân viên theo độ tuổi
            dem1=len(row1)
            dem2=len(row2)
            dem3=len(row3)
            #Thêm vào list Oy
            Oy=[dem1, dem2, dem3]
            #Định dạng cột Ox
            Ox=['Less than 35', 'From 35 to 50', 'More than 50']
            # vẽ biểu đồ tròn:
            plt.figure(figsize=(10,5))
            noibat=[0,0.1,0]
            plt.pie(Oy, explode=noibat, labels=Ox, shadow=True, startangle=45)
            plt.axis("equal")
            plt.title('percentage of total employee by age group')
            plt.legend(title='Level of Age')
            plt.show()
        #Opt-19: Lưu danh sách nhân viên xuống file dbemp_output.db, 
        #biết rằng mỗi nhân viên là một dòng và các thông tin nhân viên được phân cách bởi dấu '-'
        elif userChoice ==19:
            fw = open('dbemp_output.db',mode='w',encoding='utf-8')  
            for item in dsNhanVien:
                fw.write(f'{item.code},{item.name},{item.age},{item.salary}\n')
            fw.close()
            print('Store file successfully')
        else:
            print('BYE BYE')
            break