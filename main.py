from sanic import Sanic
from sanic_motor import BaseModel
from sanic_transmute import add_swagger

from api import api

app = Sanic(__name__)
motor_settings = dict(
    MOTOR_URI="mongodb://0.0.0.0:27017/smokeless",
    LOGO=None,
)
app.config.update(motor_settings)
BaseModel.init_app(app)
app.blueprint(api)


if __name__ == "__main__":
    add_swagger(app, "/api/v1/swagger.json", "/api/v1/")
    app.run(host="0.0.0.0", port=8000)
