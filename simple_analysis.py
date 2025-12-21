#!/usr/bin/env python3
from datasets import load_dataset
import pandas as pd

# Charge le dataset
dataset = load_dataset("Anthropic/AnthropicInterviewer")

# Affiche un exemple complet
print("📄 EXEMPLE D'INTERVIEW (workforce) :\n")
print(dataset['workforce'][0]['text'][:2000])  # Premiers 2000 caractères
print("\n... (suite)\n")

# Affiche plusieurs IDs
print("="*60)
print("\n🔢 LISTE DES 10 PREMIERS IDs (workforce) :")
for i in range(10):
    print(f"  - {dataset['workforce'][i]['transcript_id']}")

# Convertit en DataFrame pour mieux visualiser
print("\n" + "="*60)
print("\n📊 APERÇU SOUS FORME DE TABLEAU :")
df_workforce = dataset['workforce'].to_pandas()
print(df_workforce.head())

# Statistiques
print("\n" + "="*60)
print("\n📈 STATISTIQUES :")
print(f"Nombre total d'interviews : {len(dataset['workforce']) + len(dataset['creatives']) + len(dataset['scientists'])}")
print(f"  - workforce: {len(dataset['workforce'])}")
print(f"  - creatives: {len(dataset['creatives'])}")
print(f"  - scientists: {len(dataset['scientists'])}")
