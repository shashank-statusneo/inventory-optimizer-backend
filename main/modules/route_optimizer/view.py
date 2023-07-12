from flask import jsonify, make_response, request

# from flask_jwt_extended import jwt_required
from flask_restx import Namespace
from flask_restx import Resource


from main.modules.route_optimizer.controller import DistanceMatrixController

from main.modules.route_optimizer.schema_validator import RouteUploadSchema

# from main.modules.auth.controller import AuthUserController
from main.utils import (
    get_data_from_request_or_raise_validation_error,
    csv_to_dict,
)
from main.exceptions import CustomValidationError


class RouteUploadApi(Resource):
    # method_decorators = [jwt_required()]

    def post(self):
        """
        This function is used to add a new inventory to the database.
        :return:
        """
        # auth_user = AuthUserController.get_current_auth_user()

        request_data = get_data_from_request_or_raise_validation_error(
            RouteUploadSchema, request.form
        )
        request_files = request.files
        if not request_files or not request_files.get("file"):
            raise CustomValidationError("Upload File is missing")

        raw_file = request_files.get("file")

        upload_data = csv_to_dict(csv_file=raw_file)
        for item in upload_data:
            item["created_by"] = request_data.get("user_id")

        match request_data.get("file_type"):
            case "distance_matrix":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_distance_matrix(upload_data)
            case "source_coordinates":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_source_coordinates(
                    upload_data
                )
            case "destination_coordinates":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_destination_coordinates(
                    upload_data
                )
            case "fleet_details":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_fleet_details(upload_data)
            case "vehicle_availability":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_vehicle_availability(
                    upload_data
                )
            case "order_details":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_order_details(upload_data)

        response = make_response(
            jsonify({"message": "File uploaded successfully"}),
            201,
        )
        return response


route_namespace = Namespace("route", description="Route Operations")
route_namespace.add_resource(RouteUploadApi, "/upload")
