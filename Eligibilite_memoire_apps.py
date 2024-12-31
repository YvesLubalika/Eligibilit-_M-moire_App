import streamlit as st


# Eligibilité à la soutenance
st.title("Évaluation de l'Éligibilité pour la Défense de Recherche de Fin d'Études")

# Entrée des informations de l'étudiant

st.header("Informations de l'Étudiant")

nom = st.text_input("Nom de l'étudiant")
post_nom = st.text_input("post_nom de l'étudiant")
first_nom = st.text_input("first_nom de l'étudiant")
if post_nom == "":
    st.write("retype the post name")
elif first_nom  == "" :
    st.write("retype the first name")
else:
    credits_obtenus = st.number_input("Crédits obtenus", min_value=0, max_value=180, step=1)
    moyenne_generale = st.number_input("Moyenne générale", min_value=0.0, max_value=20.0, step=0.1)

    rapport_soumis = st.checkbox("Rapport de recherche soumis")
    
   # Critères d'éligibilité
    credits_requis = 120
    moyenne_minimale = 10.0
    
    # Évaluation de l'éligibilité
    if st.button("Évaluer l'Éligibilité"):
     if credits_obtenus >= credits_requis and moyenne_generale >= moyenne_minimale and rapport_soumis:
      st.success(f"{nom} est éligible pour la défense de la recherche de fin d'études.")
     else:
      st.error(f"{nom} n'est pas éligible pour la défense de la recherche de fin d'études.")
    if credits_obtenus < credits_requis:
     st.warning(f"Crédits obtenus insuffisants : {credits_obtenus}/{credits_requis} requis.")
    if moyenne_generale < moyenne_minimale:
     st.warning(f"Moyenne générale insuffisante : {moyenne_generale}/{moyenne_minimale} requis.")
    if not rapport_soumis:
     st.warning("Rapport de recherche non soumis.")