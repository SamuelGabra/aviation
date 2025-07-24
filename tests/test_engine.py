import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 6_000_000_000.0 * passenger / year},
            "passengers_per_year",
            6_000_000_000.0 * passenger / year,
        ),
        (
            {"required_global_fleet": 27_397.26 * aircraft},
            "required_global_fleet",
            27_397.26 * aircraft,
        ),
        (
            {
                "passengers_per_year": 6_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            16_438_356.16 * passenger / day,
        ),
        (
            {
                "passengers_per_day": 16_438_356.16 * passenger / day,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            27_397.26 * aircraft,
        ),
        (
            {
                "passengers_per_year": 6_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            27_397.26 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: typing.Any,  # noqa: ANN401
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected, atol=20_000.0)
