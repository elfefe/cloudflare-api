from .cloudflare.cloudflare import Cloudflare
from .cloudflare.endpoint.dns import Dns
from .cloudflare.endpoint.zones import Zones


def update_dns(auth, dns, name, **modifs):
    dns_name = f"{name}.{dns}" if name else dns

    cloudflare = Cloudflare().authenticate(auth)

    zone = Zones(name=dns)
    zones_response = cloudflare.query(zone)
    try:
        zone_id = zones_response["result"][0]["id"]
    except Exception as e:
        raise Exception(f"{e}\nZone {dns} not found, found:\n{zones_response}")

    dns = Dns(zone_identifier=zone_id)
    dns_response = cloudflare.query(dns)

    for record in dns_response["result"]:
        if dns_name in record["name"]:
            update_record = record

            for key, value in modifs.items():
                update_record[key] = value

            dns.set_update(
                identifier=update_record["id"],
                content=update_record["content"],
                name=update_record["name"],
                record_type=update_record["type"],
            )
            break

    if dns.update is not None:
        return cloudflare.update(dns)
    else:
        raise Exception(f"DNS record {name} not found")
