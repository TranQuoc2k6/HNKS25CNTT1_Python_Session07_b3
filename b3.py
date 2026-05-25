"""
1. Phân tích và thiết kế giải pháp
    Input: dữ liệu nhân sự từ hệ thống CRM cũ
    Output: Menu gồm 4 chức năng

    Bước 1: tạo biến raw_data để lưu dữ liệu gốc:
    Bước 2: hiển thị menu và đưa vào vòng lặp, tạo 1 biến choice để cho người dùng lựa chọn
    Bước 3: tạo các case tương ứng với lựa chọn của người dùng
    Bước 4: Hiển thị dữ liệu gốc(case 1)
    Bước 5: chuẩn hóa dữ liệu(case 2)
        5.1: Cần tách dữ liệu gốc: dùng strip() và split() thành list
        5.2: dùng vòng lặp để duyệt qua từng nhân viên trong list
        5.3: tách thông tin của từng nhân viên để chuẩn hóa
        5.4: in ra kiểu f-string
    Bước 6: cho người dùng nhập nhân viên muốn tìm (case 3)
        6.1: tách dữ liệu gốc thành list
        6.2: dùng vòng lặp để duyệt qua các phần tử có trong list
        6.3: tách id của từng sinh viên để chuẩn hóa
        6.4: so sánh id nhập vào id nhân viên có trong list
    Bước 7: Nếu người dùng nhập 4 thì thoát chương trình (cas4)
    Bước 8: Kiểm tra nếu người dùng nhập khác các case trên thì hiển thị thông báo và cho nhập lại
"""

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
while True:
    print("\n\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    print()
    match choice:
        case "1":
            print(raw_data)
        case "2":
            employees = raw_data.strip().split("|")

            print(f"{'ID':<10}{'HỌ TÊN':<20}{'SỐ ĐIỆN THOẠI':<20}{'PHÒNG BAN':<10}")
            print("-" * 60) 
    
            for emp in employees:
                employee_info = emp.strip().split(";")
                
                emp_id = employee_info[0].strip().upper()
                full_name = employee_info[1].strip().title()
                deperment = employee_info[3].strip().upper()
                phone = employee_info[2].strip().replace("-", "")

                if phone.isdigit():
                    new_phone = "******" + phone[-4:]
                else:
                    new_phone = "Invalid Format"

                print(f"{emp_id:<10}{full_name:<20}{new_phone:<20}{deperment:<10}")
        
        case "3":
            employees = raw_data.strip().split("|")

            input_id_search = input("Nhập mã id cần tìm: ")
            standardization_id = input_id_search.strip().upper() 
            flag = 0
            for i in employees:
                employee_info = i.strip().split(";")

                emp_id = employee_info[0].strip().upper()
                if standardization_id == emp_id:
                    flag = 1
                    print("Đã tìm thấy nhân viên")

            if flag == 0:
                print("Không tìm thấy nhân viên")

        case "4":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại")

