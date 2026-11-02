
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Laboratorio Industrial MAT3230", page_icon="🏭")

st.title("🏭 Laboratorio Industrial: ¡Detectives del cambio!")
st.write("**MAT3230 · Semana 3 · Ingeniería Industrial**")

st.info(
    "🎯 Tu misión: mueve el deslizador y observa cómo cambia "
    "la producción acumulada y la pendiente de la recta tangente."
)

# Modelo didáctico de producción acumulada
def produccion(t):
    return 12 * t**2 - t**3

def derivada(t):
    return 24 * t - 3 * t**2

hora = st.slider(
    "⏰ Selecciona una hora de la jornada",
    min_value=0.0,
    max_value=8.0,
    value=4.0,
    step=0.1
)

tiempos = np.linspace(0, 8, 300)
valores = produccion(tiempos)

punto = produccion(hora)
pendiente = derivada(hora)
tangente = punto + pendiente * (tiempos - hora)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(tiempos, valores, label="Producción acumulada", linewidth=3)
ax.plot(tiempos, tangente, "--", label="Recta tangente")
ax.scatter([hora], [punto], color="red", s=90, zorder=5)

ax.set_xlim(0, 8)
ax.set_ylim(-20, 310)
ax.set_xlabel("Tiempo (horas)")
ax.set_ylabel("Producción acumulada (unidades)")
ax.set_title("Producción y razón de cambio instantánea")
ax.grid(alpha=0.3)
ax.legend()

st.pyplot(fig)
plt.close(fig)

col1, col2 = st.columns(2)

with col1:
    st.metric("📦 Producción acumulada", f"{punto:.1f} unidades")

with col2:
    st.metric("📈 Derivada instantánea", f"{pendiente:.1f} unid./hora")

if pendiente > 0.01:
    st.success("La producción acumulada está aumentando.")
elif pendiente < -0.01:
    st.warning("La producción acumulada está disminuyendo.")
else:
    st.info("La razón de cambio instantánea es cercana a cero.")

st.divider()

st.subheader("💭 Reflexiona como ingeniero o ingeniera industrial")

st.write(
    "¿Qué observas sobre la rapidez con que aumenta la producción "
    "durante la jornada? ¿En qué momento la producción crece más "
    "rápidamente? ¿Cómo podría ayudar esta información a tomar decisiones?"
)

st.caption(
    "Modelo matemático didáctico. No representa datos reales de una empresa."
)
