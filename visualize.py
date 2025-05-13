# visualize.py

from load_balancer import LoadBalancer
from utils import generate_request_load
import matplotlib.pyplot as plt
import time

def visualize_load(cycles=20, delay=1):
    lb = LoadBalancer()
    load_history = {f"Server-{i}": [] for i in range(len(lb.servers))}

    for cycle in range(cycles):
        print(f"Cycle {cycle + 1}")
        lb.assign_request(generate_request_load())
        lb.release_random_loads()

        for i, server in enumerate(lb.servers):
            load_history[f"Server-{i}"].append(server.current_load)

        time.sleep(delay)

    # Plotting
    for server_name, loads in load_history.items():
        plt.plot(loads, label=server_name)

    plt.xlabel("Cycle")
    plt.ylabel("Server Load")
    plt.title("Dynamic Load Balancing Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    visualize_load()
