# Stockholm

##Simulation de Ransomware Stockholm

Ce programme est une simulation de ransomware. Il est conçu pour crypter et décrypter des fichiers dans un dossier spécifique sur votre système. Le programme est purement éducatif et ne doit pas être utilisé à des fins malveillantes.

# Comment ça marche

Ce programme utilise la bibliothèque cryptography pour crypter et décrypter les fichiers. Lorsqu'il est lancé, le programme génère une clé de cryptage unique avec l'algorithme Fernet, puis parcourt tous les fichiers dans le dossier d'infection prédéfini qui ont des extensions spécifiques, et crypte ces fichiers. Les fichiers cryptés se voient ajouter l'extension .ft.

Pour décrypter les fichiers, l'utilisateur doit fournir la clé de cryptage originale. Le programme parcourt alors tous les fichiers avec l'extension .ft dans le dossier d'infection, décrypte ces fichiers et enlève l'extension .ft.

# Utilisation

Pour crypter les fichiers, exécutez simplement le programme sans arguments :
python3 stockholm.py

Pour décrypter les fichiers, utilisez l'option -r ou --reverse et fournissez la clé de cryptage :
python3 stockholm.py -r YOUR_ENCRYPTION_KEY

Pour exécuter le programme en mode silencieux (aucune sortie), utilisez l'option -s ou --silent :
python3 stockholm.py -s

# Makefile

Le Makefile contient plusieurs commandes pour faciliter l'utilisation du programme.

make acces : Rend le fichier stockholm.py exécutable.

make run ou make crypt : Exécute stockholm.py pour crypter les fichiers.

make crypt_silent : Exécute stockholm.py pour crypter les fichiers en mode silencieux.

make decrypt : Exécute stockholm.py pour décrypter les fichiers. Vous devez fournir la clé de cryptage en utilisant la variable key, par exemple : make decrypt key=YOUR_ENCRYPTION_KEY.

make decrypt_silent : Comme make decrypt, mais en mode silencieux.

make help : Affiche l'aide du programme.

make setup : Crée le dossier d'infection et y ajoute des fichiers de test.

Notez que make run, make crypt, make decrypt, et make help exécutent le programme stockholm.py avec Python 3. 

Assurez-vous donc que Python 3 est bien installé et est la version par défaut de Python sur votre système, ou modifiez ces commandes pour utiliser la commande Python appropriée.
