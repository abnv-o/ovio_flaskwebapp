from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("pcos_self_assess_model.pkl")

features = [
    "Age (yrs)", "Weight (Kg)", "Height(Cm)", "BMI",
    "Cycle length(days)", "Cycle(R/I)",
    "Weight gain(Y/N)", "hair growth(Y/N)",
    "Skin darkening (Y/N)", "Pimples(Y/N)",
    "Fast food (Y/N)", "Reg.Exercise(Y/N)"
]

def preprocess_input(form):
    processed = []
    for feature in features:
        val = form.get(feature)
        if "Y/N" in feature:
            processed.append(1 if val == "1" else 0)
        elif feature in ["Fast food (Y/N)", "Reg.Exercise(Y/N)"]:
            processed.append(int(val))
        else:
            processed.append(float(val))
    return pd.DataFrame([dict(zip(features, processed))])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            df = preprocess_input(request.form)
            prediction = model.predict(df)[0]
            prob = model.predict_proba(df)[0][1]
            result = "⚠️ Risk of PCOS" if prediction == 1 else "✅ No Risk of PCOS"
            color = "red" if prediction == 1 else "green"
            return render_template("result.html", result=result, probability=round(prob, 2), color=color, inputs=request.form)
        except Exception as e:
            return f"❌ Error: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)