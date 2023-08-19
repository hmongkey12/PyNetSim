from network import Network
from router import Router

# Create network
network = Network()

# Add routers
router1 = network.add_router(1)
router2 = network.add_router(2)

# Create links
network.create_link(router1, router2, 1)

# Simulate (will be extended when protocols are implemented)
# network.simulate(protocol_handler)
