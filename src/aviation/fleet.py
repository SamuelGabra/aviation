"""Modelling of the global fleet based on average passenger and aircraft data."""

import typing

import camia_model as model
from camia_model.units import Quantity, day, year

from aviation.units import aircraft, journey, passenger


@model.transform
def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, passenger / day]:
    """The number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers flying per year globally.
    """
    return passengers_per_year.convert_to(passenger / day)


@model.transform
def required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / aircraft],
    flights_per_aircraft_per_day: typing.Annotated[Quantity, journey / (aircraft * day)],
) -> typing.Annotated[Quantity, aircraft]:
    """The size of the required global fleet.

    Args:
        passengers_per_day: The number of passengers flying per year globally.
        seats_per_aircraft: The number of seats in the modelled aircraft.
        flights_per_aircraft_per_day: The number of flights per aircraft per day

    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (
        seats_per_aircraft * flights_per_aircraft_per_day * aircraft_per_journey
    )
