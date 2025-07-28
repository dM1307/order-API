from app import create_app, db

app = create_app()


@app.before_first_request
def init_db():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
