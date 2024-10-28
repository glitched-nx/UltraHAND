# Paket-Referenz

Die Datei `package.ini` enthält mehrere Abschnitte, von denen jeder eine Reihe von Befehlen definiert, die ausgeführt werden können. Die Abschnitte sind in eckige Klammern [ ] eingeschlossen, und die Befehle sind unter jedem Abschnitt aufgelistet.

Hier ist ein Beispiel für eine `package.ini`-Datei:

```
;creator={CREATOR_NAME}
;version=1.0.0
;about='Dies ist ein Beispielpaket mit einigen grundlegenden Befehlstests.'
;color=white

[Verzeichnisse erstellen]
mkdir /switch/.packages/example1/
mkdir /switch/.packages/example2/

[Dateien kopieren]
copy /switch/.packages/package.ini /switch/.packages/example1/
copy /switch/.packages/package.ini /switch/.packages/example2/

[Dateien umbenennen]
move /switch/.packages/example1/package.ini /switch/.packages/example1/packageX.ini
move /switch/.packages/example2/package.ini /switch/.packages/example2/packageX.ini

[Verzeichnisse verschieben]
move /switch/.packages/example1/ /switch/.packages/example3/
move /switch/.packages/example2/ /switch/.packages/example4/

[Dateien löschen]
delete /switch/.packages/example1/package.ini
delete /switch/.packages/example2/package.ini

[Verzeichnisse löschen]
delete /switch/.packages/example1/
delete /switch/.packages/example2/
delete /switch/.packages/example3/
delete /switch/.packages/example4/

[INI-Datei bearbeiten]
copy /bootloader/hekate_ipl.ini /switch/.packages/
set-ini-val /switch/.packages/hekate_ipl.ini 'Atmosphere' fss0 gonnawritesomethingelse
set-ini-val ​/switch/.packages/hekate_ipl.ini 'Atmosphere' booty true

[Paketinformationen]
```

Du kannst eigene Abschnitte und Befehle hinzufügen, um die von Ultrahand ausgeführten Aktionen anzupassen.

Hinweis: Die in den Befehlen angegebenen Pfade sollten relativ zum Stammverzeichnis der SD-Karte sein und mit einem / enden.

Für komplexere Ultrahand-Paketbeispiele und Implementierungen, schaue bitte bei den [Beispielen](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples) vorbei.

---

The package config.ini file contains multiple sections, each defining a set of commands that can be executed. The sections are enclosed in square brackets [ ], and the commands are listed below each section.

Here's an example of a `package.ini` file:

```
;creator={CREATOR_NAME}
;version=1.0.0
;about='This is an example package with some basic command testing examples.'
;color=white

[make directories]
mkdir /switch/.packages/example1/
mkdir /switch/.packages/example2/

[copy files]
copy /switch/.packages/package.ini /switch/.packages/example1/
copy /switch/.packages/package.ini /switch/.packages/example2/

[rename files]
move /switch/.packages/example1/package.ini /switch/.packages/example1/packageX.ini
move /switch/.packages/example2/package.ini /switch/.packages/example2/packageX.ini

[move directories]
move /switch/.packages/example1/ /switch/.packages/example3/
move /switch/.packages/example2/ /switch/.packages/example4/

[delete files]
delete /switch/.packages/example1/package.ini
delete /switch/.packages/example2/package.ini

[delete directories]
delete /switch/.packages/example1/
delete /switch/.packages/example2/
delete /switch/.packages/example3/
delete /switch/.packages/example4/

[modify ini file]
copy /bootloader/hekate_ipl.ini /switch/.packages/
set-ini-val /switch/.packages/hekate_ipl.ini 'Atmosphere' fss0 gonnawritesomethingelse
set-ini-val ​/switch/.packages/hekate_ipl.ini 'Atmosphere' booty true

[Package Info]
```

You can add your own sections and commands to customize the actions performed by Ultrahand.

Side-note: The paths specified in the commands should be relative to the SD card root directory and should end with /.

For more complex Ultrahand package examples and implementations, please checkout [Examples](https://github.com/ppkantorski/Ultrahand-Overlay/tree/main/examples).
