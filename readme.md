# To start services execute next commands

# Using images.tar folder
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