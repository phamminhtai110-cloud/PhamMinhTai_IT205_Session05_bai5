print("=== HE THONG QUAN LY THONG KE HOC VIEN ===\n")

while True:
    print("\n1. Nhap du lieu & bao cao")
    print("2. Huong dan")
    print("3. Thoat")
    choice = input("Chon: ")

    if choice == "1":
        so_cn = int(input("So chi nhanh: "))
        max_total = 0
        max_branch = 0
        low_classes = []

        for b in range(1, so_cn + 1):
            print(f"\nChi nhanh {b}:")
            so_lop = int(input("So lop: "))
            total = 0

            for c in range(1, so_lop + 1):
                while True:
                    sv = int(input(f"Lop {c} - so hoc vien: "))
                    if sv >= 0:
                        break
                    print("So hoc vien khong hop le!")
                total += sv
                if sv < 10:
                    low_classes.append(f"Chi nhanh {b} - Lop {c}: {sv} sv")

            print(f"Tong chi nhanh {b}: {total}")
            if total > max_total:
                max_total = total
                max_branch = b

        print(f"\nChi nhanh cao nhat: {max_branch} ({max_total} sv)")
        if low_classes:
            print("Lop si so thap:")
            for l in low_classes:
                print(f"  - {l}")
        else:
            print("Khong co lop nao duoi 10 hoc vien")

    elif choice == "2":
        print("\nNhap so hoc vien (>=0), he thong tu dong thong ke")

    elif choice == "3":
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le!")