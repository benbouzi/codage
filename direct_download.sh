#!/bin/bash
# Script pour télécharger directement les fichiers du dataset
# depuis Hugging Face sans passer par git

echo "🔍 Tentative de téléchargement direct depuis Hugging Face..."
echo "================================================================"

# Créer le dossier de destination
mkdir -p anthropic_interviewer_data

# URLs possibles pour les fichiers de données
BASE_URL="https://huggingface.co/datasets/Anthropic/AnthropicInterviewer/resolve/main"

# Liste des fichiers potentiels à télécharger
FILES=(
    "data/train.json"
    "data/test.json"
    "data/validation.json"
    "data.json"
    "train.json"
    "dataset.json"
    "interviews.json"
    "data/interviews.json"
    "data.parquet"
    "train.parquet"
    "data/train.parquet"
)

echo "📥 Tentative de téléchargement des fichiers..."
echo ""

success=0

for file in "${FILES[@]}"; do
    url="${BASE_URL}/${file}"
    output_file="anthropic_interviewer_data/$(basename $file)"

    echo "Essai: $file"
    if wget -q --timeout=10 --tries=2 "$url" -O "$output_file" 2>/dev/null; then
        if [ -s "$output_file" ]; then
            size=$(du -h "$output_file" | cut -f1)
            echo "  ✅ Téléchargé: $file ($size)"
            success=1
        else
            rm "$output_file"
            echo "  ❌ Fichier vide"
        fi
    elif curl -s --max-time 10 --retry 2 "$url" -o "$output_file" 2>/dev/null && [ -s "$output_file" ]; then
        size=$(du -h "$output_file" | cut -f1)
        echo "  ✅ Téléchargé: $file ($size)"
        success=1
    else
        [ -f "$output_file" ] && rm "$output_file"
        echo "  ⏭️  Non trouvé"
    fi
done

echo ""
echo "================================================================"

if [ $success -eq 1 ]; then
    echo "✅ Au moins un fichier téléchargé avec succès!"
    echo ""
    echo "📂 Fichiers dans anthropic_interviewer_data/:"
    ls -lh anthropic_interviewer_data/
    echo ""
    echo "🚀 Vous pouvez maintenant lancer l'analyse:"
    echo "   python download_and_analyze.py"
else
    echo "❌ Aucun fichier n'a pu être téléchargé."
    echo ""
    echo "💡 Causes possibles:"
    echo "   - Proxy bloquant l'accès à Hugging Face"
    echo "   - Structure du dataset différente de celle attendue"
    echo "   - Besoin d'authentification"
    echo ""
    echo "📖 Veuillez télécharger manuellement depuis:"
    echo "   https://huggingface.co/datasets/Anthropic/AnthropicInterviewer"
fi
