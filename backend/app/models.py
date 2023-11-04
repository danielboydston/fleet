from typing import Optional
from pydantic import condecimal
from datetime import datetime

from sqlmodel import Field, SQLModel

class Currency(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    abbr: str
    symbol: str
    
class StatusCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    password_hash: str

class FuelGrade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    octane: int

class UnitCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    category_id: int = Field(foreign_key="statuscategory.id")

class Unit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    abbr: str
    category_id: int = Field(foreign_key="unitcategory.id")

class UnitConversion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_unit_id: int = Field(foreign_key="unit.id")
    to_unit_id: int = Field(foreign_key="unit.id")
    formula: str

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None

    status_id: Optional[int] = Field(default=None, foreign_key="status.id")
    currency_id: Optional[int] = Field(default=None, foreign_key="currency.id")

class AccountUser(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    account_id: Optional[int] = Field(default=None, foreign_key="account.id", primary_key=True)
    status_id: Optional[int] = Field(default=None, foreign_key="status.id")

class VehicleCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    meter_unit_category_id: int = Field(foreign_key="unitcategory.id")

class VehicleMake(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    category_id: int = Field(foreign_key="vehiclecategory.id")

class VehicleModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    make_id: int = Field(foreign_key="vehiclemake.id")

class Vehicle(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int
    trim: str

    account_id: int = Field(foreign_key="account.id")
    model_id: int = Field(foreign_key="vehiclemodel.id")
    status_id: int = Field(foreign_key="status.id")
    default_fuel_unit_id: int = Field(foreign_key="unit.id")
    default_currency_id: int = Field(foreign_key="currency.id")

class Meter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None)
    install_date: datetime
    install_meter_reading: int
    install_vehicle_reading: int
    removal_date: Optional[datetime] = Field(default=None)
    correction_ratio: condecimal(max_digits=5, decimal_places=3)

    unit_id: int = Field(foreign_key="unit.id")
    vehicle_id: int = Field(foreign_key="vehicle.id")

class MeterReading(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reading_date: datetime
    reading: int

    meter_id: int = Field(foreign_key="meter.id")

class FuelFill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    qty: condecimal(max_digits=8, decimal_places=3)
    station: Optional[str] = Field(default=None)
    full: bool = Field(default=True)
    local_price_per_unit: condecimal(max_digits=7, decimal_places=3)
    account_price_per_unit: condecimal(max_digits=7, decimal_places=3)

    meter_reading_id: Optional[int] = Field(default=None, foreign_key="meterreading.id")
    qty_unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    fuel_grade_id: Optional[int] = Field(default=None, foreign_key="fuelgrade.id")
    local_currency_id: Optional[int] = Field(default=None, foreign_key="currency.id")