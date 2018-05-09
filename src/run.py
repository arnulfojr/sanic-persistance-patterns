from sanic import Sanic

import settings

from health.blueprint import blueprint as health_blueprint
from todo.blueprint import blueprint as todo_blueprint


app = Sanic(__name__)

# -- register blueprints -- #
app.register_blueprint(health_blueprint)
app.register_blueprint(todo_blueprint)


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT)
