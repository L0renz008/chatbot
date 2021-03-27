# chatbot
Python Chatbot
Mode d’emploi utilisateur Chat bot restaurant


Le dossier fournit et le git présentent plusieurs fichiers. Le code du chat bot qui intègre la recommandation système est dans bot.py. Le dossier rec_sys.py est le code complet du modèle de prédiction de “recommandation système”.  Les deux modèles créés et importée dans le bot : model_vins et model_desserts. Enfin il y a le read_me.


Mise en marche et installation :
Depuis un ordinateur ou un téléphone portable :
Installez, si ce n’est fait, discord, depuis : https://discord.com/download ou pour un téléphone portable, via l’Apple store (Iphone) ou Playstor (Android).
Ouvrir l’application Discord puis se rendre sur le serveur restaurant via ce lien : …
Vérifier que la version de python est supérieur ou égale à 3.7.
Aller sur le terminal et faire “$ pip install -r requirements.txt”
Lancer le programme python : bot.py 
Faire appel au chat grâce à la commande “!hello”.  Communiquer avec le chat. 


Présentation : les objectifs du projet de chatbot « serveur virtuel »
Ce chatbot s’apparente à un serveur de restaurant virtuel. Il permet au client de restaurant de l’accompagner sur toutes les étapes du service, de la connaissance du menu au paiement :
* S’inscrire dans le cadre du traçage des clients dans le cadre de la crise sanitaire (en respectant le RGPD)
* Ouvrir un compte pour que les choix effectués restent en mémoire (en particulier allergies alimentaires et plats bien notés)
* Prendre connaissance des boissons
* Prendre connaissance des suggestions de boisson du jour (cocktail du jour, vin du mois etc…)
* Prendre connaissance du menu, des plats du jour,
* Connaître, le cas échéant, la composition des plats, et  les calories associées
* Choisir un thème : menu vegan, menu hypocalorique, menu sans gluten, menu sportif…) afin d’avoir une suggestion de plats adaptée
* bénéficier de suggestions d’accords mets/vin, tout au long de la commande (hors d’œuvre, plat principal)
* Saisir son choix entre menu ou commande à la carte
* Saisir sa commande, avec d’éventuels commentaires (« sans oignons », « sans frites » etc…) 
* Cocher , le cas échéant, les allergies et intolérances alimentaires (sauf si le client est connecté sur son compte et ces informations pré-enregistrées avec son accord)
* Opter pour une option (payante ou non)  « client pressé » ou « client affamé » pour accélérer le service
* Patienter en attendant la commande en donnant accès  à des contenus informatifs liés à la commande (origine des plats, de certains ingrédients) ou à des partenaires touristiques (informations touristiques de type « que faire autour de vous », « suggestions de balade pour digérer », « suggestions pour se dépenser ») ou des commerçants des alentours
* Commander des suppléments en cours de repas (« verre de vin », ou autre boisson…)
* Prendre connaissance des desserts 
* Bénéficier d’une suggestion de café, thé (accord dessert/thé) ou infusion
* Commander les desserts, le café, le thé ou une infusion
* Payer en ligne son repas
* Recevoir le reçu éventuellement sur son adresse mail
* Payer un pourboire
* Noter le service, la qualité des plats
* Aux clients satisfaits proposer de laisser un commentaire sur Tripadvisor, la fourchette ou autre. 


Détail du processus : 


Le chatbot porte sur le choix du menu et la recommandation au client (vin….)
Le client est connecté sur Discord, à partir de son propre téléphone ou d’une tablette prêtée par le restaurant, éventuellement encastrée.
Une option vocale est à proscrire afin d’éviter d’amplifier le brouhaha dans le restaurant.
Sur la tablette, il sera nécessaire d’être vigilant sur l’hygiène, dans le cadre du respect des gestes barrières. 
Le client ouvre ainsi sur son téléphone l’application de messagerie Discord. 
Il saisit le « serveur » du restaurant.
Il écrit « !hello » pour déclencher le chat bot.
Le chatbot lui présente les services existant : 
* présenter la carte des boissons, la carte des plats, la carte du menu, 
* commander les boissons/les plats/le menu/le dessert/
* payer
* évaluer
* S’informer en attendant la commande
Le client coche le service dont il a besoin. 
Par exemple, si il choisit la carte des boissons, il peut cliquer sur les boissons pour en connaitre davantage (origine, saveur des vins, composition des cocktails….), cocher ses choix, et les envoyer. 
Le chatbot interagit en disant « bien reçu » et en suggérant les étapes suivantes : « voulez-vous commander les plats ? »  ou en relançant (« avez-vous choisi ?) ou en émettant des suggestions  (« envie de fraîcheur ? », « envie d’évasion « , « envie d’amertume », « envie d’une boisson soft », « envie de bulles »…).


Prototype développé :


Ce chatbot a été développé avec Python, pour sa richesse en librairies open source : NLP et Discord.
Le prototype porte uniquement sur la prise de connaissance du menu, la commande et la recommandation client. 


L’utilisateur entre dans le serveur et écrit “!hello” pour interagir avec le bot. 
Le bot répond et présente ses services disponibles ( nous nous contenterons de la commande ) : 
* Présenter le menu des plats; des entrées; des desserts. 
* Présenter les vins
        L’utilisateur réagira en écrivant un message lié aux services présentés et le chatbot    réorientera le client. 
Le chatbot peut conseiller un dessert ou un verre de vin en rapport avec le plat choisi et sur la base des anciennes commandes réalisées par l’ensemble des clients.
