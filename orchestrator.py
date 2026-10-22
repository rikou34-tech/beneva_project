from prompts import CREATOR_PROMPT, CONTRADICTOR_PROMPT, VERIFIER_PROMPT
from database import log_friction

def run_beneva_council(user_query, client_llm_func):
    """
    Orchestre le débat entre les 3 agents et consigne la friction.
    client_llm_func est une fonction simulant ou appelant l'API du modèle.
    """
    # Étape 1 : Le Créateur propose
    creator_response = client_llm_func(CREATOR_PROMPT, user_query)
    
    # Étape 2 : Le Contradicteur critique
    contradictor_input = f"Requête initiale : {user_query}\nProposition du Créateur : {creator_response}"
    contradictor_response = client_llm_func(CONTRADICTOR_PROMPT, contradictor_input)
    
    # Étape 3 : Le Vérificateur arbitre
    verifier_input = f"Proposition : {creator_response}\nCritique : {contradictor_response}"
    verifier_response = client_llm_func(VERIFIER_PROMPT, verifier_input)
    
    # Consignation automatique dans le Journal de Friction
    log_friction(
        symptom=user_query[:100],
        level="Niveau 2 - Systémique",
        cause="Analyse croisée multi-agents",
        constraint_function="Évaluation de la contrainte et de la fidélité factuelle",
        observed_reality=verifier_response[:200],
        alternative="Arbitrage BENEVA appliqué",
        validation_result="Validé par le Conseil"
    )
    
    return {
        "creator": creator_response,
        "contradictor": contradictor_response,
        "verifier": verifier_response
    }
