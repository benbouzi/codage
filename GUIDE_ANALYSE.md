# 🎯 Guide d'Analyse du Dataset Anthropic/AnthropicInterviewer

## 📌 Résumé

Vous souhaitez analyser le dataset **Anthropic/AnthropicInterviewer** qui contient 1,250 transcriptions d'entretiens avec des professionnels sur leur utilisation de l'IA au travail.

**Problème actuel**: L'accès direct à Hugging Face est bloqué par un proxy (erreur 403).

---

## ✅ Ce qui a été créé

### Scripts d'Analyse

1. **`analyze_anthropic_dataset.py`** - Script principal
   - Analyse complète du dataset
   - Statistiques détaillées
   - Export en CSV/JSON
   - Génération de rapports

2. **`download_and_analyze.py`** - Script alternatif
   - Vérifie les données locales
   - Support d'authentification avec token
   - Analyse des fichiers déjà téléchargés
   - Instructions de téléchargement

3. **`direct_download.sh`** - Script de téléchargement
   - Essaie de télécharger directement via wget/curl
   - Test de plusieurs URLs possibles

4. **`demo_analysis.py`** - Démonstration
   - ✅ **DÉJÀ EXÉCUTÉ avec succès**
   - Utilise des données simulées
   - Montre le type d'analyse possible
   - Résultats dans `output/`

### Documentation

- **`README_DATASET.md`** - Documentation complète du dataset
- **`requirements.txt`** - Dépendances Python (déjà installées)

### Résultats de la Démonstration

Le dossier `output/` contient:
- `demo_dataset.json` - Dataset de démonstration (25 entretiens)
- `demo_dataset.csv` - Version CSV
- `demo_sample_*.json` - Échantillons par groupe
- `demo_report.md` - Rapport d'analyse

---

## 🚀 Comment Analyser le Vrai Dataset

### Option 1: Téléchargement Manuel (⭐ Recommandé)

**Étapes**:

1. **Téléchargez le dataset** depuis votre navigateur:
   - Visitez: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer
   - Cliquez sur "Files and versions"
   - Téléchargez tous les fichiers de données (*.json, *.parquet, etc.)

2. **Placez les fichiers** dans un nouveau dossier:
   ```bash
   mkdir anthropic_interviewer_data
   # Copiez les fichiers téléchargés dans ce dossier
   ```

3. **Lancez l'analyse**:
   ```bash
   python download_and_analyze.py
   ```

### Option 2: Utiliser un Token Hugging Face

Si vous pouvez accéder à Hugging Face depuis un autre environnement:

1. **Créez un compte** sur https://huggingface.co

2. **Générez un token**: https://huggingface.co/settings/tokens

3. **Utilisez le token**:
   ```bash
   export HF_TOKEN='votre_token_ici'
   python download_and_analyze.py
   ```

### Option 3: Télécharger depuis un Autre Environnement

Sur une machine sans proxy:

```bash
pip install datasets
python -c "from datasets import load_dataset; load_dataset('Anthropic/AnthropicInterviewer').save_to_disk('anthropic_interviewer_data')"
```

Puis transférez le dossier `anthropic_interviewer_data/` vers cet environnement.

---

## 📊 Résultats Attendus

Une fois le vrai dataset analysé, vous obtiendrez:

### Statistiques
- Distribution par groupe (workforce, creatives, scientists)
- Longueur des transcriptions
- Durée des entretiens
- Analyse de contenu et mots-clés

### Exports
- Fichiers CSV pour analyse dans Excel/Pandas
- Fichiers JSON pour traitement programmatique
- Échantillons pour inspection rapide
- Rapport Markdown récapitulatif

### Analyses Possibles
- **Thématiques**: Identifier les sujets récurrents
- **Sentiment**: Analyser les opinions sur l'IA
- **Comparaisons**: Différences entre groupes professionnels
- **Tendances**: Évolution des usages de l'IA
- **Visualisations**: Word clouds, graphiques, etc.

---

## 🔍 Exemples d'Analyses

### Analyse de Base
```python
import pandas as pd
import json

# Charger les données
with open('output/full_dataset.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Statistiques par groupe
print(df.groupby('participant_group').size())

# Mots-clés les plus fréquents
all_text = ' '.join(df['transcript'].values)
# ... analyse de texte
```

### Analyse de Sentiment
```python
from collections import Counter

# Identifier les mots-clés positifs/négatifs
positive_words = ['helpful', 'efficient', 'innovative', 'exciting']
negative_words = ['concern', 'worried', 'replace', 'threat']

# Compter les occurrences
# ...
```

---

## 📁 Structure des Fichiers

```
codage/
├── analyze_anthropic_dataset.py    # Script principal
├── download_and_analyze.py          # Script alternatif
├── direct_download.sh               # Script téléchargement
├── demo_analysis.py                 # Démonstration
├── README_DATASET.md                # Documentation dataset
├── GUIDE_ANALYSE.md                 # Ce guide
├── requirements.txt                 # Dépendances
├── output/                          # Résultats
│   ├── demo_dataset.json
│   ├── demo_dataset.csv
│   ├── demo_report.md
│   └── demo_sample_*.json
└── anthropic_interviewer_data/      # À créer pour les vraies données
```

---

## 💡 Conseils

### Pour Contourner le Proxy

1. **VPN ou Proxy personnel**: Si disponible
2. **Réseau différent**: WiFi personnel, mobile hotspot
3. **Machine locale**: Téléchargez sur votre PC, puis transférez
4. **Miroir**: Certains datasets ont des miroirs alternatifs

### Pour l'Analyse

1. **Commencez petit**: Analysez d'abord un échantillon
2. **Sauvegardez régulièrement**: Les datasets peuvent être gros
3. **Utilisez des chunks**: Pour les très gros fichiers
4. **Documentez**: Notez vos découvertes au fur et à mesure

---

## 🔗 Ressources

- **Dataset**: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer
- **Documentation Hugging Face**: https://huggingface.co/docs/datasets
- **Article de recherche**: [All About AI - What Anthropic Learned](https://www.allaboutai.com/ai-news/what-anthropic-learned-from-1250-people-using-ai-at-work/)
- **Discussions**: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer/discussions

---

## 🆘 Dépannage

### Erreur 403
- **Cause**: Proxy bloquant Hugging Face
- **Solution**: Téléchargement manuel (Option 1)

### Dataset Non Trouvé
- **Cause**: Fichiers pas dans le bon dossier
- **Solution**: Vérifiez que les fichiers sont dans `anthropic_interviewer_data/`

### Erreur de Parsing
- **Cause**: Format de fichier incorrect
- **Solution**: Vérifiez l'extension (.json, .parquet, etc.)

### Mémoire Insuffisante
- **Cause**: Dataset trop gros
- **Solution**: Analysez par chunks ou échantillonnez

---

## ✨ Prochaines Étapes

1. ✅ Scripts créés et testés
2. ✅ Démonstration exécutée
3. 📥 **À faire**: Télécharger le vrai dataset
4. 🔍 **À faire**: Lancer l'analyse sur les vraies données
5. 📊 **À faire**: Explorer et visualiser les résultats

---

**Bonne analyse ! 🚀**
