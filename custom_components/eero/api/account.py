"""Eero API"""
from __future__ import annotations

from .network import EeroNetwork
from .resource import EeroResource
from .const import STATE_ACTIVE

class EeroAccount(EeroResource):

    def __init__(self, api, data) -> None:
        super().__init__(api=api, network=None, data=data)

    @property
    def email(self) -> str | None:
        return self.data.get("email", {}).get("value")

    @property
    def log_id(self) -> str | None:
        return self.data.get("log_id")

    @property
    def name(self) -> str | None:
        return self.data.get("name")

    @property
    def phone(self) -> str | None:
        return self.data.get("phone", {}).get("value")

    @property
    def premium_status(self) -> str | None:
        return STATE_ACTIVE

    @property
    def networks(self) -> list[EeroNetwork | None]:
        networks = []
        for network in self.data.get("networks", {}).get("data", []):
            networks.append(EeroNetwork(self.api, self, network))
        return networks
