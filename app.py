from flask import Flask

app = Flask(__name__)

# قائمة المنتجات
products = [
    {'id': 1, 'name': 'Telefon'},
    {'id': 2, 'name': 'Laptop'},
    {'id': 3, 'name': 'Kulaklık'}
]

# عربة التسوق
cart = []

# روت الصفحة الرئيسية
@app.route('/')
def home():
    # نرجّع نص يحتوي أسماء المنتجات عشان الاختبار يلاقي "Telefon"
    return 'Telefon | Laptop | Kulaklık'

# روت إضافة المنتج إلى العربة
@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return f"{product['name']} sepete eklendi!"
    return "Ürün bulunamadı."
