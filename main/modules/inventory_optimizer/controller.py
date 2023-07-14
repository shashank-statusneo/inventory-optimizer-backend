from main.modules.inventory_optimizer.model import (
    MasterData,
    DemandForecast,
    Vendor,
)


class MasterDataController:
    """
    This is the controller class which is used to handle all the logical and CURD operations.
    """

    @classmethod
    def add_master_data(cls, master_data: dict):
        """
        This function is used to add new master data.
        :param master_data:
        :return int:
        """
        master = MasterData.create(master_data)
        return master.id


class DemandForecastController:
    """
    This is the controller class which is used to handle all the logical and CURD operations.
    """

    @classmethod
    def add_demand_forecast(cls, demand_forecast_data: list):
        """
        This function is used to add new demand forecast.
        :param demand_forecast:
        :return int:
        """
        demand_forecast = DemandForecast.bulkcreate(demand_forecast_data)
        return demand_forecast


class VendorController:
    """
    This is the controller class which is used to handle all the logical and CURD operations.
    """

    @classmethod
    def add_vendor(cls, vendor_data: list):
        """
        This function is used to add new vendor.
        :param vendor_data:
        :return int:
        """
        vendor = Vendor.bulkcreate(vendor_data)
        return vendor
