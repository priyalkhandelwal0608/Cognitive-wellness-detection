from flask import Flask, render_template, request
from utils.state_classifier import classify_state
from recommender.rl_engine import recommend_activity

app = Flask(__name__, template_folder="../frontend/templates")

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    state = None

    if request.method == "POST":
        text = request.form.get("text_input", "")
        step_count = int(request.form.get("step_count", 0))
        heart_rate = int(request.form.get("heart_rate", 0))

        # classify state
        state = classify_state(text, step_count, heart_rate)
        # get recommendation
        recommendation = recommend_activity(state)

    return render_template("index.html", recommendation=recommendation, state=state)

if __name__ == "__main__":
    app.run(debug=True)