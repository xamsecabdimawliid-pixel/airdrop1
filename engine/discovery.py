from sources.websites import discover_airdrops as rss_discover
from sources.galxe import discover_airdrops as galxe_discover
from sources.zealy import discover_airdrops as zealy_discover
from sources.layer3 import discover_airdrops as layer3_discover

def discover_all():
    sources = [
        rss_discover,
        galxe_discover,
        zealy_discover,
        layer3_discover
    ]

    results = []

    for source in sources:
        try:
            results.extend(source())
        except Exception as error:
            print("Source error:", error)

    return results
