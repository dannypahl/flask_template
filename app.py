from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def mike():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

<main>
@app.route('/add', methods=['POST'])
def submit_form():
   
    data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'comments': request.form['comments']
    }
   
   
    data_list.append(data)
   
    return redirect('/')
</main>
