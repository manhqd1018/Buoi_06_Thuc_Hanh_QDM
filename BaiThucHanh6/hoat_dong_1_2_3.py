print("\nHoạt động 1: ");
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bscnn(a, b):
    return a*b // uscln(a, b)
def kiem_tra_nguyen_to(n):
    if n<2:
        return False
    for i in range(2, n):
        if n % 1 == 0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % 1 == 0:
            tong_uoc += i
    return tong_uoc == n
print(uscln(24, 48))
print(bscnn(4, 8))
print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28))

def in_loi_chao(ten):
    print(f"Xin chào, {ten}!")
    return
def chia_lay_thuong_du(a, b):
    return a//b, a%b
in_loi_chao("Mạnh")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thương: {thuong}, dư: {du}")

print("\nHoạt động 2: ");
def gioi_thieu(ten, tuoi = 18, lop = "Chưa rõ"):
    print(f"Tên: {ten} - Tuổi: {tuoi} - Lớp: {lop}")
gioi_thieu("Quách")
gioi_thieu("Đức", 19)
gioi_thieu("Chi", lop="ĐH14C5")
gioi_thieu(ten="Mạnh", lop="ĐH14C5", tuoi=19)

print("\nHoạt động 3: ");
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print(tinh_tong(12, 34, 56))
print(tinh_tong(78, 910, 1112, 1314, 1516))
print(tinh_tong())

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Họ tên: {ho_ten} - Tuổi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"{khoa}: {gia_tri}")
in_thong_tin("Quách Đức Mạnh", 19, lop="ĐH14C5", que_quan="Hà Nội")
in_thong_tin("Wu Lei", 27, email="b@example.com")