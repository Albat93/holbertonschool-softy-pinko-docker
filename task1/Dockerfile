FROM ubuntu:latest

# Mise à jour des paquets
RUN apt-get update && apt-get upgrade -y

# Installer Python3 et pip3
RUN apt-get install -y python3 python3-pip

# Éviter l’erreur "externally managed"
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED || true

# Installer Flask via pip3
RUN pip3 install flask

# Créer et utiliser le dossier /app
WORKDIR /app

# Copier le script Python dans l’image
COPY ./api.py /app/api.py

# Lancer le serveur Flask
CMD ["python3", "api.py"]
