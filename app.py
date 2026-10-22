import streamlit as st
from database import init_db, get_friction_history
from orchestrator import run_beneva_council

# Initialisation de la base de données
init_db()

st.set_page_config(page_title="BENEVA - Exosquelette Cognitif", layout="wide")

st.title("🛡️ BENEVA : Conseil d'IA & Analyse de Friction")
st.markdown("### Amplification cognitive, détection des biais constructeur et vérité factuelle.")

# Zone de saisie du dilemme
user_query = st.text_area("Soumettez un dilemme ou un problème complexe au Conseil :", 
                          "Ex: Évaluer un choix technologique soumis à des restrictions d'API et à des biais de lissage institutionnel.")

if st.button("Lancer la délibération BENEVA"):
    if not user_query:
        st.warning("Veuillez saisir une requête.")
    else:
        with st.spinner("Le Conseil délibère et analyse la friction..."):
            
            # Fonction simulée ou réelle d'appel LLM pour la démo
            def mock_llm(system_prompt, prompt):
                return f"[Réponse structurée selon le rôle]\n- Analyse basée sur : {prompt[:50]}..."

            results = run_beneva_council(user_query, mock_llm)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🤖 Modèle Standard (Seul)")
                st.info("Réponse classique lissée et soumise aux biais de présentation du constructeur.")
                st.write("Réponse standard type : *« Il est important de nuancer... »* (Perte d'information utile détectée).")
                
            with col2:
                st.subheader("🛡️ Conseil BENEVA (Multi-Agents)")
                st.success("Résultat de l'arbitrage factuel et de la friction croisée.")
                st.markdown(f"**Créateur :**\n{results['creator']}")
                st.markdown(f"**Contradicteur :**\n{results['contradictor']}")
                st.markdown(f"**Vérificateur (Arbitre) :**\n{results['verifier']}")

# Affichage du Journal de Friction (Mémoire SQLite)
st.markdown("---")
st.subheader("📊 Journal de Friction & Mémoire Externe (SQLite)")
history = get_friction_history()
if history:
    for row in history:
        with st.expander(f"Friction du {row[1]} — Symptôme : {row[2]}"):
            st.write(f"**Niveau :** {row[3]}")
            st.write(f"**Cause identifiée :** {row[4]}")
            st.write(f"**Réalité observée :** {row[6]}")
            st.write(f"**Alternative validée :** {row[7]}")
else:
    st.text("Aucune friction enregistrée pour le moment.")
