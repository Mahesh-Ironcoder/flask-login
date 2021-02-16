from app import APP, db
from app.models import User

@APP.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}