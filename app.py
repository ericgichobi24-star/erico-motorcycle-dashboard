from flask import Flask, render_template_string
import random

app = Flask(__name__)

def get_bike_data():
    return {
        "mode": random.choice(["ECO", "NORMAL", "SPORT"]),
        "battery": random.randint(45, 100),
        "speed": random.randint(0, 60),
        "power": random.randint(20, 95),
        "temp": random.randint(30, 65)
    }

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>ERICO TECH DASHBOARD</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="1">
<style>
body { background:#0a0a0a; color:#00ff88; font-family:monospace; text-align:center; padding:20px; }
.card { border:2px solid #00ff88; border-radius:15px; padding:20px; margin:20px auto; max-width:400px; background:#111; }
h1 { color:#00ff88; text-shadow:0 0 10px #00ff88; }
.metric { display:flex; justify-content:space-between; padding:10px; border-bottom:1px solid #333; font-size:18px; }
.value { font-weight:bold; color:white; }
.eco { color:#00ff88 } .normal { color:#ffcc00 } .sport { color:#ff0044 }
</style>
</head>
<body>
<h1>⚡ ERICO TECH E-MOTORCYCLE</h1>
<div class="card">
<h2 class="{{ data.mode.lower() }}">{{ data.mode }} MODE</h2>
<div class="metric"><span>Battery</span><span class="value">{{ data.battery }}%</span></div>
<div class="metric"><span>Speed</span><span class="value">{{ data.speed }} km/h</span></div>
<div class="metric"><span>Power</span><span class="value">{{ data.power }}%</span></div>
<div class="metric"><span>Motor Temp</span><span class="value">{{ data.temp }}°C</span></div>
</div>
<p>Updates every 1 sec • Running on Termux</p>
</body>
</html>
"""

@app.route("/")
def home():
    data = get_bike_data()
    return render_template_string(HTML, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
