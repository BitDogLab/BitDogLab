import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Pedro', '12345678')

import urequests
r = urequests.get("http://www.google.com")
print(r.content)
r.close()