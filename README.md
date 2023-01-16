# Tekla




### Beschreibung des Projekts:

Tekla ist ein Sprachassistent entwickelt mit Rasa, der informationen Über die Restaurants in Deggendorf gibt.


### Beschreibung der Dateien

* config.yml: Sprache ist auf englisch. Die standard-Piplines and Policies werden fürs Modelltraining verwendet.
* domain.yml: Auflistung aller verwendeten Intents, Entities, Slots, Actions und Responses. Die werden ausfühlicher in den entsprechenden Dateien definiert (nlu.yml, actions.py)
* stories.yml & rules.yml: Die werden als Trainingsdaten verwendet
* endpoints.yml: Für die Aktivierung der URL zum Action-Server (rasa run actions).
* restaurants.json: eine json-Datei, die die Restaurants in Deggendorf (nicht alle) enthält, da wir keine Google-API kriegen konnten

###### --> Mehr Info in Wiki
