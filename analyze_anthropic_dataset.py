#!/usr/bin/env python3
"""
Analyse du dataset Anthropic/AnthropicInterviewer
Dataset contenant 1,250 transcriptions d'entretiens sur l'utilisation de l'IA au travail
"""

import os
from datasets import load_dataset
import pandas as pd
import json
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data():
    """Charge le dataset depuis Hugging Face"""
    print("📥 Chargement du dataset Anthropic/AnthropicInterviewer...")
    dataset = load_dataset("Anthropic/AnthropicInterviewer")
    print(f"✅ Dataset chargé avec succès!")
    return dataset

def explore_structure(dataset):
    """Explore la structure du dataset"""
    print("\n" + "="*80)
    print("📊 STRUCTURE DU DATASET")
    print("="*80)

    # Afficher les splits disponibles
    print(f"\n📂 Splits disponibles: {list(dataset.keys())}")

    for split_name, split_data in dataset.items():
        print(f"\n🔹 Split: {split_name}")
        print(f"   Nombre d'exemples: {len(split_data)}")
        print(f"   Colonnes: {split_data.column_names}")

        # Afficher le premier exemple
        if len(split_data) > 0:
            print(f"\n   Premier exemple:")
            first_example = split_data[0]
            for key, value in first_example.items():
                if isinstance(value, str) and len(value) > 200:
                    print(f"   - {key}: {value[:200]}...")
                else:
                    print(f"   - {key}: {value}")

def analyze_categories(dataset):
    """Analyse les catégories de participants"""
    print("\n" + "="*80)
    print("👥 ANALYSE DES CATÉGORIES")
    print("="*80)

    # Convertir en DataFrame pour faciliter l'analyse
    for split_name, split_data in dataset.items():
        df = pd.DataFrame(split_data)

        print(f"\n🔹 Split: {split_name}")

        # Si une colonne de catégorie existe
        category_columns = [col for col in df.columns if 'category' in col.lower() or 'type' in col.lower() or 'group' in col.lower()]

        if category_columns:
            for col in category_columns:
                print(f"\n   Distribution de '{col}':")
                print(df[col].value_counts())

        # Statistiques de base
        print(f"\n   Statistiques:")
        print(f"   - Nombre total d'entretiens: {len(df)}")

        # Analyse de la longueur des transcriptions si disponible
        text_columns = [col for col in df.columns if 'text' in col.lower() or 'transcript' in col.lower() or 'content' in col.lower()]

        if text_columns:
            for col in text_columns:
                if df[col].dtype == object:  # Si c'est du texte
                    df[f'{col}_length'] = df[col].apply(lambda x: len(str(x)) if x else 0)
                    print(f"\n   Longueur de '{col}':")
                    print(f"   - Moyenne: {df[f'{col}_length'].mean():.0f} caractères")
                    print(f"   - Médiane: {df[f'{col}_length'].median():.0f} caractères")
                    print(f"   - Min: {df[f'{col}_length'].min():.0f} caractères")
                    print(f"   - Max: {df[f'{col}_length'].max():.0f} caractères")

def save_sample_data(dataset, num_samples=5):
    """Sauvegarde des exemples pour inspection"""
    print("\n" + "="*80)
    print("💾 SAUVEGARDE D'EXEMPLES")
    print("="*80)

    os.makedirs("output", exist_ok=True)

    for split_name, split_data in dataset.items():
        sample_file = f"output/sample_{split_name}.json"
        samples = split_data.select(range(min(num_samples, len(split_data))))

        with open(sample_file, 'w', encoding='utf-8') as f:
            json.dump([dict(sample) for sample in samples], f, indent=2, ensure_ascii=False)

        print(f"✅ {num_samples} exemples sauvegardés dans: {sample_file}")

def export_full_dataset(dataset):
    """Exporte le dataset complet en CSV"""
    print("\n" + "="*80)
    print("📤 EXPORT DU DATASET")
    print("="*80)

    os.makedirs("output", exist_ok=True)

    for split_name, split_data in dataset.items():
        df = pd.DataFrame(split_data)
        csv_file = f"output/dataset_{split_name}.csv"
        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"✅ Dataset exporté: {csv_file}")
        print(f"   Taille: {len(df)} lignes × {len(df.columns)} colonnes")

def generate_summary_report(dataset):
    """Génère un rapport récapitulatif"""
    print("\n" + "="*80)
    print("📋 RAPPORT RÉCAPITULATIF")
    print("="*80)

    report = []
    report.append("# Analyse du Dataset Anthropic/AnthropicInterviewer\n")
    report.append(f"Dataset: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer\n\n")

    total_examples = 0
    for split_name, split_data in dataset.items():
        df = pd.DataFrame(split_data)
        total_examples += len(df)

        report.append(f"## Split: {split_name}\n")
        report.append(f"- Nombre d'exemples: {len(df)}\n")
        report.append(f"- Colonnes: {', '.join(df.columns)}\n\n")

    report.append(f"\n**Total d'exemples: {total_examples}**\n")

    # Sauvegarder le rapport
    os.makedirs("output", exist_ok=True)
    report_file = "output/analysis_report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.writelines(report)

    print(f"✅ Rapport sauvegardé: {report_file}")
    print("\n".join(report))

def main():
    """Fonction principale"""
    print("🚀 Démarrage de l'analyse du dataset Anthropic/AnthropicInterviewer\n")

    try:
        # 1. Charger le dataset
        dataset = load_data()

        # 2. Explorer la structure
        explore_structure(dataset)

        # 3. Analyser les catégories
        analyze_categories(dataset)

        # 4. Sauvegarder des exemples
        save_sample_data(dataset, num_samples=5)

        # 5. Exporter le dataset complet
        export_full_dataset(dataset)

        # 6. Générer un rapport
        generate_summary_report(dataset)

        print("\n" + "="*80)
        print("✅ ANALYSE TERMINÉE!")
        print("="*80)
        print("\nFichiers générés dans le dossier 'output/':")
        print("  - sample_*.json : Exemples du dataset")
        print("  - dataset_*.csv : Dataset complet exporté")
        print("  - analysis_report.md : Rapport d'analyse")

    except Exception as e:
        print(f"\n❌ Erreur lors de l'analyse: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
