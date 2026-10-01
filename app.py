import streamlit as st
from datetime import datetime
from io import BytesIO

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính Bill Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

# =========================
# DỮ LIỆU MENU
# =========================
MENU = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa socola": 35000,
    "Trà sữa matcha": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa caramel": 38000,
    "Trà sữa ô long": 40000,
}

TOPPINGS = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 6000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Thạch phô mai": 7000,
    "Kem cheese": 10000,
}

# =========================
# TIÊU ĐỀ
# =========================
st.title("🧋 QUÁN TRÀ SỮA")
st.subheader("💰 Tính bill hóa đơn")

st.divider()

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
ten_khach = st.text_input(
    "👤 Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================
# CHỌN TRÀ SỮA
# =========================
st.subheader("🥤 Chọn món")

loai_tra_sua = st.selectbox(
    "Loại trà sữa",
    list(MENU.keys())
)

gia_tra_sua = MENU[loai_tra_sua]

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

# =========================
# MỨC ĐỘ ĐƯỜNG
# =========================
muc_duong = st.radio(
    "🍬 Mức độ đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# =========================
# MỨC ĐỘ ĐÁ
# =========================
muc_da = st.radio(
    "🧊 Mức độ đá",
    ["Đá riêng", "Không đá"],
    horizontal=True
)

# =========================
# TOPPING
# =========================
st.subheader("🍡 Topping")

toppings_chon = st.multiselect(
    "Chọn topping",
    list(TOPPINGS.keys())
)

# =========================
# TÍNH TIỀN
# =========================
tien_tra_sua = gia_tra_sua * so_luong

tien_topping_mot_ly = sum(
    TOPPINGS[topping] for topping in toppings_chon
)

tien_topping = tien_topping_mot_ly * so_luong

tong_tien = tien_tra_sua + tien_topping

# =========================
# HIỂN THỊ KẾT QUẢ
# =========================
st.divider()
st.subheader("🧾 HÓA ĐƠN TẠM TÍNH")

if ten_khach.strip():
    st.write(f"**Khách hàng:** {ten_khach}")
else:
    st.write("**Khách hàng:** Chưa nhập tên")

st.write(f"**Món:** {loai_tra_sua}")
st.write(f"**Đơn giá:** {gia_tra_sua:,} VNĐ")
st.write(f"**Số lượng:** {so_luong}")
st.write(f"**Đường:** {muc_duong}")
st.write(f"**Đá:** {muc_da}")

if toppings_chon:
    st.write("**Topping:**")
    for topping in toppings_chon:
        st.write(
            f"- {topping}: {TOPPINGS[topping]:,} VNĐ x {so_luong}"
        )
else:
    st.write("**Topping:** Không có")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Tiền trà sữa",
        f"{tien_tra_sua:,} VNĐ"
    )

with col2:
    st.metric(
        "Tiền topping",
        f"{tien_topping:,} VNĐ"
    )

st.success(
    f"💰 TỔNG THANH TOÁN: {tong_tien:,} VNĐ"
)

# =========================
# TẠO NỘI DUNG HÓA ĐƠN
# =========================
def tao_hoa_don():
    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    hoa_don = ""
    hoa_don += "=" * 45 + "\n"
    hoa_don += "          QUÁN TRÀ SỮA\n"
    hoa_don += "             HÓA ĐƠN\n"
    hoa_don += "=" * 45 + "\n"

    hoa_don += f"Thời gian: {thoi_gian}\n"
    hoa_don += f"Khách hàng: {ten_khach if ten_khach.strip() else 'Khách lẻ'}\n"

    hoa_don += "-" * 45 + "\n"
    hoa_don += f"Món: {loai_tra_sua}\n"
    hoa_don += f"Đơn giá: {gia_tra_sua:,} VNĐ\n"
    hoa_don += f"Số lượng: {so_luong}\n"
    hoa_don += f"Đường: {muc_duong}\n"
    hoa_don += f"Đá: {muc_da}\n"

    hoa_don += "-" * 45 + "\n"

    if toppings_chon:
        hoa_don += "TOPPING:\n"
        for topping in toppings_chon:
            tien = TOPPINGS[topping] * so_luong
            hoa_don += (
                f"- {topping}: "
                f"{TOPPINGS[topping]:,} x {so_luong} "
                f"= {tien:,} VNĐ\n"
            )
    else:
        hoa_don += "Topping: Không có\n"

    hoa_don += "-" * 45 + "\n"
    hoa_don += f"Tiền trà sữa: {tien_tra_sua:,} VNĐ\n"
    hoa_don += f"Tiền topping: {tien_topping:,} VNĐ\n"
    hoa_don += f"TỔNG THANH TOÁN: {tong_tien:,} VNĐ\n"

    hoa_don += "=" * 45 + "\n"
    hoa_don += "       CẢM ƠN QUÝ KHÁCH!\n"
    hoa_don += "=" * 45 + "\n"

    return hoa_don


# =========================
# NÚT THANH TOÁN
# =========================
st.divider()

if st.button(
    "💳 THANH TOÁN",
    type="primary",
    use_container_width=True
):

    if not ten_khach.strip():
        ten_file = "Khach_le"
    else:
        ten_file = ten_khach.strip().replace(" ", "_")

    hoa_don = tao_hoa_don()

    st.success("✅ Thanh toán thành công!")

    st.subheader("📄 Hóa đơn")

    st.text(hoa_don)

    # Tạo file để tải xuống
    file_data = hoa_don.encode("utf-8-sig")

    st.download_button(
        label="📥 TẢI HÓA ĐƠN",
        data=file_data,
        file_name=f"Hoa_don_{ten_file}.txt",
        mime="text/plain",
        use_container_width=True
    )
