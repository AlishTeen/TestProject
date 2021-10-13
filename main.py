from flask import Flask, render_template, request

app = Flask(__name__)

base = []


@app.route('/', methods=['POST', 'GET'])
def first():
    if request.method == "POST":
        category = request.form['category']
        name = request.form['name']
        price = request.form['price']
        color = request.form['color']
        temp = {'category': category, 'name': name, 'price': price, 'color': color}
        base.append(temp)
        print(base)
        return render_template('first.html')
    else:
        return render_template('first.html')


@app.route('/second')
def second():
    return render_template('second.html', data=base)


app.run(debug=False)
