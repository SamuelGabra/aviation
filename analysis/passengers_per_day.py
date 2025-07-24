"""Analysis to determine the number of passengers per day."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import passenger

days_per_year = 365.0 * day / year
passengers_per_year = 6_000_000_000.0 * passenger / year


inputs = {"passengers_per_year": passengers_per_year}
output = "passengers_per_day"
systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)
print(f"{passengers_per_day=!s}")
