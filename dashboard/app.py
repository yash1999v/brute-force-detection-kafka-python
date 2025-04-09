from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts')
def alerts():
    log_file_path = '../consumer/logs/alerts.log'

    alerts_data = []
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            for line in file:
                alerts_data.append(line.strip())

    return render_template('alerts.html', alerts=alerts_data)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
