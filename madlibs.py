from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """ Renders game form, and links to game if user wants to play. 
    Displays goodbye if not. """

    wants_to_play = request.args.get("wants_to_play")

    if wants_to_play == "yes":
        # redirect to madlib
        return render_template('game.html')

    else:
        # redirect to goodbye
        return render_template('goodbye.html')

@app.route('/madlib')
def show_madlib():
    """ Renders madlib in new page """

    person = request.args.get('person')
    animals = request.args.getlist('animal')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')

    if not person:
        person = 'A Nony Mouse'

    if color == None:
        color = '#4db6ac'

    if noun == None:
        noun = 'nudibranch'

    if adjective == None:
        adjective = 'malaised'

    return render_template('madlib.html', 
                            person=person,
                            color=color, 
                            noun=noun, 
                            adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
