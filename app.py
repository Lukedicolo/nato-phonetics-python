from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        return redirect(url_for('index', result=result))

    result = generate_nato(quote)
    return render_template('index.html', result=result)


def generate_nato(quote):
    # Conversion table for letters, numbers.
    dict =  {
    'A': 'Alpha',  'B': 'Bravo',   'C': 'Charlie',
    'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
    'G': 'Golf',   'H': 'Hotel',   'I': 'India',
    'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',   'N': 'November','O': 'Oscar',
    'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
    'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu',    '1': 'One',
    '2': 'Two',    '3': 'Three',   '4': 'Four',
    '5': 'Five',   '6': 'Six',     '7': 'Seven',
    '8': 'Eight',  '9': 'Nine',    '0': 'Zero', 
    ' ': '  ','-': 'dash',    '.': 'dot',
    '/': 'slash',  ',': 'comma'}

    res = [dict[x] for x in list(quote.upper())]
    return ' '.join(res)