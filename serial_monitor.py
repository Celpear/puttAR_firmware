import serial

# Serielle Schnittstelle konfigurieren
ser = serial.Serial('/dev/cu.usbserial-0001', 115200, timeout=1)

while True:
    # Lese eine Zeile von der seriellen Schnittstelle
    line = ser.readline().decode('utf-8').strip()
    if line:
        # Splitte die Daten am Komma
        parts = line.split(',')
        if len(parts) >= 4:
            timestamp = parts[0]  # Zeitstempel
            sensor1 = parts[1]    # Erster Sensorwert
            sensor2 = parts[2]    # Zweiter Sensorwert
            sensor3 = parts[3].strip(';')  # Dritter Sensorwert (ohne Semikolon)

            # Drucke die Werte aus
            print(f"Timestamp: {timestamp}")
            print(f"Sensor 1: {sensor1}")
            print(f"Sensor 2: {sensor2}")
            print(f"Sensor 3: {sensor3}")
            print("-" * 20)  # Trennlinie
