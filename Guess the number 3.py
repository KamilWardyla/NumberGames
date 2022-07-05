"""Warsztat: Gra w zgadywanie liczb 3
Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy frameworka Flask. Użytkownik dostaje do dyspozycji formularz z trzema guzikami: To small, To big, You win.

Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).

Uwaga – nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla, np. przy pomocy Firebuga. W tej sytuacji jednak zupełnie wystarczające. Najwyżej zepsuje sobie zabawę ;)"""

from flask import Flask, request, render_template

app = Flask(__name__)

BIG = 1000
SMALL = 0


def guess(big=1000, small=0, guess_number=0):
    return int((big - small) / 2 + small)


GUESS_NUMBER = guess()


@app.route("/", methods=["GET", "POST"])
def guess_the_number_2():
    global GUESS_NUMBER, BIG, SMALL
    if request.form.get("Choice") == "To small":
        small = GUESS_NUMBER
        GUESS_NUMBER = int((BIG - small) / 2 + small)
        msg = "Number is too small"
    elif request.form.get("Choice") == "To Big":
        big = GUESS_NUMBER
        GUESS_NUMBER = int((big - SMALL) / 2 + SMALL)
        msg = "Number is too big"
    elif request.form.get("Choice") == "You win":
        return render_template("win.html", number=GUESS_NUMBER)
    return render_template("index.html", number=GUESS_NUMBER)


if __name__ == "__main__":
    app.run(debug=True)
