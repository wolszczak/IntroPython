from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_flask():
    return 'Hello flask'

@app.route('/temp')
def use_template():
    return render_template('hello.html')


@app.route('/query/')
def query_strings(greeting = 'hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {}</h1>'.format(query_val) 

@app.route('/user/')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there! {}</h1>'.format(name)

@app.route('/text/<string:text>')
def working_with_strings(text):
    return '<h1>here is a string ' + str(text) +'</h1>'

@app.route('/numbers/<int:number>')
def working_with_integer(number):
    return '<h1>here is an integer number ' + number +'</h1>'

@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1,num2):
    return '<h1>the sum is: {}'.format(num1 + num2) + '</h1>'

@app.route('/product/<float:num1>/<float:num2>')
def multiplying_floats(num1,num2):
    return '<h1>the product is: {}'.format(num1 * num2) + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)