from sqlmodel import SQLModel, create_engine, Session
import os
from .models import Currency, UnitCategory, UnitType, Unit, UnitConversion, StatusCategory, Status, VehicleCategory

#sqlite_file_name = "database.db"
#sqlite_url = f"sqlite:///{sqlite_file_name}"
mysql_url = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_DATABASE']}"


engine = create_engine(mysql_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_static_data():
    with Session(engine) as session:

        # Currencies
        usd = Currency(name="US Dollar", abbr="USD", symbol="$")
        php = Currency(name="Philippine Peso", abbr="PHP", symbol="₱")

        session.add(usd)
        session.add(php)

        # Status Categories
        scAccount = StatusCategory(name="account")
        scAccountUser = StatusCategory(name="accountuser")
        scVehicle = StatusCategory(name="vehicle")

        session.add(scAccountUser)
        session.add(scVehicle)

        # Status
        session.add(Status(name="Active", category=scAccount))
        session.add(Status(name="Inactive", category=scAccount))

        session.add(Status(name="Active", category=scAccountUser))
        session.add(Status(name="Inactive", category=scAccountUser))

        session.add(Status(name="Active", category=scVehicle))
        session.add(Status(name="Maintenance", category=scVehicle))
        session.add(Status(name="Inactive", category=scVehicle))

        # Unit Types
        volume = UnitType(name="Volume")
        distance = UnitType(name="Distance")
        time = UnitType(name="Time")

        # Unit Categories
        metric = UnitCategory(name="Metric")
        imperial = UnitCategory(name="Imperial")
        timeCategory = UnitCategory(name="Time")

        # Units
        gallon = Unit(name="Gallon", abbr="gal", category=imperial, type=volume)
        liter = Unit(name="Liter", abbr="l", category=metric, type=volume)
        mile = Unit(name="Mile", abbr="mi", category=imperial, type=distance)
        kilometer = Unit(name="Kilometer", abbr="km", category=metric, type=distance)
        hour =  Unit(name="Hour", abbr="h", category=timeCategory, type=time)

        session.add(gallon)
        session.add(liter)
        session.add(mile)
        session.add(kilometer)
        session.add(hour)

        # Unit Conversions
        session.add(UnitConversion(from_unit=gallon, to_unit=liter, formula="v*3.78541"))
        session.add(UnitConversion(from_unit=liter, to_unit=gallon, formula="v/3.78541"))
        session.add(UnitConversion(from_unit=mile, to_unit=kilometer, formula="v*1.609344"))
        session.add(UnitConversion(from_unit=kilometer, to_unit=mile, formula="v/1.609344"))

        # Vehicle Categories
        session.add(VehicleCategory(name="Aircraft", meter_type=time))
        session.add(VehicleCategory(name="Watercraft", meter_type=time))
        session.add(VehicleCategory(name="Automobile", meter_type=distance))
        session.add(VehicleCategory(name="ATV", meter_type=distance))
        session.add(VehicleCategory(name="Motorcycle", meter_type=distance))
        session.add(VehicleCategory(name="Fixed", meter_type=time))

        session.commit()
