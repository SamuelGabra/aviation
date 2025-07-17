import aviation

days_per_year = 365.0
passengers_per_year = 6_000_000_000.0
seats_per_aircraft = 200.0
flights_per_aircraft_per_day = 3.0

passengers_per_day = aviation.passengers_per_day(
    passengers_per_year=passengers_per_year, days_per_year=days_per_year
)

print(f"The number of passengers per day are: {passengers_per_day}")
