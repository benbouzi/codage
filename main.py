import os
from dotenv import load_dotenv

def get_groq_api_key():
    # Charge les variables d'environnement depuis un fichier .env
    load_dotenv()
    
    # Récupère la clé GROQ_API_KEY
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        raise ValueError("GROQ_API_KEY n'est pas défini dans le fichier .env")
    
    return api_key

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        key = get_groq_api_key()
        print(f"Clé API chargée : {key}")
    except Exception as e:
        print(f"Erreur : {e}")
