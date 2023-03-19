from .endpoint import Endpoint


class Dns(Endpoint):
    _NAME = "dns_records"

    def __init__(self, zone_identifier=None):
        super().__init__()

        self.zone_identifier = zone_identifier

        self.update = None

    def get_list_name(self):
        return f"zones/{self.zone_identifier}/{super().get_list_name()}"

    def get_update_name(self, identifier):
        return f"zones/{self.zone_identifier}/{super().get_update_name(identifier)}"

    def set_update(self, identifier, content, name, record_type, ttl=None, proxied=None, comment=None, tags=None):
        self.update = self.Update(identifier=identifier, content=content, name=name, record_type=record_type, ttl=ttl, proxied=proxied,
                                  comment=comment,
                                  tags=tags)

    class Update(Endpoint.Update):
        def __init__(self, identifier, content, name, record_type, ttl=None, proxied=None, comment=None, tags=None):
            super().__init__(identifier=identifier, content=content, name=name, type=record_type, ttl=ttl, proxied=proxied, comment=comment,
                             tags=tags)
