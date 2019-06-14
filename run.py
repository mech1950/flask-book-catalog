from application import create_app, db  # from the application package __init__
from application.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('prod')  # This is where we define the desired configuration using .py file in config directory
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name="harry").first():
            User.create_user(user='harry',
                             email='harry@potters.com',
                             password='secret')
    flask_app.run()
