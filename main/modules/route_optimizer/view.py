from flask import jsonify, make_response, request
from json import dumps

from flask_restx import Namespace
from flask_restx import Resource


from main.modules.route_optimizer.controller import (
    RouteMasterDataController,
    DistanceMatrixController,
    SourceCoordinatesController,
    DestinationCoordinatesController,
    FleetDetailsController,
    VehicleAvailabilityController,
    OrderDetailsController,
    RouteOptimizationApiController,
)

from main.modules.route_optimizer.schema_validator import (
    RouteUploadSchema,
    RouteOptimizationApiSchema,
)
from main.modules.route_optimizer.mock_api_result import api_response

from main.utils import (
    get_data_from_request_or_raise_validation_error,
    csv_to_dict,
)
from main.exceptions import CustomValidationError


class AlgorithmMockApi(Resource):
    def post(self):
        """
        Mock API for create algorithm result
        """
        request_data = get_data_from_request_or_raise_validation_error(
            RouteOptimizationApiSchema, request.json
        )

        request_data.update({"created_by": request_data.get("user_id")})
        request_data.pop("user_id", None)

        result_id = RouteOptimizationApiController.add_optimization(
            request_data
        )

        response = make_response(
            jsonify(
                {"id": result_id, "message": "Route plan created successfully"}
            ),
            201,
        )
        return response

    def get(self, result_id: int):
        """
        Mock API for get algorithm result
        """
        route_result = (
            RouteOptimizationApiController.get_route_result_by_result_id(
                result_id
            )
        )
        response_data = api_response if route_result else {}
        return make_response(jsonify(response_data), 200)


class RouteUploadApi(Resource):
    def post(self):
        """
        This function is used to add a new inventory to the database.
        :return:
        """

        request_data = get_data_from_request_or_raise_validation_error(
            RouteUploadSchema, request.form
        )
        request_files = request.files
        if not request_files or not request_files.get("file"):
            raise CustomValidationError("Upload File is missing")

        raw_file = request_files.get("file")

        upload_data = csv_to_dict(csv_file=raw_file)

        master_data = {
            "file_object": dumps(upload_data).encode(),
            "file_name": raw_file.filename,
            "file_type": request_data.get("file_type"),
            "file_ext": raw_file.mimetype,
        }

        master_data.update({"created_by": request_data.get("user_id")})

        master_id = RouteMasterDataController.add_master_data(master_data)

        for item in upload_data:
            item["master_id"] = master_id
            item["created_by"] = request_data.get("user_id")

        match request_data.get("file_type"):
            case "distance_matrix":
                # TODO: Filter data and apply validation
                _ = DistanceMatrixController.add_distance_matrix(upload_data)
            case "source_coordinates":
                # TODO: Filter data and apply validation
                _ = SourceCoordinatesController.add_source_coordinates(
                    upload_data
                )
            case "destination_coordinates":
                # TODO: Filter data and apply validation
                _ = DestinationCoordinatesController.add_destination_coordinates(
                    upload_data
                )
            case "fleet_details":
                # TODO: Filter data and apply validation
                _ = FleetDetailsController.add_fleet_details(upload_data)
            case "vehicle_availability":
                # TODO: Filter data and apply validation
                _ = VehicleAvailabilityController.add_vehicle_availability(
                    upload_data
                )
            case "order_details":
                # TODO: Filter data and apply validation
                _ = OrderDetailsController.add_order_details(upload_data)

        response = make_response(
            jsonify(
                {
                    "message": "File uploaded successfully",
                    "master_id": master_id,
                }
            ),
            201,
        )
        return response


route_namespace = Namespace(
    "optimization-api/route", description="Route Operations"
)
route_namespace.add_resource(AlgorithmMockApi, "/mock/algorithm")
route_namespace.add_resource(
    AlgorithmMockApi, "/mock/algorithm/<int:result_id>"
)
route_namespace.add_resource(RouteUploadApi, "/upload")
