print("\nHoạt động 4: ");
so_luot_truy_cap = 0
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 36
def vi_du_bien_local():
    so_luot_truy_cap = 100
    print("Bên trong hàm, biến local = ", so_luot_truy_cap)
tang_luot_truy_cap()
tang_luot_truy_cap()
print("Số lượt truy cập (global): ", so_luot_truy_cap)

print("\nHoạt động 5: ");
danh_sach_so = [2, 4, 6, 8, 10]
binh_phuong = list(map(lambda x: x**2, danh_sach_so))
print(binh_phuong)

so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print(so_chan)

danh_sach_sv = [
    {"tên": "Quách", "điểm": 6.5},
    {"tên": "Đức", "điểm": 7.5},
    {"tên": "Mạnh", "điểm": 8.5},
]
sap_xep_theo_diem = sorted(danh_sach_sv, key=lambda sv: sv["điểm"])
sap_xep_giam_dan = sorted(danh_sach_sv, key=lambda sv: sv["điểm"], reverse=True)
print("Tăng dần")
for sv in sap_xep_theo_diem:
    print(sv["tên"], "-", sv["điểm"])
print("Giảm dần")
for sv in sap_xep_giam_dan:
    print(sv["tên"], "-", sv["điểm"])