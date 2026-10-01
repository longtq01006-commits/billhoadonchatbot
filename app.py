import streamlit as st
st.image("trasua.JPG")
from datetime import datetime
from pathlib import Path
# =========================================================
# CẤU HÌNH TRANG
# =========================================================
st.set_page_config(
    page_title="Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="centered"
)
st.image("trasua.JPG")
# =========================================================
# CSS GIAO DIỆN
# =========================================================
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-top: 5px;
        margin-bottom: 0px;
    }

    .shop-name {
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        margin-top: 5px;
    }

    .shop-slogan {
        text-align: center;
        color: #777;
        font-size: 15px;
        margin-bottom: 15px;
    }

    .total-box {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        background-color: #f0fdf4;
        border: 2px solid #22c55e;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .invoice-title {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }

    .footer {
        text-align: center;
        color: #777;
        margin-top: 30px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGO QUÁN
# =========================================================
logo_path = Path("logo.png")

if logo_path.exists():
    col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])

    with col_logo2:
        st.image(
            str(logo_path),
            width=180
        )
else:
    st.markdown(
        "<div style='text-align:center; font-size:80px;'>🧋</div>",
        unsafe_allow_html=True
    )

st.markdown(
    "<div class='shop-name'>QUÁN TRÀ SỮA</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='shop-slogan'>Ngon mỗi ngày - Vui mỗi ly ❤️</div>",
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# MENU
# =========================================================
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

# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================
st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================================================
# CHỌN TRÀ SỮA
# =========================================================
st.subheader("🥤 Chọn trà sữa")

loai_tra_sua = st.selectbox(
    "Loại trà sữa",
    list(MENU.keys())
)

gia_tra_sua = MENU[loai_tra_sua]

col1, col2 = st.columns(2)

with col1:
    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

with col2:
    st.write("Đơn giá")
    st.info(f"{gia_tra_sua:,} VNĐ")

# =========================================================
# ĐƯỜNG
# =========================================================
st.subheader("🍬 Mức độ đường")

muc_duong = st.radio(
    "Chọn mức đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# =========================================================
# ĐÁ
# =========================================================
st.subheader("🧊 Mức độ đá")

muc_da = st.radio(
    "Chọn mức đá",
    ["Đá riêng", "Không đá"],
    horizontal=True
)

# =========================================================
# TOPPING
# =========================================================
st.subheader("🍡 Topping")

toppings_chon = st.multiselect(
    "Chọn topping",
    list(TOPPINGS.keys())
)

# =========================================================
# TÍNH TIỀN
# =========================================================
tien_tra_sua = gia_tra_sua * so_luong

tien_topping_mot_ly = sum(
    TOPPINGS[topping]
    for topping in toppings_chon
)

tien_topping = tien_topping_mot_ly * so_luong

tong_tien = tien_tra_sua + tien_topping

# =========================================================
# HIỂN THỊ BILL
# =========================================================
st.divider()

st.markdown(
    "<div class='invoice-title'>🧾 HÓA ĐƠN TẠM TÍNH</div>",
    unsafe_allow_html=True
)

if ten_khach.strip():
    st.write(f"**👤 Khách hàng:** {ten_khach}")
else:
    st.write("**👤 Khách hàng:** Khách lẻ")

st.write(f"**🥤 Món:** {loai_tra_sua}")
st.write(f"**💰 Đơn giá:** {gia_tra_sua:,} VNĐ")
st.write(f"**🔢 Số lượng:** {so_luong}")
st.write(f"**🍬 Đường:** {muc_duong}")
st.write(f"**🧊 Đá:** {muc_da}")

# =========================================================
# TOPPING
# =========================================================
if toppings_chon:

    st.write("**🍡 Topping:**")

    for topping in toppings_chon:

        gia_topping = TOPPINGS[topping]
        thanh_tien = gia_topping * so_luong

        st.write(
            f"- {topping}: "
            f"{gia_topping:,} VNĐ × {so_luong} "
            f"= **{thanh_tien:,} VNĐ**"
        )

else:

    st.write("**🍡 Topping:** Không có")

# =========================================================
# TỔNG TIỀN
# =========================================================
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

st.markdown(
    f"""
    <div class="total-box">
        💰 TỔNG THANH TOÁN<br>
        {tong_tien:,} VNĐ
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TẠO NỘI DUNG HÓA ĐƠN
# =========================================================
def tao_hoa_don():

    thoi_gian = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    ten = ten_khach.strip()

    if not ten:
        ten = "Khách lẻ"

    hoa_don = ""

    hoa_don += "=" * 50 + "\n"
    hoa_don += "              QUÁN TRÀ SỮA\n"
    hoa_don += "                 HÓA ĐƠN\n"
    hoa_don += "=" * 50 + "\n"

    hoa_don += f"Thời gian: {thoi_gian}\n"
    hoa_don += f"Khách hàng: {ten}\n"

    hoa_don += "-" * 50 + "\n"

    hoa_don += "THÔNG TIN MÓN\n"
    hoa_don += "-" * 50 + "\n"

    hoa_don += f"Tên món: {loai_tra_sua}\n"
    hoa_don += f"Đơn giá: {gia_tra_sua:,} VNĐ\n"
    hoa_don += f"Số lượng: {so_luong}\n"
    hoa_don += f"Mức đường: {muc_duong}\n"
    hoa_don += f"Mức đá: {muc_da}\n"

    hoa_don += "-" * 50 + "\n"

    if toppings_chon:

        hoa_don += "TOPPING\n"

        for topping in toppings_chon:

            gia = TOPPINGS[topping]
            thanh_tien = gia * so_luong

            hoa_don += (
                f"{topping}: "
                f"{gia:,} x {so_luong} "
                f"= {thanh_tien:,} VNĐ\n"
            )

    else:

        hoa_don += "Topping: Không có\n"

    hoa_don += "-" * 50 + "\n"

    hoa_don += (
        f"Tiền trà sữa: "
        f"{tien_tra_sua:,} VNĐ\n"
    )

    hoa_don += (
        f"Tiền topping: "
        f"{tien_topping:,} VNĐ\n"
    )

    hoa_don += (
        f"TỔNG THANH TOÁN: "
        f"{tong_tien:,} VNĐ\n"
    )

    hoa_don += "=" * 50 + "\n"
    hoa_don += "           CẢM ƠN QUÝ KHÁCH!\n"
    hoa_don += "              HẸN GẶP LẠI ❤️\n"
    hoa_don += "=" * 50 + "\n"

    return hoa_don


# =========================================================
# THANH TOÁN
# =========================================================
st.divider()

if st.button(
    "💳 THANH TOÁN",
    type="primary",
    use_container_width=True
):

    hoa_don = tao_hoa_don()

    st.success(
        f"✅ Thanh toán thành công! "
        f"Tổng tiền: {tong_tien:,} VNĐ"
    )

    st.subheader("📄 Hóa đơn")

    st.text(hoa_don)

    # Tên file
    ten_file = ten_khach.strip()

    if not ten_file:
        ten_file = "Khach_le"

    # Loại bỏ ký tự không phù hợp trong tên file
    ky_tu_cam = '<>:"/\\|?*'

    for ky_tu in ky_tu_cam:
        ten_file = ten_file.replace(ky_tu, "")

    ten_file = ten_file.replace(" ", "_")

    ten_file = (
        f"Hoa_don_{ten_file}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    # Nút tải hóa đơn
    st.download_button(
        label="📥 TẢI HÓA ĐƠN",
        data=hoa_don.encode("utf-8-sig"),
        file_name=ten_file,
        mime="text/plain",
        use_container_width=True
    )

# =========================================================
# CHÂN TRANG
# =========================================================
st.markdown(
    """
    <div class="footer">
        🧋 Cảm ơn quý khách đã ủng hộ quán!<br>
        Chúc quý khách một ngày vui vẻ ❤️
    </div>
    """,
    unsafe_allow_html=True
)
