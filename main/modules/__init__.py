from flask_restx import Api

from main.modules.warehouse_manpower.view import wmp_namespace
from main.modules.inventory_optimizer.view import (
    inventory_namespace,
    algorithm_mock_namespace,
)
from main.modules.route_optimizer.view import route_namespace


api = Api()


api.add_namespace(wmp_namespace)
api.add_namespace(inventory_namespace)
api.add_namespace(route_namespace)

api.add_namespace(algorithm_mock_namespace)
