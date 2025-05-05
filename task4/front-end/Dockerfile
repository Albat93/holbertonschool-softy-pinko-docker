FROM ubuntu:latest
FROM nginx:latest

# Copier les fichiers du front-end dans le dossier web de Nginx
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copier la configuration Nginx personnalisée
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
