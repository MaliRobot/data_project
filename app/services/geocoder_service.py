from app.dependencies import get_geocoder


async def get_reverse_geocode(lat: float, lon: float) -> dict:
    """
    :param lat: Latitude
    :type: float
    :param lon: Longitude
    :type: float
    :return: list containing the dictionaries of all locations found under the lat/lon coordinates
    :rtype: list
    """
    geocoder = await get_geocoder()
    locs_by_reverse = geocoder.reverse_geocode(lat, lon)
    return locs_by_reverse


async def get_city_by_name(name: str) -> dict:
    """
    :param name: Name of the city
    :type: str
    :return: list containing the dictionaries of all locations found under the lat/lon coordinates
    :rtype: list
    """
    geocoder = await get_geocoder()
    return geocoder.geocode(name)
