from main.db import BaseModel, db
from sqlalchemy import BLOB


class MasterData(BaseModel):
    """
    Model for master data.
    """

    __tablename__ = "master_data"

    file_name = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    file_ext = db.Column(db.String(50))
    file_object = db.Column(BLOB)
    # user_id = db.Column(db.ForeignKey("auth_user.id"))
    # user = db.relationship(
    #     "AuthUser", backref=db.backref("master_data", lazy=True)
    # )


class DemandForecast(BaseModel):
    """
    Model for demand forecast data.
    """

    __tablename__ = "demand_forecast"

    master_id = db.Column(db.ForeignKey("master_data.id"))
    master_demand_forecast = db.relationship(
        "MasterData", backref=db.backref("master_demand_forecast", lazy=True)
    )
    weekend = db.Column(db.DateTime, nullable=False)
    month_no = db.Column(db.Integer, nullable=False)
    month_week = db.Column(db.Integer, nullable=False)
    article = db.Column(db.String(50), nullable=False)
    site = db.Column(db.String(50), nullable=False)
    predict = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.ForeignKey("auth_user.id"))
    # user = db.relationship(
    #     "AuthUser", backref=db.backref("demand_forecast", lazy=True)
    # )


class Vendor(BaseModel):
    """
    Model for vendor data.
    """

    __tablename__ = "vendor"

    master_id = db.Column(db.ForeignKey("master_data.id"))
    master_vendor = db.relationship(
        "MasterData", backref=db.backref("master_vendor", lazy=True)
    )
    vendor_id = db.Column(db.String(50), nullable=False)
    lead_time_avg = db.Column(db.Float, nullable=False)
    lead_time_std_dev = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_cost = db.Column(db.Float, nullable=False)
    stockout_cost = db.Column(db.Float, nullable=False)
    # user_id = db.Column(db.ForeignKey("auth_user.id"))
    # user = db.relationship("AuthUser", backref=db.backref("vendor", lazy=True))
