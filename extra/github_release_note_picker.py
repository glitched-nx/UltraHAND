"""
File: github_release_notes_picker.py
Author: glitched-nx
Description:
    Dieses Skript ruft die neuesten Release-Informationen aus einem GitHub-Repository ab.
    Es speichert die Details der letzten fünf Releases in einer Markdown-Datei,
    erweitert die Datei jedoch nur um neue Releases, die noch nicht in der Liste enthalten sind.
    Die neuen Release Notes werden oben in der Datei hinzugefügt, basierend auf den Release-Versionsnummern.

    For the latest updates and contributions, visit the project's GitHub repository.
    (GitHub Repository: https://github.com/ppkantorski/Ultrahand-Overlay)

    Note: Please be aware that this notice cannot be altered or removed. It is a part
    of the project's documentation and must remain intact.
    
Licensed under CC-BY-NC-SA-4.0
Copyright (c) 2024 ppkantorski
"""


import requests

# API-URL für alle Releases
url = "https://api.github.com/repos/ppkantorski/Ultrahand-Overlay/releases"

# Abrufen der Daten
response = requests.get(url)
releases = response.json()

# Speichern der letzten fünf aktuellsten Releases
latest_releases = releases[:5]

# Lesen der vorhandenen Release Notes
try:
    with open("ultrahand_release_notes.md", "r", encoding="utf-8") as md_file:
        existing_content = md_file.read()
except FileNotFoundError:
    existing_content = ""

# Erstellen einer Liste der vorhandenen Release-Versionsnummern
existing_versions = set()
for line in existing_content.splitlines():
    if line.startswith("## "):
        version = line.split(" ")[1]
        existing_versions.add(version)

# Erstellen und Schreiben der neuen Release Notes
new_content = "# Release Notes\n\n"
for release in latest_releases:
    version = release['name']
    if version not in existing_versions:
        new_content += f"## {release['name']}\n"
        new_content += f"**Erstellt am:** {release['created_at']}\n\n"
        new_content += f"{release['body']}\n"
        new_content += "\n" + "-" * 40 + "\n\n"

# Schreiben der kombinierten Inhalte in die Datei
with open("ultrahand_release_notes.md", "w", encoding="utf-8") as md_file:
    md_file.write(new_content + existing_content)

# Ausgabe der gefilterten Releases in der Konsole
for release in latest_releases:
    print(f"Tag: {release['tag_name']}")
    print(f"Name: {release['name']}")
    print(f"Beschreibung: {release['body']}")
    print(f"Erstellt am: {release['created_at']}")
    print("-" * 40)
