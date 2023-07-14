from main.modules.route_optimizer.model import (
    DistanceMatrix,
    SourceCoordinates,
    DestinationCoordinates,
    FleetDetails,
    VehicleAvailability,
    OrderDetails,
)


class DistanceMatrixController:
    """
    This is the controller class which is used to handle all the logical and CURD operations.
    """

    @classmethod
    def add_distance_matrix(cls, distance_matrix_data: list):
        """
        This function is used to add new distance matrix.
        :param distance_matrix_data:
        :return int:
        """
        distance_matrix = DistanceMatrix.bulkcreate(distance_matrix_data)
        return distance_matrix

    @classmethod
    def add_source_coordinates(cls, source_coordinates_data: list):
        """
        This function is used to add new source coordinates.
        :param source_coordinates_data:
        :return int:
        """
        source_coordinates = SourceCoordinates.bulkcreate(
            source_coordinates_data
        )
        return source_coordinates

    @classmethod
    def add_destination_coordinates(cls, destination_coordinates_data: list):
        """
        This function is used to add new destination coordinates.
        :param destination_coordinates_data:
        :return int:
        """
        destination_coordinates = DestinationCoordinates.bulkcreate(
            destination_coordinates_data
        )
        return destination_coordinates

    @classmethod
    def add_fleet_details(cls, fleet_details_data: list):
        """
        This function is used to add new fleet details.
        :param fleet_details_data:
        :return int:
        """
        fleet_details = FleetDetails.bulkcreate(fleet_details_data)
        return fleet_details

    @classmethod
    def add_vehicle_availability(cls, vehicle_availability_data: list):
        """
        This function is used to add new vehicle availability.
        :param vehicle_availability_data:
        :return int:
        """
        vehicle_availability = VehicleAvailability.bulkcreate(
            vehicle_availability_data
        )
        return vehicle_availability

    @classmethod
    def add_order_details(cls, order_details_data: list):
        """
        This function is used to add new order details.
        :param order_details_data:
        :return int:
        """
        order_details = OrderDetails.bulkcreate(order_details_data)
        return order_details
