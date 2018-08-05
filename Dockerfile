FROM debian

# So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
# UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
# Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

# Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip wget git curl -y && \
  pip3 install pipenv && \
  wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

# To use - build (docker build) and start (docker run) the container.
# When running, you will probably want "-p 8000:8000" (for port forwarding)
# and "-v /some/local/dir:/some/container/dir" to attach a volume for your code.
# Then you can either attach the container for interactive use, or make a
# docker-compose.yml file to specify the run command (can also do the build).
# Rename/restart the container or rebuild fresh as preferred for your workflow.
# Also note that when starting a Django server you may need to specify the
# host/port, e.g. "./manage.py runserver 0:8000", and also add
# "0.0.0.0" to the ALLOWED_HOSTS list in settings (possibly via the env var)...
