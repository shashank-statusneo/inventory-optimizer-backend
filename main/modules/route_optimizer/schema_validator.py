from marshmallow import Schema, fields
from marshmallow.validate import OneOf


class RouteUploadSchema(Schema):
    """
    Schema to add inventory file to the database.
    """

    file_type = fields.String(
        validate=OneOf(
            [
                "distance_matrix",
                "source_coordinates",
                "destination_coordinates",
                "fleet_details",
                "vehicle_availability",
                "order_details",
            ]
        ),
        required=True,
    )
    user_id = fields.Integer(required=False)


class RouteOptimizationApiSchema(Schema):
    """
    Schema to validate api request to calculate route optimization.
    """

    distance_matrix_master_id = fields.Integer(required=False)
    source_coordinates_master_id = fields.Integer(required=False)
    destination_coordinates_master_id = fields.Integer(required=False)
    fleet_details_master_id = fields.Integer(required=False)
    vehicle_availability_master_id = fields.Integer(required=False)
    order_details_master_id = fields.Integer(required=False)

    travelled_time = fields.Float(required=False)
    travelled_distance = fields.Float(required=False)
    fixed_cost = fields.Float(required=False)
    variable_cost = fields.Float(required=False)
    total_cost = fields.Float(required=False)

    default = fields.Boolean(required=False)
    vehicle_weight_capacity = fields.Boolean(required=False)
    vehicle_volume_capacity = fields.Boolean(required=False)
    vehicle_order_capacity = fields.Boolean(required=False)
    break_time_of_vehicle = fields.Boolean(required=False)
    max_travel_distance = fields.Boolean(required=False)
    max_travel_duration = fields.Boolean(required=False)
    customer_TW_constraint = fields.Boolean(required=False)
    vehicle_TW_constraint = fields.Boolean(required=False)
    infinite_vehicles_available = fields.Boolean(required=False)
    pickup_delivery = fields.Boolean(required=False)
    split_delivery = fields.Boolean(required=False)

    user_id = fields.Integer(required=False)
