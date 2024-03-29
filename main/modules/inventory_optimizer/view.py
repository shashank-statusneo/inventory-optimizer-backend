from flask import jsonify, make_response, request

from flask_restx import Namespace
from flask_restx import Resource
from json import dumps


from main.modules.inventory_optimizer.controller import (
    MasterDataController,
    DemandForecastController,
    VendorController,
)
from main.modules.inventory_optimizer.schema_validator import (
    InventoryUploadSchema,
)

from main.utils import (
    get_data_from_request_or_raise_validation_error,
    csv_to_dict,
)
from main.exceptions import CustomValidationError

from main.modules.inventory_optimizer.mock_api_result import api_response


class AlgorithmMockApi(Resource):
    def post(self):
        """
        Mock API for algorithm result
        """
        response = make_response(jsonify({"data": api_response}), 200)
        return response


class InventoryUploadApi(Resource):
    def post(self):
        """
        This function is used to add a new inventory to the database.
        :return:
        """

        request_data = get_data_from_request_or_raise_validation_error(
            InventoryUploadSchema, request.form
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

        master_id = MasterDataController.add_master_data(master_data)

        for item in upload_data:
            item["master_id"] = master_id
            item["created_by"] = request_data.get("user_id")

        match request_data.get("file_type"):
            case "demand_forecast":
                # TODO: Filter data and apply validation
                _ = DemandForecastController.add_demand_forecast(upload_data)
            case "vendor":
                # TODO: Filter data and apply validation
                _ = VendorController.add_vendor(upload_data)

        response = make_response(
            jsonify({"message": "Inventory added", "master_id": master_id}),
            201,
        )
        return response


algorithm_mock_namespace = Namespace(
    "optimization-api", description="Mock Api for Algorithm"
)
algorithm_mock_namespace.add_resource(AlgorithmMockApi, "/mock/algorithm")

inventory_namespace = Namespace(
    "optimization-api/inventory", description="Inventory Operations"
)
inventory_namespace.add_resource(InventoryUploadApi, "/upload")
