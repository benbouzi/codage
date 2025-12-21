#!/usr/bin/env python3
"""
Script alternatif pour analyser le dataset Anthropic/AnthropicInterviewer
Gère le téléchargement manuel et l'authentification Hugging Face
"""

import os
import sys
import json
from pathlib import Path
import pandas as pd

def check_local_dataset():
    """Vérifie si le dataset existe déjà localement"""
    possible_paths = [
        "anthropic_interviewer_data",
        "AnthropicInterviewer",
        "data",
        "./data"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Dataset trouvé localement dans: {path}")
            return path

    return None

def download_with_token():
    """Télécharge le dataset avec un token HuggingFace"""
    print("\n🔐 Tentative de téléchargement avec authentification...")

    # Vérifier si un token existe
    token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")

    if not token:
        print("❌ Aucun token HuggingFace trouvé.")
        print("\nPour télécharger le dataset automatiquement:")
        print("1. Créez un compte sur https://huggingface.co")
        print("2. Obtenez votre token: https://huggingface.co/settings/tokens")
        print("3. Exportez-le: export HF_TOKEN='votre_token'")
        return None

    try:
        from huggingface_hub import login, snapshot_download
        login(token=token)
        print("✅ Authentification réussie!")

        print("📥 Téléchargement du dataset...")
        local_dir = snapshot_download(
            repo_id="Anthropic/AnthropicInterviewer",
            repo_type="dataset",
            local_dir="anthropic_interviewer_data"
        )
        print(f"✅ Dataset téléchargé dans: {local_dir}")
        return local_dir

    except Exception as e:
        print(f"❌ Erreur lors du téléchargement: {e}")
        return None

def analyze_local_data(data_path):
    """Analyse les données locales"""
    print(f"\n📊 Analyse du dataset dans: {data_path}")
    print("="*80)

    # Chercher les fichiers de données
    data_files = []
    for ext in ['.json', '.jsonl', '.csv', '.parquet']:
        data_files.extend(Path(data_path).rglob(f'*{ext}'))

    if not data_files:
        print("❌ Aucun fichier de données trouvé!")
        print(f"Contenu du répertoire {data_path}:")
        for item in os.listdir(data_path):
            print(f"  - {item}")
        return

    print(f"\n📁 Fichiers trouvés: {len(data_files)}")
    for f in data_files:
        print(f"  - {f}")

    # Analyser chaque fichier
    os.makedirs("output", exist_ok=True)

    for data_file in data_files:
        print(f"\n{'='*80}")
        print(f"📄 Analyse de: {data_file.name}")
        print(f"{'='*80}")

        try:
            # Charger les données selon le format
            if data_file.suffix == '.json':
                with open(data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        df = pd.DataFrame(data)
                    else:
                        df = pd.DataFrame([data])

            elif data_file.suffix == '.jsonl':
                df = pd.read_json(data_file, lines=True)

            elif data_file.suffix == '.csv':
                df = pd.read_csv(data_file)

            elif data_file.suffix == '.parquet':
                df = pd.read_parquet(data_file)

            else:
                continue

            # Afficher les statistiques
            print(f"\n📊 Statistiques:")
            print(f"  - Nombre de lignes: {len(df)}")
            print(f"  - Nombre de colonnes: {len(df.columns)}")
            print(f"\n📋 Colonnes: {', '.join(df.columns)}")

            # Afficher les premières lignes
            print(f"\n👀 Aperçu des données:")
            print(df.head(3).to_string())

            # Types de données
            print(f"\n🔢 Types de données:")
            print(df.dtypes.to_string())

            # Statistiques descriptives pour les colonnes textuelles
            text_cols = df.select_dtypes(include=['object']).columns
            if len(text_cols) > 0:
                print(f"\n📝 Statistiques sur les colonnes textuelles:")
                for col in text_cols:
                    if df[col].dtype == object:
                        lengths = df[col].apply(lambda x: len(str(x)) if x else 0)
                        print(f"\n  {col}:")
                        print(f"    - Longueur moyenne: {lengths.mean():.0f} caractères")
                        print(f"    - Longueur médiane: {lengths.median():.0f} caractères")
                        print(f"    - Min: {lengths.min():.0f}, Max: {lengths.max():.0f}")
                        print(f"    - Valeurs uniques: {df[col].nunique()}")

            # Sauvegarder un échantillon
            sample_file = f"output/sample_{data_file.stem}.json"
            sample = df.head(5).to_dict(orient='records')
            with open(sample_file, 'w', encoding='utf-8') as f:
                json.dump(sample, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Échantillon sauvegardé: {sample_file}")

            # Sauvegarder le dataset complet en CSV
            csv_file = f"output/full_{data_file.stem}.csv"
            df.to_csv(csv_file, index=False, encoding='utf-8')
            print(f"💾 Dataset complet exporté: {csv_file}")

        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de {data_file.name}: {e}")
            import traceback
            traceback.print_exc()

def manual_download_instructions():
    """Affiche les instructions pour le téléchargement manuel"""
    print("\n" + "="*80)
    print("📖 INSTRUCTIONS POUR TÉLÉCHARGEMENT MANUEL")
    print("="*80)
    print("\nEn raison du proxy, vous devez télécharger le dataset manuellement:")
    print("\n1️⃣  Visitez: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer")
    print("2️⃣  Cliquez sur 'Files and versions'")
    print("3️⃣  Téléchargez les fichiers de données (*.json, *.parquet, etc.)")
    print("4️⃣  Placez-les dans un dossier nommé 'anthropic_interviewer_data/'")
    print("5️⃣  Relancez ce script")
    print("\n💡 Astuce: Vous pouvez aussi utiliser wget ou curl si disponibles:")
    print("   wget https://huggingface.co/datasets/Anthropic/AnthropicInterviewer/resolve/main/data.json")
    print("\nOu utilisez un token HuggingFace:")
    print("   export HF_TOKEN='votre_token'")
    print("   python download_and_analyze.py")
    print("="*80)

def main():
    """Fonction principale"""
    print("🚀 Analyse du dataset Anthropic/AnthropicInterviewer")
    print("="*80)

    # 1. Vérifier si le dataset existe localement
    local_path = check_local_dataset()

    if local_path:
        analyze_local_data(local_path)
        print("\n✅ Analyse terminée!")
        print(f"\n📂 Résultats disponibles dans le dossier 'output/'")
        return

    # 2. Essayer de télécharger avec un token
    print("\n❌ Dataset non trouvé localement.")
    downloaded_path = download_with_token()

    if downloaded_path:
        analyze_local_data(downloaded_path)
        print("\n✅ Analyse terminée!")
        return

    # 3. Afficher les instructions de téléchargement manuel
    manual_download_instructions()

if __name__ == "__main__":
    main()
