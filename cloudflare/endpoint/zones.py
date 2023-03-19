from .endpoint import Endpoint


class Zones(Endpoint):
    _NAME = "zones"

    def __init__(self, account_id=None, account_name=None, match=None, name=None, order=None, page=None, per_page=None,
                 status=None):
        super().__init__()

        self.account_id = account_id
        self.account_name = account_name
        self.match = match
        self.name = name
        self.order = order
        self.page = page
        self.per_page = per_page
        self.status = status

        if account_id is not None:
            self._params["account.id"] = account_id
        if account_name is not None:
            self._params["account.name"] = account_name
        if match is not None:
            self._params["match"] = match
        if name is not None:
            self._params["name"] = name
        if order is not None:
            self._params["order"] = order
        if page is not None:
            self._params["page"] = page
        if per_page is not None:
            self._params["per_page"] = per_page
        if status is not None:
            self._params["status"] = status
