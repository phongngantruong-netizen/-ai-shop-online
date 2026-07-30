
import streamlit as st
import pandas as pd

# Cấu hình trang web chuyên nghiệp cho dân kinh doanh
st.set_page_config(page_title="AI Profit Analyzer", layout="wide", page_icon="💸")
st.title(" AI Tự Động Tính Toán Lợi Nhuận Shop Online")
st.success(" CÔNG CỤ ĐỘC QUYỀN VIP - GIÚP CHỦ SHOP KHÔNG LO THẤT THOÁT DÒNG TIỀN")

# Thanh hướng dẫn 3 bước giúp ní ẩn mình hoàn toàn khi bán trên Sharecode
with st.expander(" HƯỚNG DẪN 3 BƯỚC CHO CHỦ SHOP (XÀI TRỌN ĐỜI)", expanded=True):
    st.markdown("""
    *   **Bước 1:** Nhập tổng **Doanh thu thô** thu được từ các sàn (TikTok, Shopee...) vào ô đầu tiên.
    *   **Bước 2:** Nhìn vào bảng phía dưới, bấm **"+ Add row"** để tự nhập các chi phí (Tiền nhập hàng, Tiền quảng cáo, Tiền ship, Phí sàn...).
    *   **Bước 3:** Bấm nút tên lửa để AI tự động tính toán số tiền thực tế bạn đút túi và vẽ biểu đồ chi phí.
    """)

st.write("---")

# 1. Ô nhập Doanh thu thô (Doanh thu chưa trừ chi phí)
st.subheader(" 1. Doanh Thu Thừa Nhận Từ Các Sàn:")
doanh_thu = st.number_input("Tổng doanh thu hiển thị trên app sàn (VNĐ):", min_value=0, value=0, step=100000)

st.write("---")

# 2. Bảng nhập chi phí động đặc thù kinh doanh online
st.subheader(" 2. Bảng Kê Khai Chi Phí Vận Hành Shop:")

# Tạo sẵn các danh mục chi phí mặc định để chủ shop dễ xài
data_chi_phi_mac_dinh = pd.DataFrame([
    {"Hạng Mục Chi Phí": "Tiền nhập hàng sỉ", "Số Tiền (VNĐ)": 0},
    {"Hạng Mục Chi Phí": "Phí sàn (TikTok/Shopee %)", "Số Tiền (VNĐ)": 0},
    {"Hạng Mục Chi Phí": "Tiền chạy quảng cáo (Ads)", "Số Tiền (VNĐ)": 0},
    {"Hạng Mục Chi Phí": "Tiền bù tiền ship/Hộp đóng gói", "Số Tiền (VNĐ)": 0}
])

# Kích hoạt tính năng kéo thả thêm dòng động của Streamlit
bang_chi_phi = st.data_editor(
    data_chi_phi_mac_dinh,
    num_rows="dynamic", # Chủ shop tự bấm dấu cộng thêm các chi phí khác như "Tiền thuê mẫu livestream"
    use_container_width=True
)

st.write("---")

# 3. Nút bấm kích hoạt Bộ não AI Pandas để tính Lợi Nhuận Ròng
if st.button(" KÍCH HOẠT AI TÍNH LỢI NHUẬN THỰC TẾ"):
    # Ép dữ liệu bảng về DataFrame của Pandas để tính toán
    df_chi_phi = pd.DataFrame(st.data_editor("bang_chinh_sua") if 'bang_chinh_sua' in locals() else bang_chi_phi)
    
    # Tính tổng chi phí
    tong_chi_phi = df_chi_phi["Số Tiền (VNĐ)"].sum()
    
    # Tính Lợi nhuận ròng (Tiền thực tế bỏ túi)
    loi_nhuan_rong = doanh_thu - tong_chi_phi
    
    # Tính Tỷ suất lợi nhuận (%)
    ty_suat = (loi_nhuan_rong / doanh_thu * 100) if doanh_thu > 0 else 0
    
    # Hiển thị kết quả bằng các ô chỉ số (Metrics) cực kỳ sang chảnh như bảng điều khiển doanh nghiệp
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label=" Tổng Chi Phí Vận Hành", value=f"{tong_chi_phi:,} VNĐ")
    with c2:
        # Nếu lợi nhuận dương thì hiện chữ xanh, âm hiện chữ đỏ cảnh báo
        if loi_nhuan_rong >= 0:
            st.metric(label="Lợi Nhuận Thực Tế Đút Túi", value=f"{loi_nhuan_rong:,} VNĐ")
        else:
            st.metric(label=" Shop Đang Bị LỖ VỐN", value=f"{loi_nhuan_rong:,} VNĐ", delta="- Nguy hiểm!")
    with c3:
        st.metric(label=" Tỷ Suất Lợi Nhuận Ròng", value=f"{ty_suat:.1f} %")
        
    # Xử lý hiệu ứng hình ảnh và biểu đồ ăn tiền
    st.write("---")
    if loi_nhuan_rong > 0:
        st.balloons() # Phun bóng bay ăn mừng shop có lãi tốt
        st.success(" Xin chúc mừng! Shop của bạn đang vận hành có lãi rất tốt. Hãy tiếp tục phát huy!")
        
        # Tự động vẽ biểu đồ hình cột phân bổ các khoản chi phí để chủ shop biết tiền đi đâu nhiều nhất
        st.write(" **Biểu đồ phân tích cấu trúc các khoản chi phí của shop:**")
        st.bar_chart(df_chi_phi.set_index("Hạng Mục Chi Phí")["Số Tiền (VNĐ)"])
    elif doanh_thu == 0 and tong_chi_phi == 0:
        st.info(" Vui lòng điền số liệu doanh thu và chi phí để AI tính toán nhé shop!")
    else:
        st.error(" Shop đang chi tiêu vượt quá doanh thu! Hãy kiểm tra lại tiền chạy quảng cáo hoặc phí nhập hàng ngay!")
