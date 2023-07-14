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
