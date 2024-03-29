from typing import Optional, List
from pydantic import condecimal
from datetime import datetime

from sqlmodel import Field, SQLModel, Relationship

class Currency(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    abbr: str
    symbol: str
    
class StatusCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    status_list: List["Status"] = Relationship(back_populates="category")

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

    unit_list: List["Unit"] = Relationship(back_populates="category")

class UnitType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    unit_list: List["Unit"] = Relationship(back_populates="type")

class Status(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category_id: int = Field(foreign_key="statuscategory.id")

    category: StatusCategory = Relationship(back_populates="status_list")
    account_list: List["Account"] = Relationship(back_populates="status")
    vehicle_list: List["Vehicle"] = Relationship(back_populates="status")

class Unit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    abbr: str
    category_id: int = Field(foreign_key="unitcategory.id")
    type_id: int = Field(foreign_key="unittype.id")

    category: UnitCategory = Relationship(back_populates="unit_list")
    type: UnitType = Relationship(back_populates="unit_list")

class UnitConversion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    from_unit_id: int = Field(foreign_key="unit.id")
    to_unit_id: int = Field(foreign_key="unit.id")
    formula: str

    from_unit: Unit = Relationship(sa_relationship_kwargs={"foreign_keys":"UnitConversion.from_unit_id"})
    to_unit: Unit = Relationship(sa_relationship_kwargs={"foreign_keys":"UnitConversion.to_unit_id"})

class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    status_id: Optional[int] = Field(default=None, foreign_key="status.id")
    currency_id: Optional[int] = Field(default=None, foreign_key="currency.id")

    status: Status = Relationship(back_populates="account_list")
    currency: Currency = Relationship()
    vehicle_list: List["Vehicle"] = Relationship(back_populates="account")

class AccountUser(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    account_id: Optional[int] = Field(default=None, foreign_key="account.id", primary_key=True)
    status_id: Optional[int] = Field(default=None, foreign_key="status.id")

    status: Status = Relationship()

class VehicleCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    meter_unit_type_id: int = Field(foreign_key="unittype.id")

    meter_type: UnitType = Relationship()
    make_list: List["VehicleMake"] = Relationship(back_populates="category")

class VehicleMake(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category_id: int = Field(foreign_key="vehiclecategory.id")

    category: VehicleCategory = Relationship(back_populates="make_list")
    model_list: List["VehicleModel"] = Relationship(back_populates="make")

class VehicleModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    make_id: int = Field(foreign_key="vehiclemake.id")

    make: VehicleMake = Relationship(back_populates="model_list")
    vehicle_list: List["Vehicle"] = Relationship(back_populates="model")

class Vehicle(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int
    trim: str
    account_id: int = Field(foreign_key="account.id")
    model_id: int = Field(foreign_key="vehiclemodel.id")
    status_id: int = Field(foreign_key="status.id")
    unit_category_id: int = Field(foreign_key="unitcategory.id")
    default_currency_id: int = Field(foreign_key="currency.id")

    account: Account = Relationship(back_populates="vehicle_list")
    model: VehicleModel = Relationship(back_populates="vehicle_list")
    status: Status = Relationship(back_populates="vehicle_list")
    unit_category: UnitCategory = Relationship()
    currency: Currency = Relationship()

    meter_list: List["Meter"] = Relationship(back_populates="vehicle")

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

    unit: Unit = Relationship()
    vehicle: Vehicle = Relationship(back_populates="meter_list")
    reading_list: List["MeterReading"] = Relationship(back_populates="meter")

class MeterReading(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reading_date: datetime
    reading: int
    meter_id: int = Field(foreign_key="meter.id")

    meter: Meter = Relationship(back_populates="reading_list")

class FuelFill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    qty: condecimal(max_digits=8, decimal_places=3)
    station: Optional[str] = Field(default=None)
    full: bool = Field(default=True)
    local_total_price: condecimal(max_digits=7, decimal_places=3)
    account_total_price: condecimal(max_digits=7, decimal_places=3)
    meter_reading_id: Optional[int] = Field(default=None, foreign_key="meterreading.id")
    qty_unit_id: Optional[int] = Field(default=None, foreign_key="unit.id")
    fuel_grade_id: Optional[int] = Field(default=None, foreign_key="fuelgrade.id")
    local_currency_id: Optional[int] = Field(default=None, foreign_key="currency.id")

    meter_reading: MeterReading = Relationship()
    qty_unit: Unit = Relationship()
    fuel_grade: FuelGrade = Relationship()
    currency: Currency = Relationship()