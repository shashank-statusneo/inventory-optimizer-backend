# from flask_jwt_extended import JWTManager
from flask_restx import Api

from main.modules.warehouse_manpower.view import wmp_namespace
from main.modules.inventory_optimizer.view import (
    inventory_namespace,
    algorithm_mock_namespace,
)
from main.modules.route_optimizer.view import route_namespace

# from main.modules.auth.view import auth_namespace
# from main.modules.jwt.controller import JWTController
# from main.modules.user.view import user_namespace

# jwt = JWTManager()
api = Api()

# jwt.token_in_blocklist_loader(JWTController.token_revoked_check)


api.add_namespace(wmp_namespace)
api.add_namespace(inventory_namespace)
api.add_namespace(route_namespace)
# api.add_namespace(auth_namespace)
# api.add_namespace(user_namespace)

api.add_namespace(algorithm_mock_namespace)
