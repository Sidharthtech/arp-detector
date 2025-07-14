from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def show_logs():
    with open("log.txt", "r") as log_file:
        recent_entries = log_file.readlines()[-20:]
    return render_template_string("""
    <h1>ARP Spoofing Log</h1>
    <pre>{{ log_data }}</pre>
    """, log_data="".join(recent_entries))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
