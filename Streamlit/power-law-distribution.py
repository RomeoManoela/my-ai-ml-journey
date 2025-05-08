import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Power Law Distribution Visualization")

# Sidebar pour les paramètres
st.sidebar.header("Parameters")
alpha = st.sidebar.slider("Alpha (exposant)", 1.0, 5.0, 2.5, 0.1)
size = st.sidebar.slider("Sample size", 1000, 50000, 10000, 1000)
log_scale = st.sidebar.checkbox("Use logarithmic scale", True)

# Générer des données
x = (np.random.pareto(alpha, size) + 1)  # distribution de Pareto

# Créer la figure avec matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(x, bins=100, density=True, alpha=0.75)

# Configurer les axes selon l'échelle choisie
if log_scale:
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.title(f"Power Law Distribution (α={alpha}) - Log Scale")
else:
    plt.title(f"Power Law Distribution (α={alpha})")

ax.set_xlabel("Value")
ax.set_ylabel("Probability")

# Ajouter des statistiques
st.pyplot(fig)

# Afficher des statistiques
st.subheader("Distribution Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Mean", f"{np.mean(x):.2f}")
col2.metric("Median", f"{np.median(x):.2f}")
col3.metric("Max", f"{np.max(x):.2f}")

# Explication théorique
st.subheader("About Power Law Distributions")
st.write("""
A power law distribution is a probability distribution where the probability of an event 
varies as a power of some attribute of that event. Power laws appear in many natural and 
man-made phenomena, including:

- Sizes of cities
- Income distribution
- Frequency of words in languages
- Magnitude of earthquakes
- Social network connections

The parameter α (alpha) controls the shape of the distribution. Lower values of alpha 
create distributions with longer, heavier tails.
""")