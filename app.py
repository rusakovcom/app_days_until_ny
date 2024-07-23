# run with
# gunicorn -w 4 -b 0.0.0.0:5000 --log-level=debug --access-logfile - app:app

# apt install python3 python3-pip
# pip3 install -r requirements.txt (Flask, gunicorn)
   
from flask import Flask
from datetime import date, datetime
from urllib.parse import quote as url_quote

# --- GET NUMBER OF DAYS FUNCTION

def days_until_new_year():
    today = datetime.today()
    new_year = datetime(year=today.year + 1, month=1, day=1)
    delta = (new_year - today).days
    return delta

# --- RUN APP

app = Flask(__name__)

@app.route('/get_date', methods=['GET'])   # only get requests curl http://109.207.173.22:5000/get_date ,return needs to be string
def count_days():
    return f'пацаны до нового года {days_until_new_year()} дней'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
