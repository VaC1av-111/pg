from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .models import Rate, db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        codes = db.session.query(Rate.code).distinct().all()
        codes = [code[0] for code in codes]
        return f"Available codes: {', '.join(codes)}"
        
        
    return app
app = Flask(__name__)



@app.route("/")
def home():
    return "Hello!"




if __name__ == "__main__":
    app.run(debug=True)