import os


def test_upload_master_data(client):
    test_file_dir = os.path.abspath(os.path.dirname(__file__)).replace(
        "integration_tests", "xls_files"
    )
    # Without any file.
    response = client.post("/inventory/upload")
    assert response.status_code == 400
    assert response.json == {
        "error": "{'file_type': ['Missing data for required field.']}"
    }

    # Valid Demand File
    with open(test_file_dir + "/demand_forecast.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "demand_forecast",
            "user_id": 1,
        }
        response = client.post("/inventory/upload", data=form_data)
    assert response.status_code == 201

    # Valid vendor File
    with open(test_file_dir + "/vendor_data.csv", "rb") as file:
        form_data = {
            "file": file,
            "file_type": "vendor",
            "user_id": 1,
        }
        response = client.post("/inventory/upload", data=form_data)
    assert response.status_code == 201


def test_mock_algorithm_data(client):
    response = client.post("/mock/algorithm")
    assert response.status_code == 200
