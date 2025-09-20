from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        print("ДАННЫЕ ОТ ПОЛЬЗОВАТЕЛЯ:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
        print("---")
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        print("ДАННЫЕ ИЗ ФОРМЫ КОНТАКТОВ:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
        print("---")
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
