# Geolocates IP addresses
# 1. checks cache (external server) to see if IP address is geolocated to within desired tolerance
# 2. if not cached, searches known DBs to see if there's an accurate estimate
# 3. if not accurate estimate, actively tries to determine geolocation using
# a) rDNS
# b) ping from RIPE Atlas
# c) ping from looking glass nodes
# 4. caches new results

class GeoLocIP:
	def __init__(self):
		pass