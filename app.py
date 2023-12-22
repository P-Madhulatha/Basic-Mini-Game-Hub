from flask import Flask, render_template, request, jsonify
import random
import threading
import time

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Rock, Paper, Scissors logic
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        choices = ['rock', 'paper', 'scissors']
        user_choice = request.form.get('choice')

        # Check if the user has made a choice
        if not user_choice:
            return render_template('game.html', error='Please choose an option')

        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)

        return render_template('game.html', user_choice=user_choice, computer_choice=computer_choice, result=result)
    else:
        # Handle GET requests (if needed)
        return render_template('game.html')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie! \U0001F926'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'You win! \U0001F918'
    else:
        return 'You lose! \U0001F91E'


# Coin Toss logic
@app.route('/coin_toss', methods=['POST','GET'])
def coin_toss():
    if request.method == 'POST':
        user_guess = request.form.get('guess').lower()
        if not user_guess:
            return render_template('coin_toss.html', error='Please choose an option')
        
        result = coin_toss_game(user_guess)
        return render_template('coin_toss.html', user_guess=user_guess, result=result)
    else:
        # This block is executed when the user initially navigates to the coin_toss page (GET request)
        return render_template('coin_toss.html')

def coin_toss_game(guess):
    result = random.choice(["heads", "tails"])
    if guess == result:
        return 'You win! \U0001F918'
    else:
        return 'You lose! \U0001F91E'

#math game
@app.route('/math_game', methods=['GET', 'POST'])
def math_game():
    if request.method == 'GET':
        # Generate random math problem
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        problem = f"{num1} {operation} {num2}"

        return render_template('math_game.html', problem=problem)
    elif request.method == 'POST':
        # Check user's answer
        user_answer = request.form['answer']
        try:
            user_answer = int(user_answer)
            correct_answer = eval(request.form['problem'])
            result = "Correct!" if user_answer == correct_answer else "Incorrect. Try again."
        except:
            result = "Invalid input. Please enter a number."

        return render_template('math_game.html', problem=request.form['problem'], result=result)

@app.route('/exit')
def exit_game():
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
