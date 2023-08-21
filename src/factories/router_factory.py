from router import Router


class RouterFactory:
    def create_router(self, router_id: int) -> Router:
        return Router(router_id)
