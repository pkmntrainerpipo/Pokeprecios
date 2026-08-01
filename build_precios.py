
import json, re, time, requests
SETS = {"base1": "Base", "base2": "Jungle", "base3": "Fossil", "base4": "Base Set 2", "base5": "Team Rocket", "base6": "Legendary Collection", "basep": "Wizards Black Star Promos", "bp": "Best of Game", "bw1": "Black & White", "bw10": "Plasma Blast", "bw11": "Legendary Treasures", "bw2": "Emerging Powers", "bw3": "Noble Victories", "bw4": "Next Destinies", "bw5": "Dark Explorers", "bw6": "Dragons Exalted", "bw7": "Boundaries Crossed", "bw8": "Plasma Storm", "bw9": "Plasma Freeze", "bwp": "BW Black Star Promos", "cel25": "Celebrations", "cel25c": "Celebrations: Classic Collection", "col1": "Call of Legends", "dc1": "Double Crisis", "det1": "Detective Pikachu", "dp1": "Diamond & Pearl", "dp2": "Mysterious Treasures", "dp3": "Secret Wonders", "dp4": "Great Encounters", "dp5": "Majestic Dawn", "dp6": "Legends Awakened", "dp7": "Stormfront", "dpp": "DP Black Star Promos", "dv1": "Dragon Vault", "ecard1": "Expedition Base Set", "ecard2": "Aquapolis", "ecard3": "Skyridge", "ex1": "Ruby & Sapphire", "ex10": "Unseen Forces", "ex11": "Delta Species", "ex12": "Legend Maker", "ex13": "Holon Phantoms", "ex14": "Crystal Guardians", "ex15": "Dragon Frontiers", "ex16": "Power Keepers", "ex2": "Sandstorm", "ex3": "Dragon", "ex4": "Team Magma vs Team Aqua", "ex5": "Hidden Legends", "ex6": "FireRed & LeafGreen", "ex7": "Team Rocket Returns", "ex8": "Deoxys", "ex9": "Emerald", "fut20": "Pokémon Futsal Collection", "g1": "Generations", "gym1": "Gym Heroes", "gym2": "Gym Challenge", "hgss1": "HeartGold & SoulSilver", "hgss2": "HS—Unleashed", "hgss3": "HS—Undaunted", "hgss4": "HS—Triumphant", "hsp": "HGSS Black Star Promos", "mcd11": "McDonald's Collection 2011", "mcd12": "McDonald's Collection 2012", "mcd14": "McDonald's Collection 2014", "mcd15": "McDonald's Collection 2015", "mcd16": "McDonald's Collection 2016", "mcd17": "McDonald's Collection 2017", "mcd18": "McDonald's Collection 2018", "mcd19": "McDonald's Collection 2019", "mcd21": "McDonald's Collection 2021", "mcd22": "McDonald's Collection 2022", "me1": "Mega Evolution", "me2": "Phantasmal Flames", "me2pt5": "Ascended Heroes", "me3": "Perfect Order", "me4": "Chaos Rising", "me5": "Pitch Black", "neo1": "Neo Genesis", "neo2": "Neo Discovery", "neo3": "Neo Revelation", "neo4": "Neo Destiny", "np": "Nintendo Black Star Promos", "pgo": "Pokémon GO", "pl1": "Platinum", "pl2": "Rising Rivals", "pl3": "Supreme Victors", "pl4": "Arceus", "pop1": "POP Series 1", "pop2": "POP Series 2", "pop3": "POP Series 3", "pop4": "POP Series 4", "pop5": "POP Series 5", "pop6": "POP Series 6", "pop7": "POP Series 7", "pop8": "POP Series 8", "pop9": "POP Series 9", "rsv10pt5": "White Flare", "ru1": "Pokémon Rumble", "si1": "Southern Islands", "sm1": "Sun & Moon", "sm10": "Unbroken Bonds", "sm11": "Unified Minds", "sm115": "Hidden Fates", "sm12": "Cosmic Eclipse", "sm2": "Guardians Rising", "sm3": "Burning Shadows", "sm35": "Shining Legends", "sm4": "Crimson Invasion", "sm5": "Ultra Prism", "sm6": "Forbidden Light", "sm7": "Celestial Storm", "sm75": "Dragon Majesty", "sm8": "Lost Thunder", "sm9": "Team Up", "sma": "Hidden Fates Shiny Vault", "smp": "SM Black Star Promos", "sv1": "Scarlet & Violet", "sv10": "Destined Rivals", "sv2": "Paldea Evolved", "sv3": "Obsidian Flames", "sv3pt5": "151", "sv4": "Paradox Rift", "sv4pt5": "Paldean Fates", "sv5": "Temporal Forces", "sv6": "Twilight Masquerade", "sv6pt5": "Shrouded Fable", "sv7": "Stellar Crown", "sv8": "Surging Sparks", "sv8pt5": "Prismatic Evolutions", "sv9": "Journey Together", "sve": "Scarlet & Violet Energies", "svp": "Scarlet & Violet Black Star Promos", "swsh1": "Sword & Shield", "swsh10": "Astral Radiance", "swsh10tg": "Astral Radiance Trainer Gallery", "swsh11": "Lost Origin", "swsh11tg": "Lost Origin Trainer Gallery", "swsh12": "Silver Tempest", "swsh12pt5": "Crown Zenith", "swsh12pt5gg": "Crown Zenith Galarian Gallery", "swsh12tg": "Silver Tempest Trainer Gallery", "swsh2": "Rebel Clash", "swsh3": "Darkness Ablaze", "swsh35": "Champion's Path", "swsh4": "Vivid Voltage", "swsh45": "Shining Fates", "swsh45sv": "Shining Fates Shiny Vault", "swsh5": "Battle Styles", "swsh6": "Chilling Reign", "swsh7": "Evolving Skies", "swsh8": "Fusion Strike", "swsh9": "Brilliant Stars", "swsh9tg": "Brilliant Stars Trainer Gallery", "swshp": "SWSH Black Star Promos", "tk1a": "EX Trainer Kit Latias", "tk1b": "EX Trainer Kit Latios", "tk2a": "EX Trainer Kit 2 Plusle", "tk2b": "EX Trainer Kit 2 Minun", "xy0": "Kalos Starter Set", "xy1": "XY", "xy10": "Fates Collide", "xy11": "Steam Siege", "xy12": "Evolutions", "xy2": "Flashfire", "xy3": "Furious Fists", "xy4": "Phantom Forces", "xy5": "Primal Clash", "xy6": "Roaring Skies", "xy7": "Ancient Origins", "xy8": "BREAKthrough", "xy9": "BREAKpoint", "xyp": "XY Black Star Promos", "zsv10pt5": "Black Bolt", "mep": "MEP Black Star Promos", "svpx": "Scarlet & Violet Black Star Promos"}
CAT = 3
UA = {"User-Agent": "PipoPokedex/1.0"}
def norm(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
def nnum(s): return re.sub(r'^0+', '', (str(s or '').split('/')[0])).lower() or '0'
def get(url):
    for _ in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=60)
            if r.status_code == 200: return r.json()
        except Exception: pass
        time.sleep(1)
    return {}
groups = get(f"https://tcgcsv.com/tcgplayer/{CAT}/groups").get("results", [])
by_name = {}
for gr in groups:
    by_name.setdefault(norm(gr.get("name")), gr["groupId"])
    parts = (gr.get("name") or "").split(":")
    if len(parts) > 1: by_name.setdefault(norm(parts[-1]), gr["groupId"])
    if gr.get("abbreviation"): by_name.setdefault(norm(gr.get("abbreviation")), gr["groupId"])
matched = {sid: by_name[norm(nm)] for sid, nm in SETS.items() if norm(nm) in by_name}
precios = {}
for setId, gid in matched.items():
    prods = get(f"https://tcgcsv.com/tcgplayer/{CAT}/{gid}/products").get("results", [])
    prices = get(f"https://tcgcsv.com/tcgplayer/{CAT}/{gid}/prices").get("results", [])
    num_by_pid = {}
    for p in prods:
        for ed in p.get("extendedData", []):
            if ed.get("name") == "Number":
                num_by_pid[p["productId"]] = nnum(ed.get("value")); break
    price_by_pid = {}
    for pr in prices:
        pid, mp, st = pr.get("productId"), pr.get("marketPrice"), pr.get("subTypeName") or ""
        if mp is None: continue
        if pid not in price_by_pid or st in ("Normal", "Holofoil"): price_by_pid[pid] = mp
    for pid, number in num_by_pid.items():
        if pid in price_by_pid: precios[f"{setId}-{number}"] = round(price_by_pid[pid], 2)
    time.sleep(0.12)
json.dump(precios, open("precios.json", "w"), ensure_ascii=False)
print("sets casados:", len(matched), "| precios:", len(precios))
