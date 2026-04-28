import csv

def zpracuj_csv(soubor_cesta):
    zamestnanci = {}

    try:
        with open(soubor_cesta, encoding="utf-8") as soubor:
            data = csv.DictReader(soubor)
            
            for r in data:
                try:
                    zam_id = r["id_zamestnance"].strip()
                    jmeno = r["jmeno"].strip()
                    hodiny = float(r["odpracovane_hodiny"].replace(",", "."))

                    if not jmeno or hodiny <= 0:
                        continue

                    
                    if zam_id not in zamestnanci:
                        zamestnanci[zam_id] = {
                            "id": zam_id,
                            "jmeno": jmeno,
                            "celkem_hodin": 0.0,
                            "pocet_smen": 0
                        }
                    
                    zamestnanci[zam_id]["celkem_hodin"] += hodiny
                    zamestnanci[zam_id]["pocet_smen"] += 1

                except (TypeError):
                    continue
                    
    except FileNotFoundError:
        print("Soubor nenalezen!")
        return []

    vysledek = list(zamestnanci.values())
    
    vysledek.sort(key=lambda x: (-x["celkem_hodin"], -x["pocet_smen"], x["id"]))
    
    return vysledek