from flask import Flask, render_template, request, session,redirect,url_for
import os
import json

def convert_txt_to_json(txt_file, json_file):
    data = []
    with open(txt_file, 'r', encoding='utf-8') as file:
        for line in file:
            if '\t' in line:
                question, answer = line.strip().split('\t')
                data.append({"question": question, "answer": answer})

    with open(json_file, 'w', encoding='utf-8') as out_file:
        json.dump(data, out_file, ensure_ascii=False, indent=2)


convert_txt_to_json('dialogs.txt', 'chat_data.json')

app = Flask(__name__)
app.secret_key = "secret-key"

if os.path.exists("chat_data.json"):
    with open("chat_data.json", "r") as f:
        data_list = json.load(f)
        memory = {item["question"]: item["answer"] for item in data_list}
else:
    memory = {}


@app.route("/", methods=["GET", "POST"])
def chat():
    if "history" not in session:
        session["history"] = []

    response = ""
    if request.method == "POST":
        user_input = request.form["message"].strip().lower()
        session["history"].append(f"You: {user_input}")

        if user_input in memory:
            response = memory[user_input]
        else:
            response = "I don't know how to answer yet."
            session["pending"] = user_input

        session["history"].append(f"Bot: {response}")

    return render_template("chat.html", history=session["history"], pending=session.get("pending"))

@app.route("/learn", methods=["POST"])
def learn():
    global memory
    if "answer" not in request.form:
        return redirect(url_for("chat"))

    user_answer = request.form["answer"].strip()
    question = session.pop("pending", None)
    if question:

        memory[question] = user_answer

        data_list = [{"question": k, "answer": v} for k, v in memory.items()]
        with open("chat_data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=2)


        with open("chat_data.json", "r", encoding="utf-8") as f:
            data_list = json.load(f)
            memory = {item["question"]: item["answer"] for item in data_list}


        session["history"].append(f"You: {user_answer}")
        session["history"].append("I have memorized the answer.")
        session["history"].append(f"Bot: {user_answer}")

    return redirect(url_for("chat"))
@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('chat'))
if __name__ == "__main__":
    app.run(debug=True)
