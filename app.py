# app.py

import streamlit as st
import matplotlib.pyplot as plt
from load_balancer import LoadBalancer
from utils import generate_request_load

st.set_page_config(page_title="Dynamic Load Balancer", layout="wide")
st.title("Dynamic Load Balancer Simulation")

# Input sliders
cycles = st.slider("Number of cycles", 10, 100, 20)
delay = st.slider("Delay per cycle (for graph only, no real delay)", 0, 2, 0)

if st.button("Start Simulation"):
    lb = LoadBalancer()
    load_history = {f"Server-{i}": [] for i in range(len(lb.servers))}

    for cycle in range(cycles):
        lb.assign_request(generate_request_load())
        lb.release_random_loads()

        for i, server in enumerate(lb.servers):
            load_history[f"Server-{i}"].append(server.current_load)

    # Plotting
    fig, ax = plt.subplots()
    for server_name, loads in load_history.items():
        ax.plot(loads, label=server_name)

    ax.set_xlabel("Cycle")
    ax.set_ylabel("Server Load")
    ax.set_title("Dynamic Load Balancing Over Time")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
