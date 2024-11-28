from flask_login import LoginManager

from website_management import app
from database_management import db, User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)