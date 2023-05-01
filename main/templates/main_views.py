from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/')
def hello():
    return 'Hello Views!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))