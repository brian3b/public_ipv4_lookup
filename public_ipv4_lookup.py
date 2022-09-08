from requests import get
import json

print ("=" * 100)
ipv4_response = get('https://ip.seeip.org/geoip').text
ipv4_response = json.loads(ipv4_response)
print("Public IPv4 Address: {}".format(ipv4_response["ip"]))
print("Country            :", ipv4_response["country"])
print("Timezone           :", ipv4_response["timezone"])
print("Location           : {}, {}, {}".format(ipv4_response["city"],ipv4_response["region"],ipv4_response["postal_code"]))
print("Coordinates        : {}, {}".format(ipv4_response["latitude"],ipv4_response["longitude"]))
print("ISP                : {}".format(ipv4_response["organization"]))
print("Autonomous System  : {}".format(ipv4_response["asn"]))
print ("=" * 100)