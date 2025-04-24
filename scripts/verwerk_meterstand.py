import json
from pathlib import Path

PAD_NIEUWE = Path("data/nieuwe-meterstand.json")
PAD_BESTAAND = Path("data/meterstanden.json")

# Laad nieuwe meterstand
with PAD_NIEUWE.open("r", encoding="utf-8") as f:
    nieuwe_meterstand = json.load(f)

# Laad bestaande meterstanden
if PAD_BESTAAND.exists():
    with PAD_BESTAAND.open("r", encoding="utf-8") as f:
        bestaande_meterstanden = json.load(f)
else:
    bestaande_meterstanden = []

# Voeg toe
bestaande_meterstanden.append(nieuwe_meterstand)

# Schrijf terug
with PAD_BESTAAND.open("w", encoding="utf-8") as f:
    json.dump(bestaande_meterstanden, f, indent=2)

# Klaar!
print(f"Invoer verwerkt: {nieuwe_meterstand['datum']}")
