# List of matchers that are always illegal to use. These always supercede CONDITIONALLY_ILLEGAL_MATCHES.
ILLEGAL_MATCHES = [
    "DEBUG",
    "Admeme",
    "SalvageShuttleMarker",
    "FTLPoint"
]
# List of matchers that are illegal to use, unless the map is a ship and the ship belongs to the keyed shipyard.
CONDITIONALLY_ILLEGAL_MATCHES = {
    "Shipyard": [
        "Python",  # Decal.
    ],
}
