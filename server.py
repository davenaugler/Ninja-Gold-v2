from flask import Flask, render_template, request, redirect, session
from random import randint
from datetime import datetime
from time import strftime

app = Flask(__name__)
app.secret_key = "This is the Coding Dojo Ninja Gold Application"


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        print('Current Gold:',session['gold'])
        session['activities'] = []
        print('Printing Activities:',session['activities'])
        session['count_down'] = 15
        session['win'] = False
        session['action'] = ''
        session['text'] = ''
        session['find_gold'] = 'Find Gold!'
        print('Total Count (in index):',session['count_down'])
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    gold = 0
    property = ''
    now = datetime.now()
    date_now=now.strftime("%Y/%m/%d %I:%M %p")

    if request.form['property'] == 'farm':
        gold = randint(10, 20)
        property = 'farm'
        session['gold'] += gold
        session['count_down'] -= 1
        print('Total Count:',session['count_down'])
        print('Farm Gold:', gold)
    elif request.form['property'] == 'cave':
        gold = randint(5, 10)
        property = 'cave'
        session['gold'] += gold
        session['count_down'] -= 1
        print('Total Count:',session['count_down'])
        print('Cave Gold:', gold)
    elif request.form['property'] == 'house':
        gold = randint(2,5)
        property = 'house'
        session['gold'] += gold
        session['count_down'] -= 1
        print('Total Count:',session['count_down'])
        print('House Gold:', gold)
    else:
        request.form['property'] == 'casino'
        gold = randint(-50,50)
        property = 'casino'
        session['gold'] += gold
        session['count_down'] -= 1
        print('Total Count:',session['count_down'])
        print('Casino Gold:', gold)

    if session['count_down'] == 0:
        color = 'text-danger'
        session['button'] = "<button type='submit' class='btn btn-danger mt-3 {{ session['button'] }}'>Reset</button>"
        session['text'] = 'Reset'

        session['action'] = 'reset'

    
    if session['count_down'] == 0:
        session['count_down'] = "You loose. Let's play again!"
        color = 'text-danger'

    if gold < 0:
        result = f"Entered a casino and lost {gold} golds... Ouch... ({date_now})"
        color = 'text-danger'
    else:
        result = f"Earned {gold} golds from the {property}! ({date_now})"
        color = 'text-success'
    
    session['activities'].append({"result": result, "color": color})
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
