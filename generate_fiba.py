import json
import random

regions = [
    {
        "conf": "Europe",
        "teams": [
            {"region": "Spain", "name": "Spain", "abbr": "ESP"},
            {"region": "Serbia", "name": "Serbia", "abbr": "SRB"},
            {"region": "France", "name": "France", "abbr": "FRA"},
            {"region": "Lithuania", "name": "Lithuania", "abbr": "LTU"},
            {"region": "Greece", "name": "Greece", "abbr": "GRE"},
            {"region": "Germany", "name": "Germany", "abbr": "GER"},
            {"region": "Italy", "name": "Italy", "abbr": "ITA"},
            {"region": "Slovenia", "name": "Slovenia", "abbr": "SLO"}
        ]
    },
    {
        "conf": "Americas",
        "teams": [
            {"region": "United States", "name": "USA", "abbr": "USA"},
            {"region": "Canada", "name": "Canada", "abbr": "CAN"},
            {"region": "Argentina", "name": "Argentina", "abbr": "ARG"},
            {"region": "Brazil", "name": "Brazil", "abbr": "BRA"}
        ]
    },
    {
        "conf": "Asia & Oceania",
        "teams": [
            {"region": "Japan", "name": "Japan", "abbr": "JPN"},
            {"region": "Australia", "name": "Australia", "abbr": "AUS"},
            {"region": "China", "name": "China", "abbr": "CHN"},
            {"region": "Philippines", "name": "Philippines", "abbr": "PHI"}
        ]
    },
    {
        "conf": "Africa",
        "teams": [
            {"region": "Nigeria", "name": "Nigeria", "abbr": "NGR"},
            {"region": "Angola", "name": "Angola", "abbr": "ANG"}
        ]
    }
]

name_pools = {
    "Spain": {"first": ["Pau", "Marc", "Ricky", "Juan", "Sergio", "Rudy", "Willy", "Usman"], "last": ["Gasol", "Rubio", "Navarro", "Llull", "Fernandez", "Hernangomez", "Garuba"]},
    "Serbia": {"first": ["Nikola", "Bogdan", "Milos", "Vasilije", "Nemanja", "Stefan", "Aleksej"], "last": ["Jokic", "Bogdanovic", "Teodosic", "Micic", "Bjelica", "Jovic", "Pusek"]},
    "France": {"first": ["Rudy", "Evan", "Nicolas", "Nando", "Frank", "Victor", "Guerschon"], "last": ["Gobert", "Fournier", "Batum", "De Colo", "Ntilikina", "Wembanyama", "Yabusele"]},
    "Lithuania": {"first": ["Jonas", "Domantas", "Mantas", "Linas", "Sarunas", "Rokas"], "last": ["Valanciunas", "Sabonis", "Kalnietis", "Kleiza", "Jasikevicius", "Giedraitis"]},
    "Greece": {"first": ["Giannis", "Thanasis", "Kostas", "Nick", "Vassilis", "Georgios"], "last": ["Antetokounmpo", "Calathes", "Spanoulis", "Printezis", "Papagiannis"]},
    "Germany": {"first": ["Dennis", "Franz", "Moritz", "Daniel", "Maxi", "Isaac"], "last": ["Schroder", "Wagner", "Theis", "Kleber", "Bonga"]},
    "Italy": {"first": ["Danilo", "Nicolo", "Marco", "Luigi", "Simone", "Stefano"], "last": ["Gallinari", "Melli", "Belinelli", "Datome", "Fontecchio", "Tonut"]},
    "Slovenia": {"first": ["Luka", "Goran", "Zoran", "Edo", "Klemen", "Mike"], "last": ["Doncic", "Dragic", "Muriic", "Prepelic", "Tobey"]},
    "United States": {"first": ["LeBron", "Stephen", "Kevin", "Jayson", "Anthony", "Devin", "Joel"], "last": ["James", "Curry", "Durant", "Tatum", "Davis", "Booker", "Embiid"]},
    "Canada": {"first": ["Shai", "Jamal", "RJ", "Dillon", "Kelly", "Lu"], "last": ["Gilgeous-Alexander", "Murray", "Barrett", "Brooks", "Olynyk", "Dort"]},
    "Argentina": {"first": ["Facundo", "Luis", "Manu", "Nicolas", "Gabriel", "Luca"], "last": ["Campazzo", "Scola", "Ginobili", "Laprovittola", "Deck", "Vildoza"]},
    "Brazil": {"first": ["Marcelinho", "Bruno", "Vitor", "Raul", "Yago", "Cristiano"], "last": ["Huertas", "Caboclo", "Benite", "Neto", "Santos", "Felicio"]},
    "Japan": {"first": ["Rui", "Yuta", "Yuki", "Keisei", "Makoto", "Kosuke"], "last": ["Hachimura", "Watanabe", "Kawamura", "Tominaga", "Hiejima", "Takeuchi"]},
    "Australia": {"first": ["Patty", "Ben", "Joe", "Josh", "Matisse", "Aron"], "last": ["Mills", "Simmons", "Ingles", "Giddey", "Thybulle", "Baynes"]},
    "China": {"first": ["Yao", "Yi", "Zhou", "Guo", "Wang", "Zhao"], "last": ["Ming", "Jianlian", "Qi", "Ailun", "Zhiwei", "Rui"]},
    "Philippines": {"first": ["June Mar", "Jayson", "Scottie", "Dwight", "Jordan", "Kai"], "last": ["Fajardo", "Castro", "Thompson", "Ramos", "Clarkson", "Sotto"]},
    "Nigeria": {"first": ["Precious", "Chikezie", "Josh", "Gabe", "Al-Farouq", "Stan"], "last": ["Achiuwa", "Metu", "Okogie", "Vincent", "Aminu", "Okoye"]},
    "Angola": {"first": ["Carlos", "Yanick", "Joaquim", "Valdelcio", "Gerson"], "last": ["Morais", "Moreira", "Gomes", "Joao", "Domingos"]}
}

bbgm_data = {
    "gameAttributes": {"phase": 0, "season": 2026},
    "teams": [],
    "players": []
}

team_id = 0
for conf_idx, conf in enumerate(regions):
    for t in conf["teams"]:
        bbgm_data["teams"].append({
            "tid": team_id,
            "region": t["region"],
            "name": t["name"],
            "abbrev": t["abbr"],
            "pop": random.randint(20, 150),
            "strategy": 0
        })
        
        country_key = t["region"]
        pool = name_pools.get(country_key, {"first": ["Player"], "last": ["Unknown"]})
        
        for p in range(12):
            f_name = random.choice(pool["first"])
            l_name = random.choice(pool["last"])
            if p > 0:
                l_name += f" {p+1}"
                
            bbgm_data["players"].append({
                "firstName": f_name,
                "lastName": l_name,
                "tid": team_id,
                "born": {"year": random.randint(1995, 2004), "loc": t["region"]},
                "ratings": [{
                    "hgt": random.randint(30, 85),
                    "stre": random.randint(30, 80),
                    "spd": random.randint(30, 80),
                    "jmp": random.randint(30, 80),
                    "endu": random.randint(40, 80),
                    "ins": random.randint(30, 80),
                    "dnk": random.randint(20, 85),
                    "ft": random.randint(50, 85),
                    "fg": random.randint(40, 80),
                    "tp": random.randint(30, 80),
                    "blk": random.randint(20, 80),
                    "stl": random.randint(20, 80),
                    "drb": random.randint(30, 80),
                    "pss": random.randint(30, 80),
                    "reb": random.randint(30, 80),
                    "pot": random.randint(60, 95)
                }],
                "contract": {"amount": random.randint(1000, 15000), "exp": 2028}
            })
        team_id += 1

with open("FIBA_World_Teams.json", "w", encoding="utf-8") as f:
    json.dump(bbgm_data, f, ensure_ascii=False, indent=2)

print("Done")
