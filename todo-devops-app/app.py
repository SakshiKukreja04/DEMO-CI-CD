from datetime import datetime
from itertools import count

from flask import Flask, redirect, render_template, request, url_for


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["TASKS"] = []
    app.config["TASK_ID_COUNTER"] = count(1)

    @app.get("/")
    def index() -> str:
        tasks = app.config["TASKS"]
        return render_template("index.html", tasks=tasks)

    @app.post("/tasks")
    def add_task():
        task_title = request.form.get("task", "").strip()
        if task_title:
            task = {
                "id": next(app.config["TASK_ID_COUNTER"]),
                "title": task_title,
                "created_at": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            }
            app.config["TASKS"].insert(0, task)
        return redirect(url_for("index"))

    @app.post("/tasks/<int:task_id>/delete")
    def delete_task(task_id: int):
        tasks = app.config["TASKS"]
        app.config["TASKS"] = [task for task in tasks if task["id"] != task_id]
        return redirect(url_for("index"))

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
