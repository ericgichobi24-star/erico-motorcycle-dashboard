from rich.console import Console
from rich.table import Table
from rich.live import Live
import time, random

console = Console()

def get_bike_data():
    return {
        "mode": random.choice(["ECO", "NORMAL", "SPORT"]),
        "battery": random.randint(45, 100),
        "speed": random.randint(0, 60),
        "power": random.randint(20, 95),
        "temp": random.randint(30, 65)
    }

with Live(console=console, refresh_per_second=2) as live:
    while True:
        data = get_bike_data()
        table = Table(title="ERICO TECH - E-MOTORCYCLE DASHBOARD")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="bold green")
        table.add_row("Mode", data["mode"])
        table.add_row("Battery", f"{data['battery']}%")
        table.add_row("Speed", f"{data['speed']} km/h")
        table.add_row("Power", f"{data['power']}%")
        table.add_row("Motor Temp", f"{data['temp']}C")
        live.update(table)
        time.sleep(0.5)
