from network import Network
from router import Router

def main() -> None:
    # Create network
    network = Network()

    # Add routers
    router1 = network.add_router(1)
    router2 = network.add_router(2)

    # Create links
    network.create_link(router1, router2, 1)

    print("Network created with routers and links")

if __name__ == "__main__":
    main()
