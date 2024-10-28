# Befehlsreferenz:

Stelle sicher, dass Du die korrekte Syntax befolgst und die erforderlichen Argumente für jeden Befehl bereitstellst.

Du kannst diese Befehle in der `package.ini`-Datei konfigurieren, indem Du sie unter den entsprechenden Optionen angibst. Achte darauf, die notwendigen Argumente wie beschrieben für jeden Befehl bereitzustellen.

Ultrahand unterstützt derzeit die folgenden Befehle:

## Systembefehle

- `reboot`: Startet das System neu. Kann auch verwendet werden, um in Hekate / UMS oder Hekate ini Boot-Einträge nach Eintragsnamen neu zu starten.
  - Verwendung: `reboot` oder `reboot hekate` oder `reboot ums` oder
    - `reboot boot <NAME_DES_BOOT_EINTRAGS>` (für Einträge innerhalb von `hekate_ipl.ini`)
    - `reboot ini <NAME_DES_INI_EINTRAGS>` oder `reboot ini <NAME_DES_INI_EINTRAGS> <DUPLIKAT_INDEX>`

- `shutdown`: Fährt das System oder alle Bluetooth-Controller herunter.
  - Verwendung: `shutdown` oder `shutdown controllers`

- `backlight`: Ändert den aktuellen Wert der Hintergrundbeleuchtung.
  - Verwendung: `backlight on` oder `backlight off` oder `backlight <PROZENTZAHL_INTEGER>`

## Dateisystembefehle

- `make` oder `mkdir`: Erstellt ein Verzeichnis.
  - Verwendung: `mkdir <verzeichnis_pfad>`

- `copy` oder `cp`: Kopiert eine Datei oder ein Verzeichnis.
  - Verwendung: `copy <quelle_datei_pfad> <ziel_datei_pfad>`

- `mirror_copy` oder `mirror_cp`: Spiegelt den Inhalt eines Verzeichnisses.
  - Verwendung: `mirror_copy <quelle_datei_pfad> <ziel_datei_pfad>`

- `delete` oder `del`: Löscht eine Datei oder ein Verzeichnis.
  - Verwendung: `delete <datei_pfad>`

- `mirror_delete` oder `mirror_del`: Verwendet den Inhalt eines Quellverzeichnisses, um Dateien im Zielpfad zu entfernen.
  - Verwendung: `mirror_delete <quelle_datei_pfad> <ziel_datei_pfad>`

- `move` oder `mv`: Verschiebt/benennt eine Datei/ein Verzeichnis an einen neuen Ort/Label um.
  - Verwendung: `move <datei_pfad> <ziel_verzeichnis_pfad>`

- `download`: Lädt Dateien von einer angegebenen URL an ein lokales Ziel herunter.
  - Verwendung: `download <datei_url> <ziel_datei_pfad>`

- `unzip`: Extrahiert Dateien aus einem angegebenen ZIP-Archiv an ein lokales Ziel.
  - Verwendung: `unzip <zip_datei_pfad> <ziel_datei_pfad>`

## INI-Befehle

- `set-ini-val` oder `set-ini-value`: Bearbeitet/erstellt eine INI-Datei, indem ein Abschnitt mit einem gewünschten Schlüssel-Wert-Paar aktualisiert/hinzugefügt wird.
  - Verwendung: `set-ini-val <datei_zum_bearbeiten> <gewünschter_abschnitt> <gewünschter_schlüssel> <gewünschter_wert>`

- `set-ini-key`: Bearbeitet eine INI-Datei, indem ein Abschnitt mit einem neuen Schlüssel aktualisiert wird.
  - Verwendung: `set-ini-key <datei_zum_bearbeiten> <gewünschter_abschnitt> <gewünschter_schlüssel> <neuer_schlüssel>`

- `remove-ini-section`: Entfernt einen Abschnitt aus einer INI-Datei.
  - Verwendung: `remove-ini-section <ini_datei_pfad> <abschnittsname>`

## Hex-Bearbeitungsbefehle

- **hex-by-offset**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei an einem angegebenen Offset mit den bereitgestellten Hex-Daten.
  - **Verwendung**: `hex-by-offset <datei_pfad> <offset> <hex_daten>`

- **hex-by-custom-offset**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei an einem angegebenen benutzerdefinierten Muster-Offset mit den bereitgestellten Hex-Daten.
  - **Verwendung**: `hex-by-custom-offset <datei_pfad> <benutzerdefiniertes_muster> <offset> <hex_daten>`

- **hex-by-custom-decimal-offset**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei an einem angegebenen benutzerdefinierten Muster-Offset mit den bereitgestellten Dezimaldaten, die in Hex umgewandelt werden.
  - **Verwendung**: `hex-by-custom-decimal-offset <datei_pfad> <benutzerdefiniertes_muster> <offset> <dezimal_daten>`

- **hex-by-custom-rdecimal-offset**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei an einem angegebenen benutzerdefinierten Muster-Offset mit den bereitgestellten umgekehrten Dezimaldaten, die in umgekehrtes Hex umgewandelt werden.
  - **Verwendung**: `hex-by-custom-rdecimal-offset <datei_pfad> <benutzerdefiniertes_muster> <offset> <rdezimal_daten>`

- **hex-by-swap**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei, indem bestimmte Hex-Daten durch andere ersetzt werden. Du kannst optional ein Vorkommen angeben, das ersetzt werden soll.
  - **Verwendung**: `hex-by-swap <datei_pfad> <hex_daten_zum_ersetzen> <hex_daten_ersatz> [vorkommen]`

- **hex-by-string**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei, indem bestimmte String-Daten durch andere ersetzt werden. String-Daten werden automatisch in Hex umgewandelt.
  - **Verwendung**: `hex-by-string <datei_pfad> <string_daten_zum_ersetzen> <string_daten_ersatz> [vorkommen]`

- **hex-by-decimal**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei, indem bestimmte Dezimaldaten durch andere ersetzt werden. Dezimaldaten werden vor dem Ersetzen in Hex umgewandelt.
  - **Verwendung**: `hex-by-decimal <datei_pfad> <dezimal_daten_zum_ersetzen> <dezimal_daten_ersatz> [vorkommen]`

- **hex-by-rdecimal**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei, indem bestimmte umgekehrte Dezimaldaten durch andere ersetzt werden. Dezimaldaten werden vor dem Ersetzen in umgekehrtes Hex umgewandelt.
  - **Verwendung**: `hex-by-rdecimal <datei_pfad> <dezimal_daten_zum_ersetzen> <dezimal_daten_ersatz> [vorkommen]`

- **hex-by-pattern**
  - **Beschreibung**: Bearbeitet den Inhalt einer Datei, indem Daten ersetzt werden, die einem bestimmten Hex-Muster entsprechen.
  - **Verwendung**: `hex-by-pattern <datei_pfad> <hex_muster_zum_ersetzen> <hex_daten_ersatz>`

---

### Hinweise

- **Vorkommen**: Einige Funktionen erlauben die Angabe eines optionalen `vorkommen`-Parameters, der definiert, welches Vorkommen des Musters oder der Daten ersetzt wird. Wenn nicht angegeben, werden alle Vorkommen ersetzt.
- **Hex-Konvertierungen**: Funktionen wie `hex-by-decimal` und `hex-by-string` konvertieren Dezimal- und String-Daten automatisch in Hex-Format, bevor die Ersetzung in der Datei erfolgt.

## Mod-Konvertierungsbefehle

- `pchtxt2ips`: Konvertiert eine .pchtxt-Mod in eine .ips.
  - Verwendung: `pchtxt2ips <pchtxt_datei_pfad> <ausgabe_datei_pfad>`

- `pchtxt2cheat`: Konvertiert und installiert eine .pchtxt-Mod in einen Cheat.
  - Verwendung: `pchtxt2cheat <pchtxt_datei_pfad>`

## Sourced Placeholder-Funktionen

- `*` (Sternchen):
  - Das Sternchen * wird oft als Platzhalter oder Wildcard verwendet und repräsentiert einen Wert, der während der Ausführung dynamisch gefüllt wird. Es wird häufig in Kontexten verwendet, in denen spezifische Werte erwartet werden, und der tatsächliche Wert wird zur Laufzeit bestimmt.
- `package_source`:
  - Package Source ermöglicht es Benutzern, ein Ultrahand-Paket-ini von einem anderen weiterzuleiten. Dies kann Benutzern helfen, ihren Code zu organisieren und längere Menüs zu verketten.
  - Verwendet mit `;mode=forwarder`, genannt `package_source /pfad/zum/forwarder_package.ini`.
- `list_source`:
  - List Source ist eine Möglichkeit, Variablen für Dropdown-Menüs innerhalb der package.ini zu speichern. Es wird als Platzhalter für die einzelnen Werte innerhalb der List Source-Variable verwendet. Der Code ersetzt List Source-Referenzen durch den entsprechenden Wert.
- `list_file_source`:
  - Ähnlich wie `list_source`, verwendet jedoch ein Textdateiverzeichnis als Eingabe, wobei die Textdatei jeden Eintrag durch Zeilenumbrüche trennt.
- `file_source`:
  - Darstellung einer Quelldatei oder Ressource. Es ist ein Platzhalter für den tatsächlichen Dateinamen oder den Quellort. Der Code ersetzt die Quelle durch den entsprechenden Dateipfad, wenn bestimmte Befehle ausgeführt werden.

    Hier ist eine Aufschlüsselung der zusätzlichen Variablen, die durch die Verwendung von `file_source` zugänglich sind:
    - `file_name`: Der Name der einzelnen Datei.
    - `folder_name`: Der Name des übergeordneten Ordners der Datei.

  - `file_source` in einem `on:`-Abschnitt impliziert, dass ein Befehl oder eine Aktion ausgeführt werden soll, wenn eine bestimmte Quelle "on" oder aktiviert ist.
  - `file_source` in einem `off:`-Abschnitt impliziert, dass ein Befehl oder eine Aktion ausgeführt werden soll, wenn eine bestimmte Quelle "off" oder deaktiviert ist.
  - Bewertet den Zustand eines Schalters oder einer Bedingung und wählt dann den entsprechenden Befehl zur Ausführung basierend darauf aus, ob die Quelle ein- oder ausgeschaltet ist.
  - Für `file_source`-Funktionstoggles, siehe bitte das [Broomstick](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples/Broomstick)-Paketbeispiel.
- `ini_file_source`:
  - Ähnlich wie `list_file_source`, verwendet jedoch Eintragsnamen aus einer ini-Datei für seinen Listenwert. Es behält auch andere ini-Funktionen ähnlich wie `ini_file`.
- `json_file_source`:
  - Dieser Befehl wird verwendet, um eine JSON-Datenquelle zu definieren. Er gibt einen Dateipfad zu einer JSON-Datei an, die Daten enthält. Diese JSON-Datenquelle wird für verschiedene Zwecke innerhalb des Codes verwendet.
  - Der Code liest Daten aus der angegebenen JSON-Datei und führt basierend auf dem Kontext und der Logik im Code möglicherweise Aktionen oder Operationen mit diesen Daten aus.
  - In einigen Fällen kann es auch ein zusätzliches Argument (z.B. jsonKey) akzeptieren, um einen bestimmten Schlüssel oder eine Eigenschaft innerhalb der JSON-Daten anzugeben, die für die Anzeige oder Verarbeitung verwendet werden soll.
  - Dieser Befehl wird verwendet, um strukturierte Daten aus JSON-Dateien abzurufen und in die Funktionalität des Programms zu integrieren.

    Hier ist eine Aufschlüsselung der zusätzlichen Variablen, die durch die Verwendung von `json_file_source` zugänglich sind:
  - `jsonPath`: Der Dateipfad zur JSON-Datenquelle.
  - `jsonKey`: Ein optionaler Schlüssel innerhalb der JSON-Daten für spezifische Datenabrufung.

  - Für Informationen zu `json_file_source`-Funktionsimplementierungen, siehe bitte das [Easy Installer](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples/Easy%20Installer)-Paketbeispiel.

## Platzhalterfunktionen

- `{ram_vendor}`
  - **Beschreibung**: Gibt den Hersteller des RAMs des Geräts zurück.
  - **Beispiel**: Zeigt "Samsung" für ein Gerät mit Samsung RAM an.

- `{ram_model}`
  - **Beschreibung**: Gibt die Modellnummer des RAMs im Gerät zurück.
  - **Beispiel**: Zeigt "M471A1K43BB1-CTD" als Modellnummer an.

- `{ams_version}`
  - **Beschreibung**: Gibt die auf dem Gerät installierte Atmosphere-Version zurück.
  - **Beispiel**: Zeigt "1.7.1" für Atmosphere-Version 1.7.1 an.

- `{hos_version}`
  - **Beschreibung**: Gibt die Horizon OS-Version zurück.
  - **Beispiel**: Zeigt "18.1.0" für Horizon OS-Version 18.1.0 an.

- `{cpu_speedo}`
  - **Beschreibung**: Gibt den CPU-Speedo-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "1600" für den CPU-Speedo-Wert des Geräts an.

- `{cpu_iddq}`
  - **Beschreibung**: Gibt den CPU-IDDQ-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "60" für den CPU-IDDQ-Wert des Geräts an.

- `{gpu_speedo}`
  - **Beschreibung**: Gibt den GPU-Speedo-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "1600" für den GPU-Speedo-Wert des Geräts an.

- `{gpu_iddq}`
  - **Beschreibung**: Gibt den GPU-IDDQ-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "60" für den GPU-IDDQ-Wert des Geräts an.

- `{soc_speedo}`
  - **Beschreibung**: Gibt den SOC-Speedo-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "1600" für den SOC-Speedo-Wert des Geräts an.

- `{soc_iddq}`
  - **Beschreibung**: Gibt den SOC-IDDQ-Wert des Geräts zurück.
  - **Beispiel**: Zeigt "60" für den SOC-IDDQ-Wert des Geräts an.

- `{slice(<STRING>,<START_INDEX>,<END_INDEX>)}`
  - **Beschreibung**: Schneidet einen String basierend auf den angegebenen Start- und Endindizes.
  - **Parameter**:
    - `<STRING>`: Der zu schneidende String.
    - `<START_INDEX>`: Der Startindex des Schnitts.
    - `<END_INDEX>`: Der Endindex des Schnitts.
  - **Beispiel**: `{slice("Test String", 0, 4)}` gibt "Test" zurück.

- `{decimal_to_hex(<DECIMAL>)}`
  - **Beschreibung**: Konvertiert eine Dezimalzahl in einen Hexadezimal-String.
  - **Parameter**:
    - `<DECIMAL>`: Die zu konvertierende Dezimalzahl.
  - **Beispiel**: `{decimal_to_hex(255)}` gibt "FF" zurück.

- `{ascii_to_hex(<ASCII>)}`
  - **Beschreibung**: Konvertiert einen ASCII-String in seine hexadezimale Darstellung.
  - **Parameter**:
    - `<ASCII>`: Der zu konvertierende ASCII-String.
  - **Beispiel**: `{ascii_to_hex("Test")}` gibt "54657374" zurück.

- `{hex_to_rhex(<HEX>)}`
  - **Beschreibung**: Konvertiert einen hexadezimalen String in umgekehrtes Endian-Hex.
  - **Parameter**:
    - `<HEX>`: Der zu konvertierende hexadezimale String.
  - **Beispiel**: `{hex_to_rhex("12345678")}` gibt "78563412" zurück.

- `{hex_to_decimal(<HEX>)}`
  - **Beschreibung**: Konvertiert einen hexadezimalen String in seine dezimale Darstellung.
  - **Parameter**:
    - `<HEX>`: Der zu konvertierende hexadezimale String.
  - **Beispiel**: `{hex_to_decimal("FF")}` gibt "255" zurück.

- `{split(<STRING>,<PATTERN>,<INDEX>)}`
  - **Beschreibung**: Teilt einen String basierend auf einem Muster und gibt einen bestimmten Teil zurück.
  - **Parameter**:
    - `<STRING>`: Der zu teilende String.
    - `<PATTERN>`: Das Muster, das zum Teilen des Strings verwendet wird.
    - `<INDEX>`: Der Index des zurückzugebenden geteilten Teils.
  - **Beispiel**: `{split("Test - String", " - ", 0)}` gibt "Test" zurück.

- `{value}`
  - **Beschreibung**: Gibt den aktuellen Wert eines Schiebereglers oder Trackbars zurück.
  - **Beispiel**: Wird in Schiebereglern verwendet, um den aktuell ausgewählten Wert anzuzeigen.

- `{index}`
  - **Beschreibung**: Gibt den aktuellen Index einer Auswahl oder Liste zurück.
  - **Beispiel**: Wird verwendet, um die Position eines Elements in einer Liste oder Dropdown anzuzeigen.

---

- `{list_source(<INDEX>)}`
  - **Beschreibung**: Ruft ein Element aus einer zuvor mit `list_source` definierten Liste ab.
  - **Parameter**:
    - `<INDEX>`: Index des Elements in der Liste.
  - **Beispiel**: `{list_source(0)}` ruft das erste Element in der Liste ab.

- `{json_source(<KEY>)}`
  - **Beschreibung**: Ruft einen Wert aus einer JSON-Quelle basierend auf dem angegebenen Schlüssel ab.
  - **Parameter**:
    - `<KEY>`: Der Schlüssel, der im JSON-Objekt nachgeschlagen werden soll.
  - **Beispiel**: `{json_source("title")}` ruft den Wert ab, der mit dem Schlüssel "

"title" im JSON-Objekt verknüpft ist.

- `{ini_file(<SECTION>, <KEY>)}`
  - **Beschreibung**: Gibt den Wert eines Schlüssels in einem bestimmten Abschnitt einer INI-Datei zurück.
  - **Parameter**:
    - `<SECTION>`: Der Abschnitt in der INI-Datei.
    - `<KEY>`: Der Schlüssel innerhalb des Abschnitts.
  - **Beispiel**: `{ini_file("Settings", "Language")}` gibt den Wert für den Schlüssel "Language" im Abschnitt "Settings" zurück.

## Befehlsmodi

- `;mode=default`
  - **Beschreibung**: Der Standardbefehlsmodus, der den Befehl so ausführt, wie er ist, ohne spezielle Interaktion oder Verhalten. Wird verwendet, wenn kein anderer Modus explizit erforderlich ist.
  - **Verwendung**: Wenn ein Befehl in seiner Standardform ausgeführt wird.
  - **Beispiel**:

      ```ini
      [Reboot]
      ;mode=default
      reboot
      ```

- `;mode=toggle`
  - **Beschreibung**: Ein Umschaltbefehl, der zwischen zwei Zuständen (ein/aus) wechselt. Der Befehl wird basierend auf seinem aktuellen Zustand ausgeführt und nach der Ausführung in den anderen Zustand umgeschaltet.
  - **Verwendung**: Nützlich für Einstellungen oder Funktionen, die aktiviert/deaktiviert werden können.
  - **Parameter**:
    - `toggle?on`: Setzt das Umschalten standardmäßig auf `ein`.
    - `toggle?off`: Setzt das Umschalten standardmäßig auf `aus`.
  - **Beispiel**:

      ```ini
      [Backlight]
      ;mode=toggle?on
      on:
      backlight on
      off:
      backlight off
      ```

- `;mode=option`
  - **Beschreibung**: Zeigt eine Liste von Optionen an, aus denen der Benutzer wählen kann. Dieser Modus ermöglicht es dem Benutzer, eine von mehreren vordefinierten Optionen auszuwählen.
  - **Verwendung**: Nützlich für Befehle, die mehrere Optionen zur Auswahl benötigen, wie z.B. Konfigurationen oder Einstellungen.
  - **Beispiel**:

      ```ini
      [Graphics Settings]
      ;mode=option
      list_source '(Low, Medium, High)'
      ```

- `;mode=trackbar`
  - **Beschreibung**: Erstellt einen Standard-Trackbar (Schieberegler), der es dem Benutzer ermöglicht, einen Wert zwischen einem minimalen und maximalen Bereich anzupassen.
  - **Verwendung**: Für numerische Einstellungen wie Lautstärke, Helligkeit oder Leistungsanpassungen.
  - **Parameter**:
    - `min_value`: Der minimale ganzzahlige Wert des Trackbars.
    - `max_value`: Der maximale ganzzahlige Wert des Trackbars.
    - `units`: Anzeigeeinheiten für den Wert.
    - `unlocked`: Ermöglicht optional das sofortige Interagieren mit dem Trackbar.
    - `on_every_tick`: Führt optional den Befehl bei jedem Trackbar-Tick aus (standardmäßig deaktiviert).
  - **Beispiel**:

      ```ini
      [Volume]
      ;mode=trackbar
      min_value=0
      max_value=100
      units=%
      ```

- `;mode=step_trackbar`
  - **Beschreibung**: Ähnlich wie der reguläre `trackbar`, jedoch mit festen Schritten zwischen den Werten. Anstatt den Wert frei anzupassen, bewegt sich der Benutzer durch vordefinierte Intervalle.
  - **Verwendung**: Nützlich, wenn Du einen Schieberegler mit bestimmten Schritten möchtest.
  - **Parameter**:
    - `steps`: Definiert die Anzahl der Schritte, die der Trackbar haben wird.
  - **Beispiel**:

      ```ini
      [Brightness]
      ;mode=step_trackbar
      min_value=0
      max_value=5
      steps=6
      ```

- `;mode=named_step_trackbar`
  - **Beschreibung**: Ein Step-Trackbar, der vordefinierte Namen für jeden Schritt verwendet. Der Benutzer wählt einen Schritt aus einer Liste benannter Optionen aus.
  - **Verwendung**: Wird verwendet, wenn spezifische Labels oder benannte Schritte erforderlich sind, wie z.B. Qualitätseinstellungen (Low, Medium, High).
  - **Parameter**:
    - `list_source`: Die Quellliste der Namen für jeden Schritt.
  - **Beispiel**:

      ```ini
      [Performance Mode]
      ;mode=named_step_trackbar
      list_source '(Low, Medium, High, Ultra)'
      ```

- `;mode=slot`
  - **Beschreibung**: Slot-Modus ermöglicht es dem Benutzer, Befehle aus einem vordefinierten Satz von Optionen mit benutzerdefinierten Labels und Fußzeilen auszuführen.
  - **Verwendung**: Wird verwendet, wenn Befehle aus einer Gruppe ausgewählt werden müssen, ähnlich wie `option`, jedoch mit mehr Kontrolle über Anzeigeelemente.
  - **Beispiel**:

      ```ini
      [*Save Slot]
      ;mode=slot
      list_source '(test a, test b, test c)'
      set_footer list_source(*)
      ```

- `;mode=forwarder`
  - **Beschreibung**: Ein Weiterleitungsbefehl, der auf die `.ini`-Datei eines anderen Pakets verweist. Der Benutzer wählt den Weiterleiter aus und wird zu dem weitergeleiteten Paket geführt oder führt Befehle aus diesem Paket aus.
  - **Verwendung**: Nützlich zum Verknüpfen von Befehlen oder Paketen auf modulare Weise.
  - **Parameter**:
    - `package_source`: Verweist auf die weitergeleitete Paket-`.ini`-Datei.
  - **Beispiel**:

      ```ini
      [Performance Options]
      ;mode=forwarder
      package_source '/switch/.packages/performance_config.ini'
      ```

- `;mode=table`
  - **Beschreibung**: Ein Tabellenanzeigemodus, der das Rendern von strukturierten Informationen in einem tabellenähnlichen Format mit Zeilen und Spalten ermöglicht.
  - **Verwendung**: Nützlich zum Anzeigen organisierter Daten wie Systeminformationen, Gerätespezifikationen usw.
  - **Parameter**:
    - `alignment`: Richtet Text innerhalb der Tabellenspalten aus (`left`, `center`, `right`).
    - `header`: Zeichnet einen Header für die Tabelle (true/false).
    - `spacing`: Legt den Abstand zwischen den Zeilen fest.
    - `gap`: Legt den Abstand nach der Tabelle fest.
  - **Beispiel**:

      ```ini
      [System Info]
      ;mode=table
      alignment=left
      header=true
      ```

---

Make sure to follow the correct syntax and provide the required arguments for each command.

You can configure these commands in the `package.ini` file by specifying them under the corresponding options. Make sure to provide the necessary arguments as described for each command.

Ultrahand currently supports the following commands:

## System Commands

- `reboot`: Restarts the system. Can also be used to reboot into Hekate / UMS or Hekate ini boot entries by entry name.
  - Usage: `reboot` or `reboot hekate` or `reboot ums` or
    - `reboot boot <NAME_OF_BOOT_ENTRY>` (for entries within `hekate_ipl.ini`)
    - `reboot ini <NAME_OF_INI_ENTRY>` or `reboot ini <NAME_OF_INI_ENTRY> <DUPLICATE_INDEX>`

- `shutdown`: Shuts down the system or all bluetooth controllers.
  - Usage: `shutdown` or `shutdown controllers`

- `backlight`: Modify the current backlight value.
  - Usage: `backlight on` or `backlight off` or `backlight <PERCENTAGE_INTEGER>`

## Filesystem Commands

- `make` or `mkdir`: Creates a directory.
  - Usage: `mkdir <directory_path>`

- `copy` or `cp`: Copies a file or diectory.
  - Usage: `copy <source_file_path> <destination_file_path>`

- `mirror_copy` or `mirror_cp`: Mirrors the contents of a directory.
  - Usage: `mirror_copy <source_file_path> <destination_file_path>`

- `delete` or `del`: Deletes a file or directory.
  - Usage: `delete <file_path>`

- `mirror_delete` or `mirror_del`: Uses contents of a source directory as for files to remove within the destination path.
  - Usage: `mirror_delete <source_file_path> <destination_file_path>`

- `move` or `mv`: Moves/renames a file/directory to a new location/label.
  - Usage: `move <file_path> <destination_directory_path>`

- `download`: Downloads files from a specified URL to a local destination.
  - Usage: `download <file_url> <destination_file_path>`

- `unzip`: Extracts files from a specified ZIP archive to a local destination.
  - Usage: `unzip <zip_file_path> <destination_file_path>`

## INI Commands

- `set-ini-val` or `set-ini-value`: Edits/makes an INI file by updating/adding a section with a desired key-value pair.
  - Usage: `set-ini-val <file_to_edit> <desired_section> <desired_key> <desired_value>`

- `set-ini-key`: Edits an INI file by updating a section with a new key.
  - Usage: `set-ini-key <file_to_edit> <desired_section> <desired_key> <desired_new_key>`

- `remove-ini-section`: Remove a section from an INI file.
  - Usage: `remove-ini-section <ini_file_path> <section_name>`

## Hex Editing Commands

- **hex-by-offset**
  - **Description**: Edits the contents of a file at a specified offset with the provided hex data.
  - **Usage**: `hex-by-offset <file_path> <offset> <hex_data>`

- **hex-by-custom-offset**
  - **Description**: Edits the contents of a file at a specified custom pattern offset with the provided hex data.
  - **Usage**: `hex-by-custom-offset <file_path> <custom_pattern> <offset> <hex_data>`

- **hex-by-custom-decimal-offset**
  - **Description**: Edits the contents of a file at a specified custom pattern offset with the provided decimal data, which is converted to hex.
  - **Usage**: `hex-by-custom-decimal-offset <file_path> <custom_pattern> <offset> <decimal_data>`

- **hex-by-custom-rdecimal-offset**
  - **Description**: Edits the contents of a file at a specified custom pattern offset with the provided reverse decimal data, which is converted to reversed hex.
  - **Usage**: `hex-by-custom-rdecimal-offset <file_path> <custom_pattern> <offset> <rdecimal_data>`

- **hex-by-swap**
  - **Description**: Edits the contents of a file by replacing a specified hex data with another. You can optionally specify an occurrence to replace.
  - **Usage**: `hex-by-swap <file_path> <hex_data_to_replace> <hex_data_replacement> [occurrence]`

- **hex-by-string**
  - **Description**: Edits the contents of a file by replacing a specified string data with another. String data is automatically converted to hex.
  - **Usage**: `hex-by-string <file_path> <string_data_to_replace> <string_data_replacement> [occurrence]`

- **hex-by-decimal**
  - **Description**: Edits the contents of a file by replacing a specified decimal data with another. Decimal data is converted to hex before replacement.
  - **Usage**: `hex-by-decimal <file_path> <decimal_data_to_replace> <decimal_data_replacement> [occurrence]`

- **hex-by-rdecimal**
  - **Description**: Edits the contents of a file by replacing a specified reverse decimal data with another. Decimal data is converted to reversed hex before replacement.
  - **Usage**: `hex-by-rdecimal <file_path> <decimal_data_to_replace> <decimal_data_replacement> [occurrence]`

- **hex-by-pattern**
  - **Description**: Edits the contents of a file by replacing data that matches a specific hex pattern.
  - **Usage**: `hex-by-pattern <file_path> <hex_pattern_to_replace> <hex_data_replacement>`

---

### Notes

- **Occurrences**: Some functions allow specifying an optional `occurrence` parameter, which defines which instance of the pattern or data will be replaced. If not specified, all occurrences will be replaced.
- **Hex Conversions**: Functions like `hex-by-decimal` and `hex-by-string` automatically convert decimal and string data to hex format before applying the replacement in the file.

## Mod Conversion Commands

- `pchtxt2ips`: Converts a .pchtxt mod into a .ips.
  - Usage: `pchtxt2ips <pchtxt_file_path> <output_file_path>`

- `pchtxt2cheat`: Converts and installs a .pchtxt mod into a cheat.
  - Usage: `pchtxt2cheat <pchtxt_file_path>`

## Sourced Placeholder Functions

- `*` (Asterisk):
  - The asterisk * is often used as a wildcard or placeholder, representing a value that will be dynamically filled in during execution. It's commonly used in contexts where specific values are expected, and the actual value will be determined at runtime.
- `package_source`:
  - Package source allows users to forward one Ultrahand package ini from another.  Can help users organize their code as well as chain up longer menus.
  - Used with `;mode=forwarder`, called `package_source /path/to/forwarder_package.ini`.
- `list_source`:
  - List source is a way to store variables for dropdown menus within the package.ini. It's used as a placeholder for the individual values within the list source variable. The code replaces list_source references with the corresponding value.
- `list_file_source`:
  - Similar to `list_source` but utilizes a text file directory as input with the text file containing each entry separated by newlines.
- `file_source`:
  - Representation of a source file or resource. It's a placeholder for the actual filename or source location. The code replaces source with the appropriate file path when executing certain commands.

    Here's a breakdown of the additional variables accessible by use of `file_source`:
    - `file_name`: The name of the individual file.
    - `folder_name`: The name of the parent folder for the file.

  - `file_source` in an `on:` section implies that a command or action should be executed when a specific source is "on" or enabled.
  - `file_source` in an `off:` section implies that a command or action should be executed when a specific source is "off" or disabled.
  - Evaluates the state of a toggle or a condition and then selects the appropriate command for execution based on whether the source is on or off.
  - For `file_source` function toggles, please refer to the [Broomstick](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples/Broomstick) package example.
- `ini_file_source`:
  - Similar to `list_file_source` but utilizes entry names from an ini file for its list value.  It also retains other ini functions similar to `ini_file`.
- `json_file_source`:
  - This command is used to define a JSON data source. It specifies a file path to a JSON file that contains data. This JSON data source is used for various purposes within the code.
  - The code reads data from the specified JSON file, and based on the context and logic in the code, it may perform actions or operations using this data.
  - In some cases, it might also accept an additional argument (e.g., jsonKey) to indicate a specific key or property within the JSON data to be used for display or processing.
  - This command is used to retrieve structured data from JSON files and incorporate it into the program's functionality.

    Here's a breakdown of the additional variables accessible by use of `json_file_source`:
  - `jsonPath`: The file path to the JSON data source.
  - `jsonKey`: An optional key within the JSON data for specific data retrieval.

  - For information on `json_file_source` function implementations, please refer to the [Easy Installer](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples/Easy%20Installer) package example.

## Placeholder Functions

- `{ram_vendor}`
  - **Description**: Returns the vendor of the device's RAM.
  - **Example**: Displays "Samsung" for a device with Samsung RAM.

- `{ram_model}`
  - **Description**: Returns the model number of the RAM in the device.
  - **Example**: Displays "M471A1K43BB1-CTD" as the model number.

- `{ams_version}`
  - **Description**: Returns the Atmosphere version installed on the device.
  - **Example**: Displays "1.7.1" for Atmosphere version 1.7.1.

- `{hos_version}`
  - **Description**: Returns the Horizon OS version.
  - **Example**: Displays "18.1.0" for Horizon OS version 18.1.0.

- `{cpu_speedo}`
  - **Description**: Returns the CPU speedo value of the device.
  - **Example**: Displays "1600" for the device's CPU speedo value.

- `{cpu_iddq}`
  - **Description**: Returns the CPU IDDQ value of the device.
  - **Example**: Displays "60" for the device's CPU IDDQ value.

- `{gpu_speedo}`
  - **Description**: Returns the GPU speedo value of the device.
  - **Example**: Displays "1600" for the device's GPU speedo value.

- `{gpu_iddq}`
  - **Description**: Returns the GPU IDDQ value of the device.
  - **Example**: Displays "60" for the device's GPU IDDQ value.

- `{soc_speedo}`
  - **Description**: Returns the SOC speedo value of the device.
  - **Example**: Displays "1600" for the device's SOC speedo value.

- `{soc_iddq}`
  - **Description**: Returns the SOC IDDQ value of the device.
  - **Example**: Displays "60" for the device's SOC IDDQ value.

- `{slice(<STRING>,<START_INDEX>,<END_INDEX>)}`
  - **Description**: Slices a string based on the provided start and end indices.
  - **Parameters**:
    - `<STRING>`: The string to be sliced.
    - `<START_INDEX>`: The starting index of the slice.
    - `<END_INDEX>`: The ending index of the slice.
  - **Example**: `{slice("Test String", 0, 4)}` returns "Test".

- `{decimal_to_hex(<DECIMAL>)}`
  - **Description**: Converts a decimal number to a hexadecimal string.
  - **Parameters**:
    - `<DECIMAL>`: The decimal number to convert.
  - **Example**: `{decimal_to_hex(255)}` returns "FF".

- `{ascii_to_hex(<ASCII>)}`
  - **Description**: Converts an ASCII string to its hexadecimal representation.
  - **Parameters**:
    - `<ASCII>`: The ASCII string to convert.
  - **Example**: `{ascii_to_hex("Test")}` returns "54657374".

- `{hex_to_rhex(<HEX>)}`
  - **Description**: Converts a hexadecimal string to reverse-endian hexadecimal.
  - **Parameters**:
    - `<HEX>`: The hexadecimal string to convert.
  - **Example**: `{hex_to_rhex("12345678")}` returns "78563412".

- `{hex_to_decimal(<HEX>)}`
  - **Description**: Converts a hexadecimal string to its decimal representation.
  - **Parameters**:
    - `<HEX>`: The hexadecimal string to convert.
  - **Example**: `{hex_to_decimal("FF")}` returns "255".

- `{split(<STRING>,<PATTERN>,<INDEX>)}`
  - **Description**: Splits a string based on a pattern and returns a specific portion.
  - **Parameters**:
    - `<STRING>`: The string to split.
    - `<PATTERN>`: The pattern used to split the string.
    - `<INDEX>`: The index of the split portion to return.
  - **Example**: `{split("Test - String", " - ", 0)}` returns "Test".

- `{value}`
  - **Description**: Returns the current value of a trackbar or slider.
  - **Example**: Used in trackbars to display the current selected value.

- `{index}`
  - **Description**: Returns the current index of a selection or list.
  - **Example**: Used to indicate the position of an item in a list or dropdown.

---

- `{list_source(<INDEX>)}`
  - **Description**: Fetches an item from a list defined earlier using `list_source`.
  - **Parameters**:
    - `<INDEX>`: Index of the item in the list.
  - **Example**: `{list_source(0)}` fetches the first item in the list.

- `{json_source(<KEY>)}`
  - **Description**: Fetches a value from a JSON source based on the provided key.
  - **Parameters**:
    - `<KEY>`: The key to look up in the JSON object.
  - **Example**: `{json_source("title")}` fetches the value associated with the "title" key in a JSON object.

- `{ini_file(<SECTION>, <KEY>)}`
  - **Description**: Returns the value of a key in a specific section of an INI file.
  - **Parameters**:
    - `<SECTION>`: The section in the INI file.
    - `<KEY>`: The key within the section.
  - **Example**: `{ini_file("Settings", "Language")}` returns the value for the "Language" key under the "Settings" section.

## Command Modes

- `;mode=default`
  - **Description**: The default command mode that executes the command as is, without any special interaction or behavior. Used when no other mode is explicitly required.
  - **Usage**: When a command is executed in its standard form.
  - **Example**:

      ```ini
      [Reboot]
      ;mode=default
      reboot
      ```

- `;mode=toggle`
  - **Description**: A toggle command that switches between two states (on/off). The command will execute based on its current state and flip to the other state after execution.
  - **Usage**: Useful for settings or features that can be enabled/disabled.
  - **Parameters**:
    - `toggle?on`: Set the toggle to default to `on`.
    - `toggle?off`: Set the toggle to default to `off`.
  - **Example**:

      ```ini
      [Backlight]
      ;mode=toggle?on
      on:
      backlight on
      off:
      backlight off
      ```

- `;mode=option`
  - **Description**: Displays a list of options for the user to choose from. This mode allows the user to pick one of several predefined options.
  - **Usage**: Useful for commands that need multiple options to be selected from, such as configurations or settings.
  - **Example**:

      ```ini
      [Graphics Settings]
      ;mode=option
      list_source '(Low, Medium, High)'
      ```

- `;mode=trackbar`
  - **Description**: Creates a standard trackbar (slider) allowing the user to adjust a value between a minimum and maximum range.
  - **Usage**: For numerical settings like volume, brightness, or performance adjustments.
  - **Parameters**:
    - `min_value`: The minimum integer value of the trackbar.
    - `max_value`: The maximum integer value of the trackbar.
    - `units`: Display units for the value.
    - `unlocked`: Optionally allows the trackbar to be unlocked for immediate interaction.
    - `on_every_tick`: Optionally execute the command at every trackbar tick (off by default).
  - **Example**:

      ```ini
      [Volume]
      ;mode=trackbar
      min_value=0
      max_value=100
      units=%
      ```

- `;mode=step_trackbar`
  - **Description**: Similar to the regular `trackbar`, but with fixed steps between values. Instead of freely adjusting the value, the user moves through predefined intervals.
  - **Usage**: Useful when you want a slider with distinct steps.
  - **Parameters**:
    - `steps`: Defines the number of steps the trackbar will have.
  - **Example**:

      ```ini
      [Brightness]
      ;mode=step_trackbar
      min_value=0
      max_value=5
      steps=6
      ```

- `;mode=named_step_trackbar`
  - **Description**: A step trackbar that uses predefined names for each step. The user selects a step from a list of named options.
  - **Usage**: Used when specific labels or named steps are required, such as quality settings (Low, Medium, High).
  - **Parameters**:
    - `list_source`: The source list of names for each step.
  - **Example**:

      ```ini
      [Performance Mode]
      ;mode=named_step_trackbar
      list_source '(Low, Medium, High, Ultra)'
      ```

- `;mode=slot`
  - **Description**: Slot mode allows the user to execute commands from a predefined set of options with custom labels and footers.
  - **Usage**: Used when commands need to be selected from a group, similar to `option`, but with more control over display elements.
  - **Example**:

      ```ini
      [*Save Slot]
      ;mode=slot
      list_source '(test a, test b, test c)'
      set_footer list_source(*)
      ```

- `;mode=forwarder`
  - **Description**: A forwarder command that points to another package's `.ini` file. The user selects the forwarder and is taken to the forwarded package or executes commands from that package.
  - **Usage**: Useful for linking commands or packages in a modular fashion.
  - **Parameters**:
    - `package_source`: Points to the forwarded package `.ini` file.
  - **Example**:

      ```ini
      [Performance Options]
      ;mode=forwarder
      package_source '/switch/.packages/performance_config.ini'
      ```

- `;mode=table`
  - **Description**: A table display mode that allows rendering of structured information in a table-like format with rows and columns.
  - **Usage**: Useful for displaying organized data like system information, device specs, etc.
  - **Parameters**:
    - `alignment`: Aligns text within the table columns (`left`, `center`, `right`).
    - `header`: Draws a header for the table (true/false).
    - `spacing`: Sets the spacing between rows.
    - `gap`: Sets the gap after the table.
  - **Example**:

      ```ini
      [System Info]
      ;mode=table
      alignment=left
      header=true
      ```
