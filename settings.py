from datetime import timedelta
from copy import deepcopy

SECRET_KEY = "test"
TOKEN_EXPIRE_IN = 360


CONFIG = {
    "SECRET_KEY": SECRET_KEY,
    "SQLALCHEMY_DATABASE_URI": 'sqlite:///db.sqlite',
    "JWT_SECRET_KEY": "secret",
    "JWT_ACCESS_TOKEN_EXPIRES": timedelta(minutes=TOKEN_EXPIRE_IN),
    "JWT_REFRESH_TOKEN_EXPIRES": timedelta(days=1)
}

TEST_CONFIG = deepcopy(CONFIG)
TEST_CONFIG["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test_db.sqlite',

