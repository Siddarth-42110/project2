from flask import Flask, jsonify

app = Flask(__name__)

def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

@app.route('/leapyear/<int:year>')
def check_leap_year(year):

    return jsonify({'year': year, 'is_leap_year': is_leap_year(year)})

if __name__ == '__main__':
    app.run(debug=True)
