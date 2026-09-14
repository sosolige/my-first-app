import streamlit as st

st.title("🛍️ แอปคิดเงิน Shoppity คำนวณส่วนลดประจำร้าน")

# ---------- ราคาสินค้า ----------
p1 = 49    # 🍪 คุกกี้ช็อกโกแล็ตดูไบ ไส้เนยถั่วพิสตาชิโอ
p2 = 79    # 🥣 น้ำพริกหมูสับ จิ้มข้าว
p3 = 299   # 🦐 กุ้งลายเสือดองจัมโบ้ โคเรียดอง
p4 = 20    # 🌶️ หน่อไม้ เห็ดเข้มทองหมาล่า
p5 = 99    # 🥟 ปานิปุริกุ้งดอง

st.header("🧾 กรอกจำนวนที่ต้องการซื้อ")
q1 = st.number_input("🍪 คุกกี้ช็อกโกแล็ตดูไบ ไส้เนยถั่วพิสตาชิโอ (49.-)", min_value=0, value=0, step=1)
q2 = st.number_input("🥣 น้ำพริกหมูสับ จิ้มข้าว (79.-)", min_value=0, value=0, step=1)
q3 = st.number_input("🦐 กุ้งลายเสือดองจัมโบ้ โคเรียดอง (299.-)", min_value=0, value=0, step=1)
q4 = st.number_input("🌶️ หน่อไม้ เด็ดเข้มทองหมาล่า (20.-)", min_value=0, value=0, step=1)
q5 = st.number_input("🥟 ปานิปุริกุ้งดอง (99.-)", min_value=0, value=0, step=1)

st.divider()

# ---------- คำนวณ ----------
total_qty = q1 + q2 + q3 + q4 + q5
subtotal = (q1 * p1) + (q2 * p2) + (q3 * p3) + (q4 * p4) + (q5 * p5)

# if-else ค่าจัดส่ง
if subtotal >= 199:
    shipping = 0
else:
    shipping = 40

total = subtotal + shipping

st.header(f"💰 ยอดรวมสินค้า: {subtotal:.2f} บาท")
st.header(f"🚚 ค่าจัดส่ง: {shipping:.2f} บาท")
st.header(f"💳 ยอดที่ต้องชำระ: {total:.2f} บาท")

# if-else คูปองส่วนลด
if total_qty >= 5:
    st.success("🎉 ยินดีด้วย! รับคูปองส่วนลด 15% สำหรับการซื้อครั้งถัดไป 🎁")
else:
    st.info("🛒 ซื้อครบ 5 ชิ้นขึ้นไป รับคูปองส่วนลด 15% สำหรับครั้งถัดไป")

st.divider()

# ---------- รับเงินและคำนวณเงินทอน ----------
st.header("💵 รับเงินจากลูกค้า")
cash = st.number_input("ลูกค้าจ่ายเงินมา (บาท):", min_value=0.0, value=0.0, step=1.0)

if cash > 0:
    change = cash - total
    if change < 0:
        st.error(f"❌ เงินไม่พอ ขาดอีก {abs(change):.2f} บาท")
    else:
        st.success(f"✅ เงินทอนลูกค้า: {change:.2f} บาท")
