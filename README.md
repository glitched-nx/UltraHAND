# Ultrahand
[![platform](https://img.shields.io/badge/platform-Switch-898c8c?logo=C++.svg)](https://gbatemp.net/forums/nintendo-switch.283/?prefix_id=44)
[![language](https://img.shields.io/badge/language-C++-ba1632?logo=C++.svg)](https://github.com/topics/cpp)
[![GPLv2 License](https://img.shields.io/badge/license-GPLv2-189c11.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Latest Version](https://img.shields.io/github/v/release/ppkantorski/Ultrahand-Overlay?label=latest%20version&color=blue)](https://github.com/ppkantorski/Ultrahand-Overlay/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/ppkantorski/Ultrahand-Overlay/total?color=6f42c1)](https://github.com/ppkantorski/Ultrahand-Overlay/graphs/traffic)
[![GitHub issues](https://img.shields.io/github/issues/ppkantorski/Ultrahand-Overlay?color=222222)](https://github.com/ppkantorski/Ultrahand-Overlay/issues)
[![GitHub stars](https://img.shields.io/github/stars/ppkantorski/Ultrahand-Overlay)](https://github.com/ppkantorski/Ultrahand-Overlay/stargazers)

Erstelle Verzeichnisse, verwalte Dateien und passe Konfigurationen mühelos mit einfachen INI-Dateien an.

[![Ultrahand Logo](.pics/banner.gif)](https://gbatemp.net/threads/ultrahand-overlay-the-fully-craft-able-overlay-executor.633560/)

Ultrahand Overlay ist ein Ersatz für das [Tesla Menu](https://github.com/WerWolv/Tesla-Menu), das von Grund auf mit [libtesla](https://github.com/WerWolv/libtesla) entwickelt wurde. Es bietet leistungsstarke C/C++-Befehle durch die Nutzung einer eigenen [benutzerdefinierten interpretativen Programmiersprache](https://github.com/ppkantorski/Ultrahand-Overlay/wiki/Command-Reference) (ähnlich wie Shell/BASH). Es ist ein vielseitiges Werkzeug, das es Dir ermöglicht, benutzerdefinierte befehlsbasierte Pakete zu erstellen und zu teilen, um erweiterte Funktionen zur Verwaltung von Einstellungen, Dateien und Verzeichnissen auf Deiner Nintendo Switch bereitzustellen.

Mit Ultrahand hast Du die Flexibilität, Dein Dateiverwaltungssystem nach Deinen Bedürfnissen anzupassen und zu gestalten, was Dir mehr Kontrolle über Deine Systemkonfigurationen gibt.

## Screenshots
![Slideshow](.pics/slideshow.gif)

## Funktionen

Ultrahand Overlay bietet derzeit folgende Funktionen:

- **Verzeichnisse erstellen**: 
  - Erstelle mühelos Verzeichnisse auf Deiner SD-Karte, indem Du den Verzeichnispfad angibst. Ultrahand übernimmt den Erstellungsprozess für Dich.

- **Dateien oder Verzeichnisse kopieren**: 
  - Kopiere einfach Dateien oder Verzeichnisse von einem Ort zu einem anderen auf Deiner SD-Karte. Gib einfach die Quell- und Zielpfade an, und Ultrahand übernimmt den Kopiervorgang nahtlos.

- **Dateien oder Verzeichnisse löschen**: 
  - Vereinfache das Löschen von Dateien und Verzeichnissen auf Deiner SD-Karte. Indem Du den Pfad der Datei oder des Verzeichnisses angibst, das Du löschen möchtest, entfernt Ultrahand es umgehend und macht den Löschvorgang problemlos.

- **Dateien oder Verzeichnisse verschieben**: 
  - Verschiebe Dateien oder Verzeichnisse nahtlos zwischen verschiedenen Orten auf Deiner SD-Karte. Gib den Quellpfad und den Zielverzeichnispfad an, und Ultrahand kümmert sich um den Verschiebeprozess, um eine reibungslose Umsiedlung zu gewährleisten.

- **Dateien herunterladen**: 
  - Lade Dateien mühelos auf Deine SD-Karte herunter. Hole effizient Dateien aus Repositories oder URLs an Deinen gewünschten Ort. Egal, ob Du Homebrew herunterladen/aktualisieren oder Dateien zwischen Orten übertragen musst, diese Funktion vereinfacht den Prozess und macht das Repository-Management zum Kinderspiel.

- **Dateien entpacken**: 
  - Extrahiere komprimierte ZIP-Dateien auf Deiner SD-Karte, indem Du archivierte Dateien entpackst und ihre ursprüngliche Struktur beibehältst. Egal, ob Du ZIP-Archive heruntergeladen oder komprimierte Dateien erhalten hast, dieser Befehl vereinfacht den Prozess des Entpackens und macht es mühelos, auf die Inhalte zuzugreifen.

- **INI-Dateien bearbeiten**: 
  - Bearbeite INI-Dateien auf Deiner SD-Karte mit Leichtigkeit. Übernimm die volle Kontrolle über Deine Konfigurationen, indem Du vorhandene Schlüssel-Wert-Paare aktualisierst, neue Einträge hinzufügst oder neue Abschnitte innerhalb der INI-Datei mit Ultrahand erstellst.

- **Hex-Dateien bearbeiten**: 
  - Führe eine hexadezimale Bearbeitung von Dateien auf Deiner SD-Karte durch. Bearbeite die Binärdaten direkt, um eine präzise Kontrolle über Deine Daten zu ermöglichen. Die Hex-Dateien-Bearbeitungsfunktion von Ultrahand ermöglicht es Dir, Dateien in ihrer Rohform zu analysieren, zu ändern und anzupassen.

- **Mods konvertieren**: 
  - Konvertiere `pchtxt`-Mods in das `ips`- oder `cheats`-Format.

- **Systembefehle**: 
  - Es gibt eine Vielzahl von Systembefehlen, die Benutzer nutzen können. Dazu gehören Funktionen zum Herunterfahren, Neustarten, direktes Neustarten in Hekate-Einträge/-Modi, Manipulieren der Bildschirmhintergrundbeleuchtung und Ausschalten aller Bluetooth-Controller.

- **Befehle beim Start ausführen**: 
  - Benutzer können auch ihre eigene `/switch/.packages/boot_package.ini`-Datei (mit einem Befehlsabschnitt `boot`) verwenden, um eine Reihe von Befehlen einmal beim Start des Geräts auszuführen.

## Erste Schritte

### Verwendung

Um Ultrahand zu verwenden, folge diesen Schritten:

1. Lade den neuesten [nxovloader](https://github.com/ppkantorski/nx-ovlloader) herunter und installiere ihn.
2. Lade das neueste Ultrahand [ovlmenu.ovl](https://github.com/ppkantorski/Ultrahand-Overlay/releases/latest/download/ovlmenu.ovl) herunter und platziere es in `/switch/.overlays/`.
    - WARNUNG: Dies überschreibt das `Tesla Menu`, falls es bereits installiert ist.
3. Nach der Installation von Ultrahand Overlay wird ein neuer Ordner namens `ultrahand` im Root-Konfigurationsordner auf Deiner SD-Karte erstellt (`/config/ultrahand/`) zusammen mit einer `config.ini`-Datei, die verschiedene Ultrahand-Einstellungen enthält.
4. Starte Ultrahand (ähnlich wie das `Tesla Menu`) mit Teslas Standard-Hotkeys oder Ultrahands (`ZL+ZR+DDOWN`). Ein neuer Ordner wird erstellt (`/switch/.packages/`) mit einer voreingestellten `package.ini`-Datei für Deine Basis-Menübefehle.

5. Platziere Deine benutzerdefinierte `package.ini`-Paketdatei in Deinem Ultrahand-Paketverzeichnis (`/switch/.packages/<PACKAGE_NAME>/`). Diese Datei enthält die Befehle für Dein benutzerdefiniertes Ultrahand-Paket. Wenn Dein Ultrahand-Paket nicht angezeigt wird, musst Du möglicherweise `Fix Bit Archive` in Hekate ausführen.
    - Siehe [Ultrahand Packages](https://github.com/ppkantorski/Ultrahand-Packages) für eine umfassende Liste bekannter Pakete.

6. Deine Befehle werden nun im Paketmenü innerhalb von Ultrahand angezeigt.

## Zusätzliche Funktionen
- Du kannst `A` drücken, um einen Befehl auszuführen, sowie `MINUS`, um die einzelnen Befehlszeilen im INI zur Ausführung anzuzeigen/auszuführen.
- Du kannst `PLUS` im Hauptmenü drücken, um das Einstellungsmenü zu öffnen.
- Du kannst `X` über einem Overlay/Paket drücken, um sie zu markieren.
- Du kannst `Y` über einem Overlay/Paket drücken, um zusätzliche Einstellungen zu konfigurieren.

Für zusätzliche Unterstützung bei benutzerdefinierten Paketen, schau Dir das [Ultrahand Overlay Wiki](https://github.com/ppkantorski/Ultrahand-Overlay/wiki) an.

### Nintendo Switch Kompatibilität
Um Ultrahand Overlay auf der Nintendo Switch auszuführen, musst Du die notwendige [Homebrew-Umgebung](https://github.com/Atmosphere-NX/Atmosphere) auf Deiner Konsole mit HOS 16.0.0+ eingerichtet haben. Sobald Du die Homebrew-Umgebung eingerichtet hast, kannst Du die kompilierte .ovl auf Deine Switch übertragen und mit Deinen alten `Tesla Menu`-Hotkeys starten.

Bitte beachte, dass die Ausführung von Homebrew-Software auf Deiner Nintendo Switch Deine Garantie ungültig machen kann und gewisse Risiken mit sich bringen kann. Stelle sicher, dass Du die Implikationen verstehst und die entsprechenden Richtlinien und Vorsichtsmaßnahmen beim Verwenden von Homebrew-Software befolgst.

### Kompilierungsvoraussetzungen

Um die Software zu kompilieren und auszuführen, musst Du die folgenden C/C++-Abhängigkeiten installiert haben:

- [libultrahand](https://github.com/ppkantorski/libultrahand)
- libnx
- switch-curl
- switch-zziplib
- switch-mbedtls
- switch-jansson

## Mitwirken

Beiträge sind willkommen! Wenn Du Ideen, Vorschläge oder Fehlerberichte hast, erstelle bitte ein [Issue](https://github.com/ppkantorski/Ultrahand-Overlay/issues/new/choose), reiche einen [Pull Request](https://github.com/ppkantorski/Ultrahand-Overlay/compare) ein oder kontaktiere mich direkt auf [GBATemp](https://gbatemp.net/threads/ultrahand-overlay-the-fully-craft-able-overlay-executor.633560/).

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X8X3VR194)

## Lizenz

Dieses Projekt ist unter [GPLv2](LICENSE) lizenziert und verteilt, mit einer [benutzerdefinierten Bibliothek](https://github.com/ppkantorski/libultrahand/tree/main/libultra), die [CC-BY-4.0](SUB_LICENSE) nutzt.

Copyright (c) 2024 ppkantorski
