from main.db import BaseModel, db
from sqlalchemy import BLOB


class RouteMasterData(BaseModel):
    """
    Model for route master data
    """

    __table_name = "route_master_data"
    file_name = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    file_ext = db.Column(db.String(50))
    file_object = db.Column(BLOB)


class DistanceMatrix(BaseModel):
    """
    Model for Distance Matrix
    """

    __tablename__ = "distance_matrix"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_distance_matrix = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_distance_matrix", lazy=True),
    )
    start_node = db.Column(db.String(50), nullable=False)
    end_node = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)


class SourceCoordinates(BaseModel):

    """
    Model for Source Coordinates
    """

    __tablename__ = "source_coordinates"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_source_coordinates = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_source_coordinates", lazy=True),
    )
    hub_id = db.Column(db.String(50), nullable=False)
    hub_latitude = db.Column(db.String(50), nullable=False)
    hub_longitude = db.Column(db.String(50), nullable=False)


class DestinationCoordinates(BaseModel):

    """
    Model for Destination Coordinates
    """

    __tablename__ = "destination_coordinates"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_destination_coordinates = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_destination_coordinates", lazy=True),
    )
    destination_id = db.Column(db.String(50), nullable=False)
    destination_latitude = db.Column(db.String(50), nullable=False)
    destination_longitude = db.Column(db.String(50), nullable=False)


class FleetDetails(BaseModel):
    """
    Model for Fleet Details
    """

    __tablename__ = "fleet_details"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_fleet_details = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_fleet_details", lazy=True),
    )
    vehicle_type = db.Column(db.String(50), nullable=False)
    vehicle_count = db.Column(db.Integer(), nullable=False)
    fixed_cost = db.Column(db.Float(), nullable=False)
    variable_cost_per_km = db.Column(db.Float(), nullable=False)
    capacity_kg = db.Column(db.Float(), nullable=False)
    avg_speed_kmph = db.Column(db.Float(), nullable=False)
    characteristics = db.Column(db.String(50))


class VehicleAvailability(BaseModel):
    """
    Model for Vehicle Availability
    """

    __tablename__ = "vehicle_availability"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_vehicle_availability = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_vehicle_availability", lazy=True),
    )
    vehicle_id = db.Column(db.String(50), nullable=False)
    availability_start_time = db.Column(db.DateTime(), nullable=False)
    availability_end_time = db.Column(db.DateTime(), nullable=False)


class OrderDetails(BaseModel):
    """
    Model for Order Details
    """

    __tablename__ = "order_details"

    master_id = db.Column(db.ForeignKey("route_master_data.id"))
    master_order_details = db.relationship(
        "RouteMasterData",
        backref=db.backref("master_order_details", lazy=True),
    )
    order_id = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    order_weight = db.Column(db.Double(), nullable=False)
    order_volume = db.Column(db.Double(), nullable=False)
    delivery_slot_start_time = db.Column(db.DateTime(), nullable=False)
    delivery_slot_end_time = db.Column(db.DateTime(), nullable=False)
    special_vehicle_requirements = db.Column(db.String(50), nullable=False)


class RouteResult(BaseModel):
    """
    Model for Route Result
    """

    __tablename__ = "route_result"

    distance_matrix_master_id = db.Column(db.Integer, nullable=True)
    source_coordinates_master_id = db.Column(db.Integer, nullable=True)
    destination_coordinates_master_id = db.Column(db.Integer, nullable=True)
    fleet_details_master_id = db.Column(db.Integer, nullable=True)
    vehicle_availability_master_id = db.Column(db.Integer, nullable=True)
    order_details_master_id = db.Column(db.Integer, nullable=True)

    travelled_time = db.Column(db.Float, nullable=True)
    travelled_distance = db.Column(db.Float, nullable=True)
    fixed_cost = db.Column(db.Float, nullable=True)
    variable_cost = db.Column(db.Float, nullable=True)
    total_cost = db.Column(db.Float, nullable=True)
    default = db.Column(db.Boolean, default=True)
    vehicle_weight_capacity = db.Column(db.Boolean, default=True)
    vehicle_volume_capacity = db.Column(db.Boolean, default=True)
    vehicle_order_capacity = db.Column(db.Boolean, default=True)
    break_time_of_vehicle = db.Column(db.Boolean, default=True)
    max_travel_distance = db.Column(db.Boolean, default=True)
    max_travel_duration = db.Column(db.Boolean, default=True)
    customer_TW_constraint = db.Column(db.Boolean, default=False)
    vehicle_TW_constraint = db.Column(db.Boolean, default=False)
    infinite_vehicles_available = db.Column(db.Boolean, default=False)
    pickup_delivery = db.Column(db.Boolean, default=False)
    split_delivery = db.Column(db.Boolean, default=False)
