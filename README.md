# Projet d'Affichage de Cryptomonnaies avec Arduino et Écran OLED
## Description du Projet
Ce projet utilise un microcontrôleur Arduino connecté à un écran OLED pour afficher les prix de différentes cryptomonnaies en temps réel. Les données des cryptomonnaies sont récupérées à partir de l'API de CoinGecko. Un bouton est utilisé pour changer la cryptomonnaie affichée sur l'écran.

### Matériel Nécessaire
- Rasberry Pi Pico 
- Écran OLED SSD1306
- Bouton poussoir
- Connexion Wi-Fi
- Câbles de connexion
### Bibliothèques Utilisées
- machine: Pour la gestion des pins de l'Arduino.
- ssd1306: Pilote pour l'écran OLED.
- network: Pour la connexion Wi-Fi.
- urequests: Pour les requêtes HTTP à l'API de CoinGecko.
- time et utime: Pour la gestion du temps.
### Installation
- Connectez votre Arduino à votre ordinateur et chargez MicroPython.
- Téléchargez les bibliothèques nécessaires (ssd1306.py, urequests.py) et le script principal (main.py) sur votre Arduino.
- Connectez l'écran OLED aux pins adéquates (SDA à la pin 4, SCL à la pin 5) et le bouton à la pin 15.
- Configurez votre connexion Wi-Fi en modifiant les variables ssid et password dans le script main.py.
### Utilisation
- Connectez l'Arduino à une source d'alimentation.
- L'Arduino se connectera automatiquement au Wi-Fi et commencera à récupérer les données des cryptomonnaies à partir de l'API de CoinGecko.
- L'écran OLED affichera le prix actuel de la cryptomonnaie sélectionnée.
- Appuyez sur le bouton pour changer la cryptomonnaie affichée.
 
