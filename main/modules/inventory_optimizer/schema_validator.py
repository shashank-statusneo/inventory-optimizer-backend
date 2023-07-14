from marshmallow import Schema, fields
from marshmallow.validate import OneOf


class InventoryUploadSchema(Schema):
    """
    Schema to add inventory file to the database.
    """

    file_type = fields.String(
        validate=OneOf(["demand_forecast", "vendor"]), required=True
    )
    user_id = fields.Integer(required=False)
