from sanic import Sanic

import settings

from health.blueprint import blueprint as health_blueprint
from todo.blueprint import blueprint as todo_blueprint
from reminder.blueprint import blueprint as reminder_blueprint


app = Sanic(__name__)

# -- register blueprints -- #
app.blueprint(health_blueprint)
app.blueprint(todo_blueprint)
app.blueprint(reminder_blueprint)


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT)
