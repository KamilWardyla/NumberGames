from flask import Flask
from flask import request
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_guess_the_number():
    return """
        <label> Imagine a number between 0 and 1000!
        <form action=/ method="POST"
            Imagine a number between 0 and 1000! <br/>
            <button name="to_small" value="To small" onclick="you_small()" id='to_small'> To small</button>
            <button name="to_big" value="To Big" onclick="to_big()" id='to_big' > To Big</button>
            <button name="you_win" value="You win" onclick="you_win()" id='you_win'> You win</button>
            <br/>
        </label>
        </form> 
    """


def to_small():
    if guess_number > small:
        small = guess_number
    guess_number = random.randint(last_number, big)
    i += 1


def to_big():
    if guess_number < big:
        big = guess_number
    guess_number = random.randint(small, last_number)
    i += 1


def you_win():
    return "You win!"


@app.route("/", methods=["POST"])
def guess_the_number_2():
    global guess_the_number_2
    guess_number = random.randrange(0, 1000)
    global big
    big = 1000
    global small
    small = 0
    i = 1
    global last_number
    last_number = 0
    while i < 11:
        if i == 1:
            guess_number = 500
        last_number = guess_number
        if request.form.get("to_small") == "To small":
            to_small()
        elif request.form.get("to_big") == "To Big":
            to_big()
        elif request.form.get("you_win") == "You win":
            you_win()
        last_number = guess_number
    return "You lost"


if __name__ == "__main__":
    app.run(debug=True)
