# coding:utf-8
from configs import configs
from api import create_app

app = create_app(configs)
app.debug = configs['defaultConfig'].DEBUG
