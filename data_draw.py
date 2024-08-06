import pandas as pd
import matplotlib.pyplot as plt

# Pfad zur CSV-Datei
csv_file_path = 'data.csv'

# Lese die Datei als Text ein und entferne das letzte Semikolon
with open(csv_file_path, 'r') as file:
    lines = file.readlines()

# Entferne das letzte Semikolon am Ende jeder Zeile
cleaned_lines = [line.strip().rstrip(';') for line in lines]

# Speichere die bereinigte Datei temporär
cleaned_csv_path = 'cleaned_data.csv'
with open(cleaned_csv_path, 'w') as file:
    file.write('\n'.join(cleaned_lines))

# CSV-Datei einlesen mit Komma als Trennzeichen
df = pd.read_csv(cleaned_csv_path, header=None, sep=',', names=['timestamp', 'sensor1', 'sensor2', 'sensor3'])

# Konvertiere die Spalten zu den richtigen Datentypen
df['timestamp'] = pd.to_numeric(df['timestamp'], errors='coerce')
df['sensor1'] = pd.to_numeric(df['sensor1'], errors='coerce')
df['sensor2'] = pd.to_numeric(df['sensor2'], errors='coerce')
df['sensor3'] = pd.to_numeric(df['sensor3'], errors='coerce')

# Entferne Zeilen mit NaN-Werten
df = df.dropna()

# Daten anzeigen
print(df.head())

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['sensor1'], label='Sensor 1')
plt.plot(df['timestamp'], df['sensor2'], label='Sensor 2')
plt.plot(df['timestamp'], df['sensor3'], label='Sensor 3')

# Achsenbeschriftungen und Titel hinzufügen
plt.xlabel('Timestamp')
plt.ylabel('Sensor Values')
plt.title('Sensor Data Over Time')
plt.legend()

# Grid hinzufügen
plt.grid(True)

# Bild speichern
plot_image_path = 'sensor_data_plot.png'
plt.savefig(plot_image_path)

# Plot anzeigen
plt.show()
