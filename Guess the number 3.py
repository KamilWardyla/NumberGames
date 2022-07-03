from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_guess_the_number():
    return """
        <label> Imagine a number between 0 and 1000!
        <form action=/ method="POST"
            Imagine a number between 0 and 1000! <br/>
            <input type='hidden' name='big' value='1000'>
            <input type='hidden' name='small' value='0'>
            <button name="Choice" value="To small" id='to_small'> To small</button>
            <button name="Choice" value="To Big" id='to_big'> To Big</button>
            <button name="Choice" value="You win" id='you_win'> You win</button>
            <br/>
        </label>
        </form> 
    """


@app.route("/", methods=["POST"])
def guess_the_number_2(big=1000, small=0, guess_number=0):
    guess_number = int((big - small) / 2 + small)
    if request.form.get("Choice") == "To small":
        small = guess_number
        print(f"small number: {small}")
        guess_number = int((big - small) / 2 + small)
        return format(guess_number)
    elif request.form.get("Choice") == "To Big":
        big = guess_number
        guess_number = int((big - small) / 2 + small)
        return format(guess_number)
    elif request.form.get("Choice") == "You win":
        return "You win!"


if __name__ == "__main__":
    app.run(debug=True)
