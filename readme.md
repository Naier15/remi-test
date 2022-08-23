# To start services execute next commands

# Using images.tar folder
## Link for loading docker images https://drive.google.com/drive/folders/1bAByEkntsRlkf1do2BBGeTJ6buJWkGbV?usp=sharing
## Put images into general folder with docker-compose.yaml file
docker load -i images.tar
docker-compose up

# Without images.tar
docker-compose up --build


# Access available through localhost:8000 or {local ip}:8000
# /      - directory for django ssr client
# /vue   - directory for vue spa client
# /admin - directory for admin site


# Login & password for admin
# friend - 123