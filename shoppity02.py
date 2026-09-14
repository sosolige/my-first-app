"""
🛍️  Shoppity  🛍️
แอปคิดเงินและคำนวณส่วนลดประจำร้าน (Smart Shop & Discount)
"""

# ---------- ข้อมูลร้าน ----------
SHOP_NAME = "Shoppity"

PRODUCTS = [
    {"name": "คุกกี้ช็อกโกแล็ตดูไบ ไส้เนยถั่วพิสตาชิโอ", "emoji": "🍪", "price": 49},
    {"name": "น้ำพริกหมูสับ จิ้มข้าว",                    "emoji": "🥣", "price": 79},
    {"name": "กุ้งลายเสือดองจัมโบ้ โคเรียดอง",             "emoji": "🦐", "price": 299},
    {"name": "หน่อไม้ เห็ดเข้มทองหมาล่า",                  "emoji": "🌶️", "price": 20},
    {"name": "ปานิปุริกุ้งดอง",                            "emoji": "🥟", "price": 99},
]

# ---------- เงื่อนไขส่วนลด ----------
COUPON_QTY = 5      # ซื้อครบกี่ชิ้นถึงได้คูปอง
COUPON_PCT = 15     # % ส่วนลดคูปอง (ใช้ครั้งถัดไป)
FREE_SHIP_MIN = 199  # ยอดขั้นต่ำที่ส่งฟรี
SHIP_FEE = 40        # ค่าส่งถ้ายอดไม่ถึงขั้นต่ำ


def print_header():
    print("=" * 46)
    print(f"   🛍️✨  welcome to {SHOP_NAME}  ✨🛍️")
    print("      ร้านของอร่อย ๆ ครบจบในที่เดียว 🍡")
    print("=" * 46)


def print_menu():
    print("\n🧾 รายการสินค้า")
    print("-" * 46)
    for i, p in enumerate(PRODUCTS, start=1):
        print(f"  {i}. {p['emoji']}  {p['name']:<38} {p['price']:>4.0f}.-")
    print("-" * 46)


def get_quantities():
    """ให้ลูกค้ากรอกจำนวนสินค้าแต่ละชิ้น"""
    qty = []
    print("\n📝 กรอกจำนวนที่ต้องการซื้อของสินค้าแต่ละชิ้น (พิมพ์ 0 ถ้าไม่ซื้อ)")
    for p in PRODUCTS:
        while True:
            raw = input(f"   {p['emoji']} {p['name']}: ")
            if raw.strip() == "":
                raw = "0"
            try:
                n = int(raw)
                if n < 0:
                    raise ValueError
                qty.append(n)
                break
            except ValueError:
                print("   ⚠️  กรุณากรอกจำนวนเต็มไม่ติดลบนะคะ")
    return qty


def calc_subtotal(qty):
    return sum(q * p["price"] for q, p in zip(qty, PRODUCTS))


def calc_shipping(subtotal):
    # if-else เงื่อนไขค่าส่ง
    if subtotal >= FREE_SHIP_MIN:
        return 0
    else:
        return SHIP_FEE


def check_coupon(total_qty):
    # if-else เงื่อนไขคูปองส่วนลด
    if total_qty >= COUPON_QTY:
        return True
    else:
        return False


def print_receipt(qty, subtotal, shipping, total, coupon_earned):
    print("\n" + "🌸 สรุปยอดการสั่งซื้อ 🌸".center(46, " "))
    print("-" * 46)
    for q, p in zip(qty, PRODUCTS):
        if q > 0:
            line_total = q * p["price"]
            print(f"  {p['emoji']} {p['name']} x{q}  =  {line_total:.0f}.-")
    print("-" * 46)
    print(f"  ยอดรวมสินค้า        : {subtotal:>8.0f}.-")
    ship_text = "ฟรี 🚚" if shipping == 0 else f"{shipping:.0f}.-"
    print(f"  ค่าจัดส่ง            : {ship_text:>8}")
    print("=" * 46)
    print(f"  💳 ยอดที่ต้องชำระ     : {total:>8.0f}.-")
    print("=" * 46)

    if coupon_earned:
        print(f"  🎉 ยินดีด้วย! รับคูปองส่วนลด {COUPON_PCT}% สำหรับการซื้อครั้งถัดไป 🎁")


def get_cash_and_change(total):
    while True:
        raw = input("\n💵 รับเงินจากลูกค้ากี่บาท: ")
        try:
            cash = float(raw)
            break
        except ValueError:
            print("   ⚠️  กรุณากรอกตัวเลขนะคะ")

    change = cash - total
    if change < 0:
        print(f"\n❌ เงินไม่พอค่ะ ขาดอีก {abs(change):.0f}.- 🙏")
    else:
        print(f"\n✅ เงินทอนลูกค้า: {change:.0f}.- 💰")


def main():
    print_header()
    print_menu()
    qty = get_quantities()

    total_qty = sum(qty)
    if total_qty == 0:
        print("\n🙁 ยังไม่ได้เลือกสินค้าเลยนะคะ แอปขอจบการทำงานก่อน")
        return

    subtotal = calc_subtotal(qty)
    shipping = calc_shipping(subtotal)
    total = subtotal + shipping
    coupon_earned = check_coupon(total_qty)

    print_receipt(qty, subtotal, shipping, total, coupon_earned)
    get_cash_and_change(total)

    print("\n🙏 ขอบคุณที่อุดหนุนร้าน Shoppity นะคะ แล้วมาใหม่น้า 💗\n")


if __name__ == "__main__":
    main()
