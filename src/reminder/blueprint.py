from sanic.blueprints import Blueprint


blueprint = Blueprint('reminders', url_prefix='/reminders', strict_slashes=False)

# register controllers
from reminder import controller
