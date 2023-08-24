import os


def test_upload_master_data(client):
    test_file_dir = os.path.abspath(os.path.dirname(__file__)).replace(
        "integration_tests", "xls_files"
    )
    # Without any file.
    response = client.post("/optimization-api/route/upload")
    assert response.status_code == 400
    assert response.json == {
        "error": "{'file_type': ['Missing data for required field.']}"
    }

    # Valid distance matrix File
    with open(test_file_dir + "/distance_matrix.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "distance_matrix",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201

    # Valid source coordinates File
    with open(test_file_dir + "/source_coordinates.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "source_coordinates",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201

    # Valid distance coordinates File
    with open(test_file_dir + "/destination_coordinates.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "destination_coordinates",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201

    # Valid fleet details File
    with open(test_file_dir + "/fleet_details.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "fleet_details",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201

    # Valid vehicle availability File
    with open(test_file_dir + "/vehicle_availability.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "vehicle_availability",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201

    # Valid order details File
    with open(test_file_dir + "/order_details.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "order_details",
            "user_id": 1,
        }
        response = client.post(
            "/optimization-api/route/upload", data=form_data
        )
    assert response.status_code == 201


def test_create_plan(client):
    plan_data = {
        "distance_matrix_master_id": 1,
        "source_coordinates_master_id": 2,
        "destination_coordinates_master_id": 3,
        "fleet_details_master_id": 4,
        "vehicle_availability_master_id": 5,
        "order_details_master_id": 6,
        "travelled_time": 12,
        "travelled_distance": 5000,
        "fixed_cost": 50000,
        "variable_cost": 300,
        "total_cost": 53000,
        "default": True,
        "vehicle_weight_capacity": False,
        "vehicle_volume_capacity": False,
        "vehicle_order_capacity": False,
        "break_time_of_vehicle": False,
        "max_travel_distance": False,
        "max_travel_duration": False,
        "customer_TW_constraint": False,
        "vehicle_TW_constraint": False,
        "infinite_vehicles_available": False,
        "pickup_delivery": False,
        "split_delivery": False,
        "user_id": 1,
    }

    response = client.post(
        "/optimization-api/route/mock/algorithm",
        json=plan_data,
        # headers=headers,
    )
    assert isinstance(response.json, dict)
    assert "id" in response.json

    result_id = response.json["id"]

    assert response.status_code == 201

    # test result
    response = client.get(
        f"/optimization-api/route/mock/algorithm/{result_id}",
    )

    assert response.status_code == 200


# def test_mock_algorithm_data(client):
#     response = client.post("/optimization-api/route/mock/algorithm")
#     assert response.status_code == 200
