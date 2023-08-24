import os

import pytest

from main.modules.warehouse_manpower.controller import WarehouseController


@pytest.fixture(scope="function")
def add_fixtures(load_data_to_model_using_controller_from_file):
    load_data_to_model_using_controller_from_file(
        WarehouseController.add_warehouses,
        "integration_tests/fixtures/warehouses.json",
    )


def test_add_and_get_warehouses(client, add_fixtures):
    response = client.post(
        "/optimization-api/wmp/warehouses",
        json={
            "warehouses": [
                {"name": "Warehouse E", "description": "Warehouse E"},
                {"name": "Warehouse F", "description": "Warehouse F"},
                {"name": "Warehouse G", "description": "Warehouse G"},
            ]
        },
    )
    assert response.status_code == 201

    response = client.get("/optimization-api/wmp/warehouses")
    assert response.status_code == 200
    assert len(response.json) == 5


def test_upload_get_and_update_benchmark_productivity(client, add_fixtures):
    test_file_dir = os.path.abspath(os.path.dirname(__file__)).replace(
        "integration_tests", "xls_files"
    )
    # Upload from a file.

    # Invalid warehouse id
    response = client.post(
        "/optimization-api/wmp/upload_productivity_file/100"
    )
    assert response.status_code == 403

    # Without any file.
    response = client.post("/optimization-api/wmp/upload_productivity_file/1")
    assert response.status_code == 400
    assert response.json == {"error": "No file uploaded."}

    # Invalid File Extension
    with open(test_file_dir + "/invalid_file.txt", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {"error": "Invalid file extension."}

    # Invalid File with Extra Columns
    with open(test_file_dir + "/Invalid_Productivity.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {"error": "Extra columns: {'extra_column'}."}

    # Invalid File with missing required columns
    with open(
        test_file_dir + "/Invalid_Productivity_Missing_Column.xlsx", "rb"
    ) as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {
        "error": "Missing columns: {'productivity_new_employee'}."
    }

    # Invalid File with Invalid column value
    with open(
        test_file_dir + "/Invalid_Value_Productivity.xlsx", "rb"
    ) as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {"error": ["Invalid value(s) for : category 8"]}

    # Valid File
    with open(test_file_dir + "/Productivity.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 201

    # Get benchmark productivity

    response = client.get("/optimization-api/wmp/benchmark_productivity/1")
    assert response.status_code == 200
    assert len(response.json) == 24
    assert response.json[0]["productivity_new_employee"] == 70
    benchmark_productivity_id = response.json[0]["id"]

    # Update benchmark productivity

    data = {
        "productivity": [
            {"id": benchmark_productivity_id, "productivity_new_employee": 80}
        ]
    }
    response = client.put(
        "/optimization-api/wmp/benchmark_productivity", json=data
    )
    assert response.status_code == 200

    # Check if the value got updated or not

    response = client.get("/optimization-api/wmp/benchmark_productivity/1")
    assert response.status_code == 200
    assert response.json[0]["productivity_new_employee"] == 80


def test_upload_get_and_test_demands(client, add_fixtures):
    test_file_dir = os.path.abspath(os.path.dirname(__file__)).replace(
        "integration_tests", "xls_files"
    )
    # Upload from a file.

    # Invalid warehouse id
    response = client.post("/optimization-api/wmp/demand_forecast_file/100")
    assert response.status_code == 403

    # Without any file.
    response = client.post("/optimization-api/wmp/demand_forecast_file/1")
    assert response.status_code == 400
    assert response.json == {"error": "No file uploaded."}

    # Invalid File Extension
    with open(test_file_dir + "/invalid_file.txt", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {"error": "Invalid file extension."}

    # Missing Date Column.
    with open(
        test_file_dir + "/Invalid_Demand_Missing_Date.xlsx", "rb"
    ) as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {"error": "Date column is missing"}

    # Invalid Demand Category
    with open(test_file_dir + "/Productivity.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 201

    with open(test_file_dir + "/Invalid_Demand_Categories.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {
        "error": "Invalid categories : [['invalid category', 'invalid category 2']]"
    }

    # Without passing start_date and end_date
    with open(test_file_dir + "/Invalid_Demand_Value.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {
        "error": "start_date and end_date should be present in form data of requests"
    }

    # Invalid Demand value
    with open(test_file_dir + "/Invalid_Demand_Value.xlsx", "rb") as file:
        files = {
            "file": file,
            "start_date": "2023-05-24",
            "end_date": "2023-05-31",
        }
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 400
    assert response.json == {
        "error": [
            "Invalid Demand (276sd) for date : 2023-05-31 category : category 1"
        ]
    }

    # Valid File
    with open(test_file_dir + "/Demand.xlsx", "rb") as file:
        files = {
            "file": file,
            "start_date": "2023-05-24",
            "end_date": "2023-05-31",
        }
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 201

    # Get demands

    response = client.get(
        "/optimization-api/wmp/demands/1?start_date=2023-05-24"
    )
    assert response.status_code == 400
    assert response.json == {
        "error": "start_date and end_date are required parameters"
    }

    response = client.get(
        "/optimization-api/wmp/demands/1?start_date=2023-05-24&end_date=2023-05-31"
    )
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert "total" in response.json
    assert len(response.json.keys()) == 9
    assert response.json["2023-05-24"]["category 1"]["demand"] == 269

    demand_id = response.json["2023-05-24"]["category 1"]["id"]

    #  Update Demand
    data = {"demands": [{"id": demand_id, "demand": 900}]}
    response = client.put("/optimization-api/wmp/demands", json=data)
    assert response.status_code == 200

    response = client.get(
        "/optimization-api/wmp/demands/1?start_date=2023-05-24&end_date=2023-05-31"
    )
    assert response.status_code == 200
    assert response.json["2023-05-24"]["category 1"]["demand"] == 900


def test_calculate_result(client, add_fixtures, monkeypatch):
    test_file_dir = os.path.abspath(os.path.dirname(__file__)).replace(
        "integration_tests", "xls_files"
    )

    with open(test_file_dir + "/Productivity.xlsx", "rb") as file:
        files = {"file": file}
        response = client.post(
            "/optimization-api/wmp/upload_productivity_file/1", data=files
        )
    assert response.status_code == 201

    with open(test_file_dir + "/Demand.xlsx", "rb") as file:
        files = {
            "file": file,
            "start_date": "2023-05-24",
            "end_date": "2023-05-31",
        }
        response = client.post(
            "/optimization-api/wmp/demand_forecast_file/1", data=files
        )
    assert response.status_code == 201

    def mocked_f(input_date):
        return True

    monkeypatch.setattr(
        "main.utils.greater_or_equal_to_current_date", mocked_f
    )

    input_requirements = {
        "warehouse_id": 1,
        "num_current_employees": 10,
        "plan_from_date": "2023-08-24",
        # update to current date to pass test
        "plan_to_date": "2023-08-31",
        # update to date more than plan_from_date to pass test
        "percentage_absent_expected": 5,
        "day_working_hours": 8,
        "cost_per_employee_per_month": 10000,
        "total_hiring_budget": 200000,
    }
    response = client.post(
        "/optimization-api/wmp/calculate", json=input_requirements
    )
    assert response.status_code == 200
