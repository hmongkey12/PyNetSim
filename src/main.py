from network import Network
from factories.router_factory import RouterFactory
from managers.link_manager import LinkManager


def main() -> None:
    router_factory = RouterFactory()
    link_manager = LinkManager()
    network = Network(router_factory, link_manager)

    router1 = network.add_router(1)
    router2 = network.add_router(2)
    network.create_link(router1, router2, 1)

    print("Network created with routers and links")


if __name__ == "__main__":
    main()
