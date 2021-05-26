import os
import os.path  # importiert ein packet was erlaubt das man auf das betriebsystem zugreifen darf (Pfade)

# überprüfen ob eine Datei im Verzeichnis existiert
data_dir = 'data/'   #überprüft den relativen Pfad
file_list = os.listdir(data_dir) # gibt eine Liste aus was sich in data befindet
for filename in file_list:
    # automatisches Laden des Dateinamens
    if os.path.isfile(filename):
        # was soll er tun wenn das zutrifft?
        #ist es eine CSV-Datei
        if filename.lower().endswith('.csv'):
            # weiter mit der auswertung der Daten
            print("es ist eine CSV Datei")
        else: 
            # was soll getan werden wenn der Dateinamen nicht passt?
    else:
        # was soll getan werden wenn das nicht
    