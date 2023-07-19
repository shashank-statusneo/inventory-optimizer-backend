from main.db import BaseModel, db


class DistanceMatrix(BaseModel):
    """
    Model for Distance Matrix
    """

    __tablename__ = "distance_matrix"

    start_node = db.Column(db.String(50), nullable=False)
    end_node = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)


class SourceCoordinates(BaseModel):

    """
    Model for Source Coordinates
    """

    __tablename__ = "source_coordinates"

    hub_id = db.Column(db.String(50), nullable=False)
    hub_latitude = db.Column(db.String(50), nullable=False)
    hub_longitude = db.Column(db.String(50), nullable=False)


class DestinationCoordinates(BaseModel):

    """
    Model for Destination Coordinates
    """

    __tablename__ = "destination_coordinates"

    destination_id = db.Column(db.String(50), nullable=False)
    destination_latitude = db.Column(db.String(50), nullable=False)
    destination_longitude = db.Column(db.String(50), nullable=False)


class FleetDetails(BaseModel):
    """
    Model for Fleet Details
    """

    __tablename__ = "fleet_details"

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

    vehicle_id = db.Column(db.String(50), nullable=False)
    availability_start_time = db.Column(db.DateTime(), nullable=False)
    availability_end_time = db.Column(db.DateTime(), nullable=False)


class OrderDetails(BaseModel):
    """
    Model for Order Details
    """

    __tablename__ = "order_details"

    order_id = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    order_weight = db.Column(db.Double(), nullable=False)
    order_volume = db.Column(db.Double(), nullable=False)
    delivery_slot_start_time = db.Column(db.DateTime(), nullable=False)
    delivery_slot_end_time = db.Column(db.DateTime(), nullable=False)
    special_vehicle_requirements = db.Column(db.String(50), nullable=False)
