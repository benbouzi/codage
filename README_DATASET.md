# Analyse du Dataset Anthropic/AnthropicInterviewer

## 📋 À propos du Dataset

Le **AnthropicInterviewer** est un dataset publié par Anthropic contenant **1,250 transcriptions d'entretiens** avec des professionnels sur leur utilisation de l'IA au travail.

### Composition
- **General Workforce**: 1,000 participants
- **Creatives**: 125 participants
- **Scientists**: 125 participants

### Licence
MIT License - Dataset public et gratuit

### Source
https://huggingface.co/datasets/Anthropic/AnthropicInterviewer

---

## 🚧 Problème Actuel: Proxy

L'accès direct à Hugging Face est bloqué par un proxy (erreur 403). Vous avez plusieurs options pour analyser ce dataset :

### Option 1: Téléchargement Manuel (Recommandé)

1. **Visitez directement le dataset**: https://huggingface.co/datasets/Anthropic/AnthropicInterviewer

2. **Naviguez vers "Files and versions"**

3. **Téléchargez les fichiers de données** (généralement dans un dossier `data/`)

4. **Placez-les dans le dossier** `anthropic_interviewer_data/`

5. **Lancez l'analyse**:
   ```bash
   python download_and_analyze.py
   ```

### Option 2: Utiliser un Token Hugging Face

1. **Créez un compte** sur https://huggingface.co

2. **Générez un token**: https://huggingface.co/settings/tokens

3. **Exportez le token**:
   ```bash
   export HF_TOKEN='votre_token_ici'
   ```

4. **Lancez le script**:
   ```bash
   python download_and_analyze.py
   ```

### Option 3: Accès depuis un Autre Environnement

Si vous avez accès à un environnement sans proxy (votre machine locale, un autre serveur, etc.):

1. **Téléchargez le dataset**:
   ```bash
   pip install datasets
   python -c "from datasets import load_dataset; load_dataset('Anthropic/AnthropicInterviewer').save_to_disk('anthropic_interviewer_data')"
   ```

2. **Transférez les fichiers** vers cet environnement

3. **Lancez l'analyse**

---

## 📊 Scripts Disponibles

### 1. `analyze_anthropic_dataset.py`
Script principal d'analyse qui:
- Charge le dataset depuis Hugging Face
- Analyse la structure et les catégories
- Génère des statistiques détaillées
- Export en CSV et JSON
- Crée un rapport complet

**Utilisation**:
```bash
python analyze_anthropic_dataset.py
```

### 2. `download_and_analyze.py`
Script alternatif qui:
- Vérifie les données locales
- Tente l'authentification avec token
- Analyse les fichiers déjà téléchargés
- Fournit des instructions

**Utilisation**:
```bash
python download_and_analyze.py
```

### 3. `direct_download.sh`
Script bash pour téléchargement direct:
- Essaie plusieurs URLs possibles
- Utilise wget et curl
- Télécharge les fichiers individuellement

**Utilisation**:
```bash
chmod +x direct_download.sh
./direct_download.sh
```

### 4. `demo_analysis.py`
Script de démonstration avec données simulées:
- Montre la structure attendue
- Démontre les capacités d'analyse
- Fonctionne sans connexion

**Utilisation**:
```bash
python demo_analysis.py
```

---

## 📦 Résultats Attendus

Une fois le dataset analysé, vous trouverez dans le dossier `output/`:

- **`sample_*.json`**: Échantillons du dataset pour inspection
- **`dataset_*.csv`**: Dataset complet exporté en CSV
- **`full_*.csv`**: Versions complètes par split
- **`analysis_report.md`**: Rapport d'analyse détaillé

---

## 🔍 Structure Attendue du Dataset

D'après la documentation, le dataset contient probablement:

```json
{
  "interview_id": "...",
  "participant_group": "workforce|creatives|scientists",
  "transcript": "...",
  "metadata": {
    "date": "...",
    "duration": "...",
    ...
  }
}
```

---

## 💡 Analyses Possibles

Une fois le dataset chargé, vous pourrez:

1. **Analyse de contenu**
   - Thèmes récurrents dans les entretiens
   - Sentiment analysis
   - Mots-clés les plus fréquents

2. **Comparaison entre groupes**
   - Différences workforce vs creatives vs scientists
   - Usages de l'IA par profession

3. **Statistiques**
   - Longueur moyenne des entretiens
   - Distribution des sujets
   - Fréquence des mentions de technologies

4. **Visualisations**
   - Word clouds par groupe
   - Graphiques de distribution
   - Analyse temporelle

---

## 🆘 Besoin d'Aide?

Si vous rencontrez des problèmes:

1. Vérifiez que les dépendances sont installées:
   ```bash
   pip install -r requirements.txt
   ```

2. Consultez les discussions du dataset:
   https://huggingface.co/datasets/Anthropic/AnthropicInterviewer/discussions

3. Vérifiez les logs d'erreur dans la console

---

## 📚 Sources

- **Dataset**: [Anthropic/AnthropicInterviewer](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer)
- **Documentation**: [All About AI - Anthropic Interviewer](https://www.allaboutai.com/ai-news/what-anthropic-learned-from-1250-people-using-ai-at-work/)
- **Research**: Introducing Anthropic Interviewer - What 1,250 professionals told us about working with AI
