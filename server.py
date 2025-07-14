from flask import Flask, render_template, request
import os

app = Flask(__name__)

PRODUCTS = {
    "Pant Hook Packet": 15,
    "Press Button": 15,
    "Sewing Needle": 30,
    "Machine Needle": 50,
    "Oil Bottle Small": 30,
    "Oil Bottle Big": 50,
    "Oil Pouring Bottle": 25,
    "Fall": 12,
    "Cotton Fall": 20,
    "Cobra Measure Tape": 25,
    "Sada Astar": 32,
    "Divya Astar": 35,
    "TR Astar": 46,
    "Butter Crepe": 45,
    "Satin Astar": 80,
    "Manjar Paat": 120,
    "Sadi Net": 30,
    "Coats Thread Box": 85,
    "Bobbin Case": 50,
    "Bobbin": 5
}

@app.route('/')
def index():
    return render_template("index.html", products=PRODUCTS)

def get_next_bill_number():
    path = "bill_counter.txt"
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("1")
        return 1
    with open(path, "r") as f:
        bill_no = int(f.read())
    with open(path, "w") as f:
        f.write(str(bill_no + 1))
    return bill_no

@app.route('/generate-bill', methods=['POST'])
def generate_bill():
    customer_name = request.form['customerName']
    items = request.form.getlist('item[]')
    quantities = list(map(int, request.form.getlist('quantity[]')))
    bill_no = get_next_bill_number()

    bill_items = []
    total_amount = 0
    for item, qty in zip(items, quantities):
        price = PRODUCTS[item]
        amount = price * qty
        total_amount += amount
        bill_items.append({
            'description': item,
            'quantity': qty,
            'price': price,
            'amount': amount
        })

    return render_template("bill_template.html", customer_name=customer_name, bill_items=bill_items, total=total_amount, bill_no=bill_no)

if __name__ == '__main__':
    app.run(debug=True)
