drum_names = ["BASS01", "BASS02", "SNARE01", "SNARE02", "TOM01", "HICLOSE", "HIOPEN", "CRASH", "PER01", "PER02", "BASS03", "TOM02"] #order is important. org1.3 consulted.
binary_data = b''

for drum_name in drum_names:
    with open(drum_name+".wav", "rb") as f:
        read_data = f.read()
        binary_data += read_data

with open("DrumWaves_beta.bin", "wb") as f:
    f.write(binary_data)
