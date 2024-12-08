from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')  # Busca en la carpeta templates/login.html

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')  # Busca en templates/catalogo.html

if __name__ == '__main__':
    app.run(port=5000)
