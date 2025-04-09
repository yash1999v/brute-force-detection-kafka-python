from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    log_file_path = 'logs/alerts.log'
    failed_ips = {}
    last_seen = {}

    try:
        with open(log_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "BRUTE FORCE DETECTED" in line:
                    parts = line.strip().split()
                    ip = parts[-1]
                    
                    # Extract timestamp from log line
                    timestamp = parts[0] + " " + parts[1]
                    
                    failed_ips[ip] = failed_ips.get(ip, 0) + 1
                    last_seen[ip] = timestamp  # Always update to latest timestamp
    except Exception as e:
        print(f"Error reading log file: {e}")

    return render_template('index.html', failed_ips=failed_ips, last_seen=last_seen)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
