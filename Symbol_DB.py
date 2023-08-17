from pymongo import MongoClient

# create a connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')

# specify the database and the collection (equivalent of a table in SQL)
db = client['tinymce-db']
ghs = db['piktogramms']
hsatz = db['hsatzs']
euhsatz = db['euhsatzs']
psatz = db['psatzs']
phrasen = db['phrasens']

# Piktogramm
ghs_data = [
    {
        "_id": "GHS01", 
        "description": "Explosive Stoffe/\nGemische und Erzeugnisse mit Explosivstoff (instabil oder Unterklassen 1.1 bis 1.4\nSelbstzersetzliche Stoffe und Gemische, Typ A oder Typ B\nOrganische Peroxide, Typ A oder Typ B\n", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs01.gif",
    },
    {
        "_id": "GHS02", 
        "description": "Entzündbare Gase, Kategorie 1 \r\nAerosole, Kategorie 1 und 2\r\nEntzündbare Flüssigkeiten/Feststoffe\r\nSelbstzersetzliche Stoffe und Gemische, Typ B bis Typ F\r\nPyrophore Flüssigkeiten/Feststoffe\r\nSelbsterhitzungsfähige Stoffe/Gemische\r\nStoffe und Gemische, die mit Wasser entzündbare Gase entwickeln\r\nOrganische Peroxide, Typ B bis Typ F", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs02.gif",
    },
    {
        "_id": "GHS03", 
        "description": "Oxidierende Gase\r\nOxidierende Flüssigkeiten\r\nOxidierende Feststoffe\r\n", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs03.gif",
    },
    {
        "_id": "GHS04", 
        "description": "Gase unter Druck: verdichtete/verflüssigte/gelöste Gase, tiefgekühlt verflüssigte Gase", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs04.gif",
    },
    {
        "_id": "GHS05", 
        "description": "Korrosiv gegenüber Metallen\r\nÄtz-/Reizwirkung auf die Haut, Kategorie 1A, 1B, 1C\r\nSchwere Augenschädigung/ Augenreizung, Kategorie 2\r\n", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs05.gif",
    },
    {
        "_id": "GHS06", 
        "description": "Akute Toxizität, Kategorie 1 bis 3", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs06.gif",
    },
    {
        "_id": "GHS07", 
        "description": "Akute Toxizität, Kategorie 4\r\nÄtz-/Reizwirkung auf die Haut, Kategorie 2\r\nSchwere Augenschädigung/\r\nAugenreizung, Kategorie 2\r\nSensibilisierung der Haut\r\nSpezifische Zielorgan-Toxizität (einmalige Exposition), Kategorie 3, H335 oder H336\r\nDie Ozonschicht schädigend\r\n", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs07.gif",
    },
    {
        "_id": "GHS08", 
        "description": "Sensibilisierung der Atemwege \r\nKeimzellmutagenität, Karzinogenität\r\nReproduktionstoxizität\r\nSpezifische Zielorgan-Toxizität (einmalige Exposition), Kategorie 1 oder 2\r\nSpezifische Zielorgan-Toxizität (wiederholte Exposition)  \r\nAspirationsgefahr\r\n\r\n", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs08.gif",
    },
    {
        "_id": "GHS09", 
        "description": "Gewässergefährdend: Akut, Kategorie 1 oder Chronisch, Kategorie 1 oder 2", 
        "symbol": "https://gestis-api.dguv.de/api/exactimage/GHS/ghs09-neu.gif",
    }
]
ghs.insert_many(ghs_data)

#Phrase
phrasen_data = [
    {
        "_id": "Explosiv",
        "ghs_reference_id": "GHS01"
    },
    {
        "_id": "Extrem entzündbar",
        "ghs_reference_id": "GHS02"
    },
    {
        "_id": "Leicht entzündbar",
        "ghs_reference_id": "GHS02"
    },
    {
        "_id": "Entzündbar",
        "ghs_reference_id": "GHS02"
    },
    {
        "_id": "Reagiert heftig mit Wasser",
        "ghs_reference_id": "GHS02"
    },
    {
        "_id": "Selbstentzündlich",
        "ghs_reference_id": "GHS02"
    },
    {
        "_id": "Oxidationsmittel",
        "ghs_reference_id": "GHS03"
    },
    {
        "_id": "Lebensgefahr",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "Giftig",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "Gesundheitsschädlich",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "Betäubend",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "Allergisierend beim Einatmen",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "Allergisierend bei Hautkontakt",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "KMR–Stoff Kat. 1",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "KMR–Stoff Kat. 2",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "Schädigt die Organe",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "Kann die Organe schädigen",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "Aspirationsgefahr lebensgefährlich",
        "ghs_reference_id": "GHS08"
    },
    {
        "_id": "Ätzend/Korrosiv",
        "ghs_reference_id": "GHS05"
    },
    {
        "_id": "Reizend",
        "ghs_reference_id": "GHS07"
    }
]
phrasen.insert_many(phrasen_data)

#H-satz and EUH
hsatz_data = [
    {
        "_id": "H200",
        "description": "Instabil, explosiv.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P201", "P202", "P372", "P373", "P380", "P401", "P501"]
    },
    {
        "_id": "H201",
        "description": "Explosiv, Gefahr der Massenexplosion.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P230", "P240", "P250", "P280", "P372", "P373", "P401", "P501"]
    },
    {
        "_id": "H202",
        "description": "Explosiv; große Gefahr durch Splitter, Spreng- und Wurfstücke.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P230", "P240", "P250", "P280", "P372", "P373", "P401", "P501"]
    },
    {
        "_id": "H203",
        "description": "Explosiv; Gefahr durch Feuer, Luftdruck oder Splitter, Spreng- und Wurfstücke.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P230", "P240", "P250", "P280", "P372", "P373", "P401", "P501"]
    },
    {
        "_id": "H204",
        "description": "Gefahr durch Feuer oder Splitter, Spreng- und Wurfstücke.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P234", "P240", "P250", "P280", "P370+P372+P380+P373", "P401", "P503"]
    },
    {
        "_id": "H205",
        "description": "Gefahr der Massenexplosion bei Feuer.",
        "pharsen_reference_id": "Extrem entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P230", "P240", "P250", "P280", "P372", "P373", "P401", "P501"]    
    },
    {
        "_id": "H206",
        "description": "Gefahr durch Feuer, Druckstoß oder Sprengstücke; erhöhte Explosionsgefahr, wenn das Desensibilisierungsmittel reduziert wird.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P212", "P230", "P233", "P280", "P370+P380+P375", "P401", "P501"]
    },
    {
        "_id": "H207",
        "description": "Gefahr durch Feuer oder Sprengstücke; erhöhte Explosionsgefahr, wenn das Desensibilisierungsmittel reduziert wird.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P212", "P230", "P233", "P280", "P370+P380+P375", "P401", "P501"]
    },
    {
        "_id": "H208",
        "description": "Gefahr durch Feuer, erhöhte Explosionsgefahr, wenn das Desensibilisierungsmittel reduziert wird.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P371+P380+P375", "P401", "P501"]
    },
    {
        "_id": "H220",
        "description": "Extrem entzündbares Gas.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P230", "P210", "P222", "P280", "P377", "P381", "P403"]
    },
    {
        "_id": "H221",
        "description": "Entzündbares Gas.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P377", "P381", "P403"]
    },
    {
        "_id": "H222",
        "description": "Extrem entzündbares Aerosol.",
        "pharsen_reference_id": "Extrem entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P211", "P251", "P410+P412"]
    },
    {
        "_id": "H223",
        "description": "Entzündbares Aerosol.",
        "pharsen_reference_id": "Entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P211", "P251", "P410+P412"]
    },
    {
        "_id": "H224",
        "description": "Flüssigkeit und Dampf extrem entzündbar.",
        "pharsen_reference_id": "Extrem entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P233", "P240", "P241", "P242", "P243", "P280", "P303+P361+P353", "P370+P378", "P403+P235", "P501"]
    },
    {
        "_id": "H225",
        "description": "Flüssigkeit und Dampf leicht entzündbar.",
        "pharsen_reference_id": "Leicht entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P233", "P240", "P241", "P242", "P243", "P280", "P303+P361+P353", "P370+P378", "P403+P235", "P501"]
    },
    {
        "_id": "H226",
        "description": "Flüssigkeit und Dampf entzündbar.",
        "pharsen_reference_id": "Entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P233", "P240", "P241", "P242", "P243", "P280", "P303+P361+P353", "P370+P378", "P403+P235", "P501"]
    },
    {
        "_id": "H228",
        "description": "Entzündbarer Feststoff.",
        "pharsen_reference_id": "Entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P240", "P241", "P280", "P370+P378"]
    },
    {
        "_id": "H229",
        "description": "Behälter steht unter Druck: kann bei Erwärmung bersten.",
        "pharsen_reference_id": "Entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P251", "P410+P412"]
    },
    {
        "_id": "H230",
        "description": "Kann auch in Abwesenheit von Luft explosionsartig reagieren.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P337", "P381", "P403"]
    },
    {
        "_id": "H231",
        "description": "Kann auch in Abwesenheit von Luft bei erhöhtem Druck und/oder erhöhter Temperatur explosionsartig reagieren.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P337", "P381", "P403"]
    },
    {
        "_id": "H232",
        "description": "Kann sich bei Kontakt mit Luft bei Erwärmung spontan entzünden.",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P222", "P280", "P377", "P381", "P403"]
    },
    {
        "_id": "H240",
        "description": "Erwärmung kann Explosion verursachen.",
        "pharsen_reference_id": "Explosiv",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P234", "P235", "P240", "P280", "P370+P372+P380+P373", "P403", "P410", "P411", "P420", "P501"]   
    },
    {
        "_id": "H241",
        "description": "Erwärmung kann Brand oder Explosion verursachen.",
        "pharsen_reference_id": "Explosiv ",
        "ghs_reference_id": "GHS01",
        "psatz_id": ["P210", "P234", "P235", "P240", "P280", "P370+P380+P375[+P378]", "P403", "P410", "P411", "P420", "P501"]
    },
    {
        "_id" : "H242",
        "description": "Erwärmung kann Brand verursachen.",
        "pharsen_reference_id": "Entzündbar",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P234", "P235", "P240", "P280", "P370+P378", "P403", "P410", "P411", "P420", "P501"]
    },
    {
        "_id": "H250",
        "description": "Entzündet sich in Berührung mit Luft von selbst.",
        "pharsen_reference_id": " Selbstentzündlich",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P210", "P222", "P231", "P233", "P280", "P302+P335+P334", "P370+P378"]
    },
    {
        "_id": "H251",
        "description": "Selbsterhitzungsfähig; kann in Brand geraten.",
        "pharsen_reference_id": "Selbstentzündlich",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P235", "P280", "P407", "P410", "P413", "P420"]
    },
    {
        "_id": "H252",
        "description": "In großen Mengen selbsterhitzungsfähig; kann in Brand geraten.",
        "pharsen_reference_id": "Selbstentzündlich",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P235", "P280", "P407", "P410", "P413", "P420"]
    },
    {
        "_id": "H260",
        "description": "In Berührung mit Wasser entstehen entzündbare Gase, die sich spontan entzündenkönnen.",
        "pharsen_reference_id": "Reagiert heftig mit Wasser",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P223", "P231+P232", "P280", "P302+P335+P334", "P370+P378", "P402+P404", "P501"]
    },
    {
        "_id": "H261",
        "description": "In Berührung mit Wasser entstehen entzündbare Gase.",
        "pharsen_reference_id": "Reagiert heftig mit Wasser",
        "ghs_reference_id": "GHS02",
        "psatz_id": ["P223", "P231+P232", "P280", "P302+P335+P334", "P370+P378", "P402+P404", "P501"]
    },
    {
        "_id": "H270",
        "description": "Kann Brand verursachen oder verstärken; Oxidationsmittel.",
        "pharsen_reference_id": "Oxidationsmittel",
        "ghs_reference_id": "GHS03",
        "psatz_id": ["P220", "P244", "P370+P376", "P403"]
    },
    {
        "_id": "H271",
        "description": "Kann Brand oder Explosion verursachen; starkes Oxidationsmittel.",
        "pharsen_reference_id": "Oxidationsmittel",
        "ghs_reference_id": "GHS03",
        "psatz_id": ["P210", "P220", "P280", "P283", "P306+P360", "P371+P380+P375", "P370+P378", "P420", "P501"]
    },
    {
        "_id": "H272",
        "description": "Kann Brand verstärken; Oxidationsmittel.",
        "pharsen_reference_id": "Oxidationsmittel",
        "ghs_reference_id": "GHS03",
        "psatz_id": ["P210", "P220", "P280", "P370+P378", "P501"]
    },
    {
        "_id": "H280",
        "description": "Enthält Gas unter Druck; kann bei Erwärmung explodieren.",
        "ghs_reference_id": "GHS04",
        "psatz_id": ["P410+P403"]
    },
    {
        "_id": "H281",
        "description": "Enthält tiefgekühltes Gas; kann Kälteverbrennungen oder -verletzungen verursachen.",
        "ghs_reference_id": "GHS04",
        "psatz_id": ["P282", "P403"]
    },
    {
        "_id": "H290",
        "description": "Kann gegenüber Metallen korrosiv sein.",
        "ghs_reference_id": "GHS05",
        "psatz_id": ["P234", "P390", "P406"]
    },
    {
        "_id": "H300",
        "description": "Lebensgefahr bei Verschlucken.",
        "pharsen_reference_id": "Lebensgefahr",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P264", "P270", "P321", "P330", "P405", "P501"]
    },
    {
        "_id": "H301",
        "description": "Giftig bei Verschlucken.",
        "pharsen_reference_id": "Giftig",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P264", "P270", "P321", "P330", "P405", "P501"]
    },
    {
        "_id": "H302",
        "description": "Gesundheitsschädlich bei Verschlucken.",
        "pharsen_reference_id": "Gesundheitsschädlich",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P264", "P270", "P330", "P501"]
    },
    {
        "_id": "H304",
        "description": "Kann bei Verschlucken und Eindringen in die Atemwege tödlich sein.",
        "pharsen_reference_id": "Aspirationsgefahr lebensgefährlich",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P331", "P405", "P501"]
    },
    {
        "_id": "H310",
        "description": "Lebensgefahr bei Hautkontakt.",
        "pharsen_reference_id": "Lebensgefahr",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P262", "P264", "P270", "P280", "P302+P352", "P321", "P361+P364", "P405", "P501"]
    },
    {
        "_id": "H311",
        "description": "Giftig bei Hautkontakt.",
        "pharsen_reference_id": "Giftig",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P280", "P302+P352", "P321", "P361+P364", "P405", "P501"]
    },
    {
        "_id": "H312",
        "description": "Gesundheitsschädlich bei Hautkontakt.",
        "pharsen_reference_id": "Gesundheitsschädlich",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P280", "P302+P352", "P321", "P362+P364", "P501"]
    },
    {
        "_id": "H314",
        "description": "Verursacht schwere Verätzungen der Haut und schwere Augenschäden.",
        "pharsen_reference_id": "Ätzend/Korrosiv",
        "ghs_reference_id": "GHS05",
        "psatz_id": ["P260", "P264", "P280", "P301+P330+P331", "P363", "P304+P340", "P321", "P405", "P501"]
    },
    {
        "_id": "H315",
        "description": "Verursacht Hautreizungen.",
        "pharsen_reference_id": "Reizend",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P264", "P280", "P302+P352", "P321", "P362+P364"]
    },
    {
        "_id": "H317",
        "description": "Kann allergische Hautreaktionen verursachen.",
        "pharsen_reference_id": "Allergisierend bei Hautkontakt",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P261", "P272", "P280", "P302+P352", "P333+P313", "P321", "P362+P364", "P501"]
    },
    {
        "_id": "H318",
        "description": "Verursacht schwere Augenschäden.",
        "pharsen_reference_id": "Ätzend/Korrosiv",
        "ghs_reference_id": "GHS05",
        "psatz_id": ["P280"]
    },
    {
        "_id": "H319",
        "description": "Verursacht schwere Augenreizung.",
        "pharsen_reference_id": "Reizend",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P280", "P305+P351+P338"]
    },
    {
        "_id": "H330",
        "description": "Lebensgefahr bei Einatmen.",
        "pharsen_reference_id": "Lebensgefahr",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P260", "P271", "P284", "P304+P340", "P320", "P403+P233", "P405", "P501"]
    },
    {
        "_id": "H331 ",
        "description": "Giftig bei Einatmen.",
        "pharsen_reference_id": "Giftig",
        "ghs_reference_id": "GHS06",
        "psatz_id": ["P261", "P271", "P304+P340", "P321", "P403+P233", "P405", "P501"]
    },
    {
        "_id": "H332",
        "description": "Gesundheitsschädlich bei Einatmen.",
        "pharsen_reference_id": "Gesundheitsschädlich",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P261", "P271", "P304+P340", "P317"]
    },
    {
        "_id": "H334",
        "description": "Kann bei Einatmen Allergie, asthmaartige Symptome oder Atembeschwerden verursachen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P261", "P284", "P304+P340", "P501"]
    },
    {
        "_id": "H335",
        "description": "Kann die Atemwege reizen.",
        "pharsen_reference_id": "Reizend",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P261", "P271", "P304+P340", "P403+P233", "P405", "P501"]
    },
    {
        "_id": "H336",
        "description": "Kann Schläfrigkeit und Benommenheit verursachen.",
        "pharsen_reference_id": "Betäubend",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P261", "P271", "P304+P340", "P403+P233", "P405", "P501"]
    },
    {
        "_id": "H340",
        "description": "Kann genetische Defekte verursachen <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 1",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P405", "P501"]
    },
    {
        "_id": "H341",
        "description": "Kann vermutlich genetische Defekte verursachen <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 2",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P405", "P501"]
    },
    {
        "_id": "H350",
        "description": "Kann Krebs erzeugen <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 1",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H350i",
        "description": "Kann bei Einatmen Krebs erzeugen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H351",
        "description": "Kann vermutlich Krebs erzeugen <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 2",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360",
        "description": "Kann die Fruchtbarkeit beeinträchtigen oder das Kind im Mutterleib schädigen <konkrete Wirkung angeben, sofern bekannt> <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 1",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360F",
        "description": "Kann die Fruchtbarkeit beeinträchtigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360D",
        "description": "Kann das Kind im Mutterleib schädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360FD",
        "description": "Kann die Fruchtbarkeit beeinträchtigen. Kann das Kind im Mutterleib schädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360Fd",
        "description": "Kann die Fruchtbarkeit beeinträchtigen. Kann vermutlich das Kind im Mutterleib schädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H360Df",
        "description": "Kann das Kind im Mutterleib schädigen. Kann vermutlich die Fruchtbarkeit einträchtigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H361",
        "description": "Kann vermutlich die Fruchtbarkeit beeinträchtigen oder das Kind im Mutterleib schädigen <konkrete Wirkung angeben, sofern bekannt> <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "KMR–Stoff Kat. 2",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405","P501"]
    },
    {
        "_id": "H361f",
        "description": "Kann vermutlich die Fruchtbarkeit beeinträchtigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H361d",
        "description": "Kann vermutlich das Kind im Mutterleib schädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H361fd",
        "description": "Kann vermutlich die Fruchtbarkeit beeinträchtigen. Kann vermutlich das Kind im Mutterleib chädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P280", "P405", "P501"]
    },
    {
        "_id": "H362",
        "description": "Kann Säuglinge über die Muttermilch schädigen.",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P260", "P263", "P264", "P270"]
    },
    {
        "_id": "H370",
        "description": "Schädigt die Organe <oder alle betroffenen Organe nennen, sofern bekannt> <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "Schädigt die Organe",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P260", "P264", "P270", "P321", "P405", "P501"]
    },
    {
        "_id": "H371",
        "description": "Kann die Organe schädigen <oder alle betroffenen Organe nennen, sofern bekannt> <Expositionsweg angeben, sofern schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "Kann die Organe schädigen",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P260", "P264", "P270", "P405", "P501"]
    },
    {
        "_id": "H372",
        "description": "Schädigt die Organe <alle betroffenen Organe nennen> bei längerer oder wiederholter Exposition <Expositionsweg angeben, wenn schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "Schädigt die Organe",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P260", "P264", "P270", "P501"]
    },
    {
        "_id": "H373",
        "description": "Kann die Organe schädigen <alle betroffenen Organe nennen, sofern bekannt> bei längerer oder wiederholter Exposition <Expositionsweg angeben, wenn schlüssig belegt ist, dass diese Gefahr bei keinem anderen Expositionsweg besteht>.",
        "pharsen_reference_id": "Kann die Organe schädigen",
        "ghs_reference_id": "GHS08",
        "psatz_id": ["P260", "P501"]
    },
    {
        "_id": "H300 + H310",
        "description": "Lebensgefahr bei Verschlucken oder Hautkontakt.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H300 + H330",
        "description": "Lebensgefahr bei Verschlucken oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H310 + H330",
        "description": "Lebensgefahr bei Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H300 + H310 + H330",
        "description": "Lebensgefahr bei Verschlucken, Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H301 + H311",
        "description": "Giftig bei Verschlucken oder Hautkontakt.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H301 + H331",
        "description": "Giftig bei Verschlucken oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H311 + H331",
        "description": "Giftig bei Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H301 + H311 + H331",
        "description": "Giftig bei Verschlucken, Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS06"
    },
    {
        "_id": "H302 + H312",
        "description": "Gesundheitsschädlich bei Verschlucken oder Hautkontakt",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "H302 + H332",
        "description": " Gesundheitsschädlich bei Verschlucken oder Einatmen.",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "H312 + H332",
        "description": "Gesundheitsschädlich bei Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "H302 + H312 + H332",
        "description": "Gesundheitsschädlich bei Verschlucken, Hautkontakt oder Einatmen.",
        "ghs_reference_id": "GHS07"
    },
    {
        "_id": "H400",
        "description": "Sehr giftig für Wasserorganismen.",
        "ghs_reference_id": "GHS09",
        "psatz_id": ["P273", "P391", "P501"]
    },
    {
        "_id": "H410",
        "description": "Sehr giftig für Wasserorganismen, mit langfristiger Wirkung.",
        "ghs_reference_id": "GHS09",
        "psatz_id": ["P273", "P391", "P501"]
    },
    {
        "_id": "H411",
        "description": "Giftig für Wasserorganismen, mit langfristiger Wirkung.",
        "ghs_reference_id": "GHS09",
        "psatz_id": ["P273", "P391", "P501"]
    },
    {
        "_id": "H412",
        "description": "Schädlich für Wasserorganismen, mit langfristiger Wirkung.",
        "psatz_id": ["P273", "P501"]
    },
    {
        "_id": "H413",
        "description": "Kann für Wasserorganismen schädlich sein, mit langfristiger Wirkung.",
        "psatz_id": ["P273", "P501"]
    },
    {
        "_id": "H420",
        "description": "Schädigt die öffentliche Gesundheit und die Umwelt durch Ozonabbau in der äußeren Atmosphäre.",
        "ghs_reference_id": "GHS07",
        "psatz_id": ["P502"]
    },
]
hsatz.insert_many(hsatz_data)

#EUH-satz
euhsatz_data = [
    {
        "_id": "EUH014",
        "description": "Reagiert heftig mit Wasser.",
    },
    {
        "_id": "EUH018",
        "description": "Kann bei Verwendung explosionsfähige/entzündbare Dampf/Luft-Gemische bilden.",
    },
    {
        "_id": "EUH019",
        "description": "Kann explosionsfähige Peroxide bilden.",
    },
    {
        "_id": "EUH044",
        "description": "Explosionsgefahr bei Erhitzen unter Einschluss.",
    },
    {
        "_id": "EUH029",
        "description": "Entwickelt bei Berührung mit Wasser giftige Gase.",
    },
    {
        "_id": "EUH031",
        "description": "Entwickelt bei Berührung mit Säure giftige Gase.",
    },
    {
        "_id": "EUH032",
        "description": "Entwickelt bei Berührung mit Säure sehr giftige Gase.",
    },
    {
        "_id": "EUH066",
        "description": "Wiederholter Kontakt kann zu spröder oder rissiger Haut führen.",
    },
    {
        "_id": "EUH070",
        "description": "Giftig bei Berührung mit den Augen.",
    },
    {
        "_id": "EUH071",
        "description": "Wirkt ätzend auf die Atemwege.",
    },
    {
        "_id": "EUH201",
        "description": "Enthält Blei. Nicht für den Anstrich von Gegenständen verwenden, die von Kindern gekaut oder gelutscht werden könnten.",
    },
    {
        "_id": "EUH201A",
        "description": "Achtung! Enthält Blei.",
    },
    {
        "_id": "EUH202",
        "description": "Cyanacrylat. Gefahr. Klebt innerhalb von Sekunden Haut und Augenlider zusammen. Darf nicht in die Hände von Kindern gelangen.",
    },
    {
        "_id": "EUH203",
        "description": "Enthält Chrom (VI). Kann allergische Reaktionen hervorrufen.",
    },
    {
        "_id": "EUH204",
        "description": "Enthält Isocyanate. Kann allergische Reaktionen hervorrufen.",
    },
    {
        "_id": "EUH205",
        "description": "Enthält epoxidhaltige Verbindungen. Kann allergische Reaktionen hervorrufen.",
    },
    {
        "_id": "EUH206",
        "description": "Achtung! Nicht zusammen mit anderen Produkten verwenden, da gefährliche Gase (Chlor) freigesetzt werden können.",
    },
    {
        "_id": "EUH207",
        "description": "Achtung! Enthält Cadmium. Bei der Verwendung entstehen gefährliche Dämpfe. Hinweise des Herstellers beachten. Sicherheitsanweisungen einhalten.",
    },
    {
        "_id": "EUH208",
        "description": "Enthält <Name des sensibilisierenden Stoffes>. Kann allergische Reaktionen hervorrufen.",
    },
    {
        "_id": "EUH209",
        "description": "Kann bei Verwendung leicht entzündbar werden.",
    },
    {
        "_id": "EUH209A",
        "description": "Kann bei Verwendung entzündbar werden.",
    },
    {
        "_id": "EUH210",
        "description": "Sicherheitsdatenblatt auf Anfrage erhältlich.",
    },
    {
        "_id": "EUH211",
        "description": "Achtung! Beim Sprühen können gefährliche lungengängige Tröpfchen entstehen. Aerosol oder Nebel nicht einatmen.",
    },
    {
        "_id": "EUH212",
        "description": "Achtung! Bei der Verwendung kann gefährlicher lungengängiger Staub entstehen. Staub nicht einatmen.",
    },
    {
        "_id": "EUH401",
        "description": "Zur Vermeidung von Risiken für Mensch und Umwelt die Gebrauchsanleitung einhalten.",
    }
]
euhsatz.insert_many(euhsatz_data)

#P-satz
psatz_data = [
    {
        "_id": "P101",
        "description": "Ist ärztlicher Rat erforderlich, Verpackung oder Kennzeichnungsetikett bereithalten.",
    },
    {
        "_id": "P102",
        "description": "Darf nicht in die Hände von Kindern gelangen.",
    },
    {
        "_id": "P103",
        "description": "Lesen Sie sämtliche Anweisungen aufmerksam und befolgen Sie diese.",
    },
    {
        "_id": "P201",
        "description": "Vor Gebrauch besondere Anweisungen einholen.",
    },
    {
        "_id": "P202",
        "description": "Vor Gebrauch alle Sicherheitshinweise lesen und verstehen.",
    },
    {
        "_id": "P210",
        "description": "Von Hitze, heißen Oberflächen, Funken, offenen Flammen sowie anderen Zündquellen fernhalten. Nicht rauchen.",
    },
    {
        "_id": "P211",
        "description": "Nicht gegen offene Flamme oder andere Zündquelle sprühen.",
    },
    {
        "_id": "P212",
        "description": "Erhitzen unter Einschluss und Reduzierung des Desensibilisierungsmittels vermeiden.",
    },
    {
        "_id": "P220",
        "description": "Von Kleidung und anderen brennbaren Materialien fernhalten.",
    },
    {
        "_id": "P222",
        "description": "Keinen Kontakt mit Luft zulassen.",
    },
    {
        "_id": "P223",
        "description": "Keinen Kontakt mit Wasser zulassen.",
    },
    {
        "_id": "P230",
        "description": "Feucht halten mit ...",
    },
    {
        "_id": "P231",
        "description": "Inhalt unter inertem Gas/… handhaben und aufbewahren.",
    },
    {
        "_id": "P232",
        "description": "Vor Feuchtigkeit schützen.",
    },
    {
        "_id": "P233",
        "description": "Behälter dicht verschlossen halten.",
    },
    {
        "_id": "P234",
        "description": "Nur in Originalverpackung aufbewahren.",
    },
    {
        "_id": "P235",
        "description": "Kühl halten.",
    },
    {
        "_id": "P240",
        "description": "Behälter und zu befüllende Anlage erden",
    },
    {
        "_id": "P241",
        "description": "Explosionsgeschützte [elektrische/Lüftungs-/Beleuchtungs-/…] Geräte verwenden",
    },
    {
        "_id": "P242",
        "description": "Funkenarmes Werkzeug verwenden.",
    },
    {
        "_id": "P243",
        "description": "Maßnahmen gegen elektrostatische Entladungen treffen.",
    },
    {
        "_id": "P244",
        "description": "Ventile und Ausrüstungsteile öl- und fettfrei halten.",
    },
    {
        "_id": "P250",
        "description": "Nicht schleifen/stoßen/reiben/...",
    },
    {
        "_id": "P251",
        "description": "Nicht durchstechen oder verbrennen, auch nicht nach Gebrauch.",
    },
    {
        "_id": "P260",
        "description": "Staub/Rauch/Gas/Nebel/Dampf/Aerosol nicht einatmen.",
    },
    {
        "_id": "P261",
        "description": "Einatmen von Staub/Rauch/Gas/Nebel/Dampf/Aerosol vermeiden.",
    },
    {
        "_id": "P262",
        "description": "Nicht in die Augen, auf die Haut oder auf die Kleidung gelangen lassen.",
    },
    {
        "_id": "P263",
        "description": "Berührung während Schwangerschaft und Stillzeit vermeiden.",
    },
    {
        "_id": "P264",
        "description": "Nach Gebrauch ... gründlich waschen.",
    },
    {
        "_id": "P270",
        "description": "Bei Gebrauch nicht essen, trinken oder rauchen.",
    },
    {
        "_id": "P271",
        "description": "Nur im Freien oder in gut belüfteten Räumen verwenden.",
    },
    {
        "_id": "P272",
        "description": "Kontaminierte Arbeitskleidung nicht außerhalb des Arbeitsplatzes tragen.",
    },
    {
        "_id": "P273",
        "description": "Freisetzung in die Umwelt vermeiden.",
    },
    {
        "_id": "P280",
        "description": "Schutzhandschuhe/Schutzkleidung/Augenschutz/Gesichtsschutz/Gehörschutz/… tragen.",
    },
    {
        "_id": "P282",
        "description": "Schutzhandschuhe mit Kälteisolierung und zusätzlich Gesichtsschild oder Augenschutz tragen.",
    },
    {
        "_id": "P283",
        "description": "Schwer entflammbare oder flammhemmende Kleidung tragen.",
    },
    {
        "_id": "P284",
        "description": "[Bei unzureichender Belüftung] Atemschutz tragen.",
    },
    {
        "_id": "P231+P232",
        "description": "Inhalt unter inertem Gas/… handhaben und aufbewahren. Vor Feuchtigkeit schützen.",
    },
    {
        "_id": "P301",
        "description": "BEI VERSCHLUCKEN",
    },
    {
        "_id": "P302",
        "description": "BEI BERÜHRUNG MIT DER HAUT:",
    },
    {
        "_id": "P303",
        "description": "BEI BERÜHRUNG MIT DER HAUT (oder dem Haar):",
    },
    {
        "_id": "P304",
        "description": "BEI EINATMEN:",
    },
    {
        "_id": "P305",
        "description": "BEI KONTAKT MIT DEN AUGEN:",
    },
    {
        "_id": "P306",
        "description": "BEI KONTAKT MIT DER KLEIDUNG:",
    },
    {
        "_id": "P308",
        "description": "BEI Exposition oder falls betroffen:",
    },
    {
        "_id": "P310",
        "description": "Sofort GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P311",
        "description": "GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P312",
        "description": "Bei Unwohlsein GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P313",
        "description": "Ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P314",
        "description": "Bei Unwohlsein ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P315",
        "description": "Sofort ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P320",
        "description": "Besondere Behandlung dringend erforderlich (siehe ... auf diesem Kennzeichnungsetikett).",
    },
    {
        "_id": "P321",
        "description": "Besondere Behandlung (siehe ... auf diesem Kennzeichnungsetikett).",
    },
    {
        "_id": "P330",
        "description": "Mund ausspülen.",
    },
    {
        "_id": "P331",
        "description": "KEIN Erbrechen herbeiführen.",
    },
    {
        "_id": "P332",
        "description": "Bei Hautreizung:",
    },
    {
        "_id": "P333",
        "description": "Bei Hautreizung oder -ausschlag:",
    },
    {
        "_id": "P334",
        "description": "In kaltes Wasser tauchen [oder nassen Verband anlegen]. 8. ATP",
    },
    {
        "_id": "P335",
        "description": "Lose Partikel von der Haut abbürsten.",
    },
    {
        "_id": "P336",
        "description": "Vereiste Bereiche mit lauwarmem Wasser auftauen. Betroffenen Bereich nicht reiben.",
    },
    {
        "_id": "P337",
        "description": "Bei anhaltender Augenreizung:",
    },
    {
        "_id": "P338",
        "description": "Eventuell vorhandene Kontaktlinsen nach Möglichkeit entfernen. Weiter ausspülen.",
    },
    {
        "_id": "P340",
        "description": "Die Person an die frische Luft bringen und für ungehinderte Atmung sorgen.",
    },
    {
        "_id": "P342",
        "description": "Bei Symptomen der Atemwege:",
    },
    {
        "_id": "P351",
        "description": "Einige Minuten lang behutsam mit Wasser ausspülen.",
    },
    {
        "_id": "P352",
        "description": "Mit viel Wasser/...waschen.",
    },
    {
        "_id": "P353",
        "description": "Haut mit Wasser abwaschen [oder duschen]. 8. ATP",
    },
    {
        "_id": "P360",
        "description": "Kontaminierte Kleidung und Haut sofort mit viel Wasser abwaschen und danach Kleidung ausziehen.",
    },
    {
        "_id": "P361",
        "description": "Alle kontaminierten Kleidungsstücke sofort ausziehen.",
    },
    {
        "_id": "P362",
        "description": "Kontaminierte Kleidung ausziehen.",
    },
    {
        "_id": "P363",
        "description": "Kontaminierte Kleidung vor erneutem Tragen waschen.",
    },
    {
        "_id": "P364",
        "description": "Und vor erneutem Tragen waschen.",
    },
    {
        "_id": "P370",
        "description": "Bei Brand:",
    },
    {
        "_id": "P371",
        "description": "Bei Großbrand und großen Mengen:",
    },
    {
        "_id": "P372",
        "description": "Explosionsgefahr.",
    },
    {
        "_id": "P373",
        "description": "KEINE Brandbekämpfung, wenn das Feuer explosive Stoffe/Gemische/Erzeugnisse erreicht.",
    },
    {
        "_id": "P375",
        "description": "Wegen Explosionsgefahr Brand aus der Entfernung bekämpfen.",
    },
    {
        "_id": "P376",
        "description": "Undichtigkeit beseitigen, wenn gefahrlos möglich.",
    },
    {
        "_id": "P377",
        "description": "Brand von ausströmendem Gas: Nicht löschen, bis Undichtigkeit gefahrlos beseitigt werden kann.",
    },
    {
        "_id": "P378",
        "description": "... zum Löschen verwenden.",
    },
    {
        "_id": "P380",
        "description": "Umgebung räumen.",
    },
    {
        "_id": "P381",
        "description": "Bei Undichtigkeit alle Zündquellen entfernen.",
    },
    {
        "_id": "P390",
        "description": "Verschüttete Mengen aufnehmen, um Materialschäden zu vermeiden.",
    },
    {
        "_id": "P391",
        "description": "Verschüttete Mengen aufnehmen.",
    },
    {
        "_id": "P301+P310",
        "description": "BEI VERSCHLUCKEN: Sofort GIFTINFORMATIONSZENTRUM/Arzt/.../ anrufen.",
    },
    {
        "_id": "P301+P312",
        "description": "BEI VERSCHLUCKEN: Bei Unwohlsein GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P302+P334",
        "description": "BEI BERÜHRUNG MIT DER HAUT: In kaltes Wasser tauchen [odernassen Verband anlegen].",
    },
    {
        "_id": "P302+P352",
        "description": "BEI BERÜHRUNG MIT DER HAUT: Mit viel Wasser/...waschen.",
    },
    {
        "_id": "P304+P340",
        "description": "BEI EINATMEN: Die Person an die frische Luft bringen und fürungehinderte Atmung sorgen.",
    },
    {
        "_id": "P306+P360",
        "description": "BEI KONTAKT MIT DER KLEIDUNG: Kontaminierte Kleidung und Haut sofort mit viel Wasser abwaschen und danach Kleidung ausziehen.",
    },
    {
        "_id": "P308+P311",
        "description": "BEI Exposition oder falls betroffen: GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P308+P313",
        "description": "BEI Exposition oder falls betroffen: Ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P332+P313",
        "description": "Bei Hautreizung: Ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P333+P313",
        "description": "Bei Hautreizung oder-ausschlag: Ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P336+P315",
        "description": "Vereiste Bereiche mit lauwarmem Wasser auftauen. Betroffenen Bereich nicht reiben. Sofort ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P337+P313",
        "description": "Bei anhaltender Augenreizung: Ärztlichen Rat einholen/ärztliche Hilfe hinzuziehen.",
    },
    {
        "_id": "P342+P311",
        "description": "Bei Symptomen der Atemwege: GIFTINFORMATIONSZENTRUM/Arzt/... anrufen.",
    },
    {
        "_id": "P361+P364",
        "description": "Alle kontaminierten Kleidungsstücke sofort ausziehen und vor erneutem Tragen waschen.",
    },
    {
        "_id": "P362+P364",
        "description": "Kontaminierte Kleidung ausziehen und vor erneutem Tragen waschen.",
    },
    {
        "_id": "P370+P376",
        "description": "Bei Brand: Undichtigkeit beseitigen, wenn gefahrlos möglich.",
    },
    {
        "_id": "P370+P378",
        "description": "Bei Brand: ... zum Löschen verwenden.",
    },
    {
        "_id": "P301+P330+P331",
        "description": "BEI VERSCHLUCKEN: Mund ausspülen. KEIN Erbrechen herbeiführen.",
    },
    {
        "_id": "P302+P335+P334",
        "description": "BEI BERÜHRUNG MIT DER HAUT: Lose Partikel von der Haut abbürsten. In kaltes Wasser tauchen [oder nassen Verband anlegen].",
    },
    {
        "_id": "P303+P361+P353",
        "description": "BEI BERÜHRUNG MIT DER HAUT (oder dem Haar): Alle kontaminierten Kleidungsstücke sofort ausziehen. Haut mit Wasser abwaschen [oder duschen].",
    },
    {
        "_id": "P305+P351+P338",
        "description": "BEI KONTAKT MIT DEN AUGEN: Einige Minuten lang behutsam mit Wasser spülen. Eventuell vorhandene Kontaktlinsen nach Möglichkeit entfernen. Weiter spülen.",
    },
    {
        "_id": "P370+P380+P375",
        "description": "Bei Brand: Umgebung räumen. Wegen Explosionsgefahr Brand aus der Entfernung bekämpfen.",
    },
    {
        "_id": "P371+P380+P375",
        "description": "Bei Großbrand und großen Mengen: Umgebung räumen. Wegen Explosionsgefahr Brand aus der Entfernung bekämpfen.",
    },
    {
        "_id": "P370+P372+P380+P373",
        "description": "Bei Brand: Explosionsgefahr. Umgebung räumen. KEINE Brandbekämpfung, wenn das Feuer explosive Stoffe/Gemische/Erzeugnisse erreicht.",
    },
    {
        "_id": "P370+P380+P375[+P378]",
        "description": "Bei Brand: Umgebung räumen. Wegen Explosionsgefahr Brand aus der Entfernung bekämpfen. [… zum Löschen verwenden.]",
    },
    {
        "_id": "P401",
        "description": "Aufbewahren gemäß …",
    },
    {
        "_id": "P402",
        "description": "An einem trockenen Ort aufbewahren.",
    },
    {
        "_id": "P403",
        "description": "An einem gut belüfteten Ort aufbewahren.",
    },
    {
        "_id": "P404",
        "description": "In einem geschlossenen Behälter aufbewahren.",
    },
    {
        "_id": "P405",
        "description": "Unter Verschluss aufbewahren",
    },
    {
        "_id": "P406",
        "description": "In korrosionsbeständigem/... Behälter mit korrosionsbeständiger Innenauskleidung aufbewahren.",
    },
    {
        "_id": "P407",
        "description": "Luftspalt zwischen Stapeln oder Paletten lassen.",
    },
    {
        "_id": "P410",
        "description": "Vor Sonnenbestrahlung schützen.",
    },
    {
        "_id": "P411",
        "description": "Bei Temperaturen nicht über ... °C/...°F aufbewahren.",
    },
    {
        "_id": "P412",
        "description": "Nicht Temperaturen über 50°C/122°F aussetzen.",
    },
    {
        "_id": "P413",
        "description": "Schüttgut in Mengen von mehr als ... kg/... lbs bei Temperaturen nicht über ... °C/... °F aufbewahren.",
    },
    {
        "_id": "P420",
        "description": "Getrennt aufbewahren.",
    },
    {
        "_id": "P402+P404",
        "description": "An einem trockenen Ort aufbewahren. In einem geschlossenen Behälter aufbewahren.",
    },
    {
        "_id": "P403+P233",
        "description": "An einem gut belüfteten Ort aufbewahren. Behälter dicht verschlossen halten.",
    },
    {
        "_id": "P403+P235",
        "description": "An einem gut belüfteten Ort aufbewahren. Kühl halten.",
    },
    {
        "_id": "P410+P403",
        "description": "Vor Sonnenbestrahlung schützen. An einem gut belüfteten Ort aufbewahren.",
    },
    {
        "_id": "P410+P412",
        "description": "Vor Sonnenbestrahlung schützen. Nicht Temperaturen über 50°C/122°F aussetzen.",
    },
    {
        "_id": "P501",
        "description": "Inhalt/Behälter ... zuführen.",
    },
    {
        "_id": "P502",
        "description": "Informationen zur Wiederverwendung oder Wiederverwertung beim Hersteller oder Lieferanten erfragen.",
    },
    {
        "_id": "P503 ",
        "description": "Informationen zur Entsorgung/Wiederverwertung/Wiederverwendung beim Hersteller/Lieferanten/… erfragen",
    }   
]
psatz.insert_many(psatz_data)