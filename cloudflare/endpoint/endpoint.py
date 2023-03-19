import json


class Endpoint:
    _NAME = None

    def __init__(self):
        self._params = {}
        self.update = None

    def get_params(self):
        return self._params

    def get_list_name(self):
        return self._NAME

    def get_update_name(self, identifier):
        return f"{self._NAME}/{identifier}"

    class Update:
        def __init__(self, identifier, **kwargs):
            self.identifier = identifier
            self._body = {}
            for key, value in kwargs.items():
                if value is not None:
                    self._body[key] = value

        def get_body(self):
            return json.dumps(self._body)
