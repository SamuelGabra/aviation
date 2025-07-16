days_per_year = 365.0
passengers_per_year = 6_000_000_000.0
seats_per_aircraft = 200.0
flights_per_aircraft_per_day = 3.0

passengers_per_day = passengers_per_year / days_per_year
global_fleet_size = passengers_per_day / (seats_per_aircraft * flights_per_aircraft_per_day)

print(f"The global fleet size is: {global_fleet_size}")

