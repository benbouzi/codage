#!/usr/bin/env python3
"""
Script de démonstration de l'analyse du dataset AnthropicInterviewer
Utilise des données simulées pour montrer les capacités d'analyse
"""

import json
import pandas as pd
import os
from collections import Counter
import random

def create_demo_data():
    """Crée des données de démonstration basées sur la structure attendue"""
    print("🎨 Création de données de démonstration...")

    groups = {
        "workforce": 20,
        "creatives": 3,
        "scientists": 2
    }

    # Thèmes et vocabulaire typiques par groupe
    themes = {
        "workforce": [
            "using AI for email automation",
            "AI helps with scheduling and calendar management",
            "incorporating AI into daily workflow",
            "using chatbots for customer service",
            "AI-powered data analysis tools",
            "concerns about job displacement",
            "need for AI training and upskilling"
        ],
        "creatives": [
            "AI as creative assistant for brainstorming",
            "using AI for image generation and editing",
            "AI helps overcome creative blocks",
            "concerns about AI replacing creative jobs",
            "AI for content generation and writing",
            "ethical considerations in AI-generated art",
            "balance between AI assistance and human creativity"
        ],
        "scientists": [
            "AI accelerates research and data analysis",
            "using AI for literature review and paper search",
            "AI models for experimental predictions",
            "concerns about AI bias in research",
            "AI for hypothesis generation",
            "collaboration between human scientists and AI",
            "reproducibility and transparency with AI tools"
        ]
    }

    demo_dataset = []

    for group, count in groups.items():
        for i in range(count):
            # Générer un transcript simulé
            selected_themes = random.sample(themes[group], k=random.randint(3, 5))
            transcript = f"Interviewer: How do you use AI in your work?\n\nParticipant: "
            transcript += " ".join(selected_themes)
            transcript += f"\n\nInterviewer: What are your main concerns?\n\nParticipant: {random.choice(selected_themes)}"

            entry = {
                "interview_id": f"{group}_{i+1:03d}",
                "participant_group": group,
                "transcript": transcript,
                "metadata": {
                    "interview_date": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                    "duration_minutes": random.randint(15, 45),
                    "consent": True
                }
            }
            demo_dataset.append(entry)

    return demo_dataset

def analyze_demo_data(dataset):
    """Analyse les données de démonstration"""
    print("\n" + "="*80)
    print("📊 ANALYSE DES DONNÉES DE DÉMONSTRATION")
    print("="*80)

    df = pd.DataFrame(dataset)

    # Statistiques générales
    print(f"\n📈 Statistiques Générales:")
    print(f"  - Total d'entretiens: {len(df)}")
    print(f"  - Colonnes: {', '.join(df.columns)}")

    # Distribution par groupe
    print(f"\n👥 Distribution par Groupe:")
    group_counts = df['participant_group'].value_counts()
    for group, count in group_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  - {group}: {count} ({percentage:.1f}%)")

    # Analyse des transcripts
    df['transcript_length'] = df['transcript'].apply(len)
    print(f"\n📝 Longueur des Transcripts:")
    print(f"  - Moyenne: {df['transcript_length'].mean():.0f} caractères")
    print(f"  - Médiane: {df['transcript_length'].median():.0f} caractères")
    print(f"  - Min: {df['transcript_length'].min():.0f} caractères")
    print(f"  - Max: {df['transcript_length'].max():.0f} caractères")

    # Analyse des métadonnées
    if 'metadata' in df.columns:
        durations = [entry['metadata']['duration_minutes'] for entry in dataset]
        print(f"\n⏱️  Durée des Entretiens:")
        print(f"  - Moyenne: {sum(durations)/len(durations):.1f} minutes")
        print(f"  - Min: {min(durations)} minutes")
        print(f"  - Max: {max(durations)} minutes")

    # Analyse de contenu simple
    print(f"\n🔍 Analyse de Contenu:")
    keywords = ["AI", "automation", "creative", "research", "concern", "job", "tool", "help"]

    for keyword in keywords:
        count = df['transcript'].str.contains(keyword, case=False).sum()
        percentage = (count / len(df)) * 100
        print(f"  - '{keyword}' mentionné dans {count} entretiens ({percentage:.1f}%)")

    # Analyse par groupe
    print(f"\n📊 Analyse par Groupe:")
    for group in df['participant_group'].unique():
        group_df = df[df['participant_group'] == group]
        print(f"\n  🔹 {group.upper()}:")
        print(f"    - Nombre: {len(group_df)}")
        print(f"    - Longueur moyenne transcript: {group_df['transcript_length'].mean():.0f} caractères")

        # Mots-clés spécifiques au groupe
        group_text = " ".join(group_df['transcript'].values).lower()
        words = group_text.split()
        word_freq = Counter(words)
        common_words = [w for w, c in word_freq.most_common(10) if len(w) > 3]
        print(f"    - Mots fréquents: {', '.join(common_words[:5])}")

    return df

def save_demo_results(dataset, df):
    """Sauvegarde les résultats de démonstration"""
    print("\n" + "="*80)
    print("💾 SAUVEGARDE DES RÉSULTATS")
    print("="*80)

    os.makedirs("output", exist_ok=True)

    # Sauvegarder le dataset complet
    with open("output/demo_dataset.json", 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"✅ Dataset sauvegardé: output/demo_dataset.json")

    # Sauvegarder en CSV
    df_export = df.copy()
    df_export['metadata'] = df_export['metadata'].apply(json.dumps)
    df_export.to_csv("output/demo_dataset.csv", index=False, encoding='utf-8')
    print(f"✅ Dataset sauvegardé: output/demo_dataset.csv")

    # Sauvegarder des échantillons par groupe
    for group in df['participant_group'].unique():
        group_df = df[df['participant_group'] == group]
        samples = group_df.head(3).to_dict(orient='records')
        with open(f"output/demo_sample_{group}.json", 'w', encoding='utf-8') as f:
            json.dump(samples, f, indent=2, ensure_ascii=False)
        print(f"✅ Échantillon sauvegardé: output/demo_sample_{group}.json")

    # Créer un rapport
    report = []
    report.append("# Rapport d'Analyse de Démonstration\n\n")
    report.append("## Dataset Anthropic/AnthropicInterviewer (Démonstration)\n\n")
    report.append(f"**Total d'entretiens**: {len(df)}\n\n")

    report.append("### Distribution par Groupe\n\n")
    for group, count in df['participant_group'].value_counts().items():
        percentage = (count / len(df)) * 100
        report.append(f"- **{group}**: {count} entretiens ({percentage:.1f}%)\n")

    report.append("\n### Statistiques\n\n")
    report.append(f"- Longueur moyenne des transcripts: {df['transcript_length'].mean():.0f} caractères\n")
    report.append(f"- Longueur médiane: {df['transcript_length'].median():.0f} caractères\n")

    with open("output/demo_report.md", 'w', encoding='utf-8') as f:
        f.writelines(report)
    print(f"✅ Rapport sauvegardé: output/demo_report.md")

def show_next_steps():
    """Affiche les prochaines étapes"""
    print("\n" + "="*80)
    print("🎯 PROCHAINES ÉTAPES")
    print("="*80)
    print("\n📌 Cette démonstration montre comment l'analyse fonctionnera avec les vraies données.\n")
    print("Pour analyser le vrai dataset AnthropicInterviewer:")
    print("\n1️⃣  Téléchargez le dataset depuis:")
    print("   https://huggingface.co/datasets/Anthropic/AnthropicInterviewer")
    print("\n2️⃣  Placez les fichiers dans: anthropic_interviewer_data/")
    print("\n3️⃣  Lancez l'analyse:")
    print("   python download_and_analyze.py")
    print("\n📖 Consultez README_DATASET.md pour plus de détails")
    print("\n" + "="*80)

def main():
    """Fonction principale"""
    print("🚀 DÉMONSTRATION D'ANALYSE - Dataset Anthropic/AnthropicInterviewer")
    print("="*80)
    print("\n⚠️  Note: Ce script utilise des données SIMULÉES pour démonstration")
    print("Les vraies données doivent être téléchargées depuis Hugging Face\n")

    # Créer les données de démonstration
    dataset = create_demo_data()
    print(f"✅ {len(dataset)} entretiens de démonstration créés")

    # Analyser les données
    df = analyze_demo_data(dataset)

    # Sauvegarder les résultats
    save_demo_results(dataset, df)

    # Afficher les prochaines étapes
    show_next_steps()

    print("\n✅ Démonstration terminée!")
    print(f"\n📂 Résultats disponibles dans: output/")

if __name__ == "__main__":
    main()
