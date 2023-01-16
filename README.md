# Tekla

### Project Description

Tekla is a conversational-AI assistant developed with Rasa that gives information about restaurants in Deggendorf (city in Bavaria).


### WHAT IS RASA?
Rasa is an open-source framework for building conversational AI. It provides a set of tools and libraries for building chatbots and virtual assistants that can understand natural language input and respond in a way that is useful to the user
### Installation
#### * Rasa Open Source:
Installation of the latest Rasa Open Source 2.0 version. [Guide](https://rasa.com/docs/rasa/2.x/installation)



### files Description  

* config.yml: Language is in English. The standard piplines and policies are used for model training.
* domain.yml: List of all used intents, entities, slots, actions and responses. These are defined in more detail in the corresponding files (nlu.yml, actions.py).
* stories.yml & rules.yml: These are used as training data in the training phase.
* endpoints.yml: For activating the URL to the action server (rasa run actions).
* restaurants.json: A json file containing the manually entered restaurants in Deggendorf (not all), because we couldn't get a Google API. It acts as a database

