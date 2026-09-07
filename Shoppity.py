# ==========================================
# ร้านค้า: Shoppity
# ระบบ Smart Shop & Discount POS System
# ==========================================

# 1. รายการสินค้าและราคา
MENU = {
    1: {"name": "คุกกี้ช็อกโกแล็ตดูไบไส้เนยถั่วพิสตาชิโอ", "price": 49},
    2: {"name": "โมจิแม่มั้ย ดิปนูเทลล่า", "price": 89},
    3: {"name": "ขันติไข่เยิ้ม", "price": 20},
    4: {"name": "ไข่ครอบเก่ง ธชย", "price": 29},
    5: {"name": "น้ำโอ๊ต", "price": 45},
    6: {"name": "น้ำพริกหมูสับดมข้าว", "price": 79},
    7: {"name": "กุ้งลายเสือดองจัมโบ้ โคเรียดอง", "price": 299},
    8: {"name": "หน่อไม้ เห็ดเข็มทองหมาล่า", "price": 20},
    9: {"name": "ขนมขี้ผึ้งสอดไส้แยมผลไม้", "price": 129},
    10: {"name": "ปานิปูริกุ้งดอง", "price": 99}
}

def display_menu():
    print("\n" + "="*50)
    print("         ยินดีต้อนรับสู่ร้าน Shoppity")
    print("="*50)
    for item_id, info in MENU.items():
        print(f"[{item_id:2d}] {info['name']:<35} {info['price']} บาท")
    print("="*50)

def main():
    display_menu()
    
    total_price = 0
    selected_items = []

    # 2. รับข้อมูลการสั่งซื้อสินค้า
    print("\n--- เลือกซื้อสินค้า (พิมพ์ 0 เมื่อเลือกเสร็จสิ้น) ---")
    while True:
        try:
            choice = int(input("กรุณาเลือกหมายเลขสินค้า (1-10): "))
            if choice == 0:
                if not selected_items:
                    print("ยังไม่ได้เลือกสินค้า กรุณาเลือกอย่างน้อย 1 รายการ")
                    continue
                break
            elif choice in MENU:
                qty = int(input(f"จำนวนสำหรับ '{MENU[choice]['name']}': "))
                if qty > 0:
                    subtotal = MENU[choice]['price'] * qty
                    total_price += subtotal
                    selected_items.append((MENU[choice]['name'], MENU[choice]['price'], qty, subtotal))
                    print(f"-> เพิ่ม {MENU[choice]['name']} x{qty} เรียบร้อยแล้ว (รวม: {subtotal} บาท)")
                else:
                    print("จำนวนต้องมากกว่า 0")
            else:
                print("ไม่มีหมายเลขสินค้านี้ กรุณาลองใหม่")
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")

    # 3. เงื่อนไขส่วนลด (If-Else)
    # เงื่อนไข 1: ยอดซื้อรวมตั้งแต่ 300 บาทขึ้นไป ลด 10%
    discount_percent = 0
    if total_price >= 300:
        discount_percent = 10

    # เงื่อนไข 2: สมาชิก ลดเพิ่ม 50 บาท
    is_member = input("\nเป็นสมาชิกหรือไม่? (y/n): ").strip().lower() == 'y'
    member_discount = 50 if is_member else 0

    # คำนวณส่วนลดและยอดเงินสุทธิ
    percent_discount_amount = (total_price * discount_percent) / 100
    total_discount = percent_discount_amount + member_discount
    
    # กรณีส่วนลดมากกว่าราคาสินค้า ให้ยอดจ่ายจริงเป็น 0
    final_amount = max(0, total_price - total_discount)

    # 4. สรุปรายการและรับเงิน
    print("\n" + "="*50)
    print("                  ใบเสร็จชำระเงิน")
    print("="*50)
    for name, price, qty, subtotal in selected_items:
        print(f"- {name} x{qty} @{price} = {subtotal} บาท")
    print("-" * 50)
    print(f"ราคารวมทั้งหมด:           {total_price:.2f} บาท")
    print(f"ส่วนลดซื้อครบ 300 ({discount_percent}%):   -{percent_discount_amount:.2f} บาท")
    print(f"ส่วนลดสมาชิก:             -{member_discount:.2f} บาท")
    print(f"ยอดเงินที่ต้องจ่ายจริง:       {final_amount:.2f} บาท")
    print("="*50)

    # รับเงินจากลูกค้าและคำนวณเงินทอน
    while True:
        try:
            cash = float(input("\nกรุณารับเงินจากลูกค้า (บาท): "))
            if cash >= final_amount:
                change = cash - final_amount
                print(f"เงินทอน:                  {change:.2f} บาท")
                print("\nขอบคุณที่ใช้บริการร้าน Shoppity!")
                break
            else:
                print(f"เงินไม่พอ! ขาดอีก {final_amount - cash:.2f} บาท")
        except ValueError:
            print("กรุณากรอกจำนวนเงินเป็นตัวเลข")

if __name__ == "__main__":
    main()
