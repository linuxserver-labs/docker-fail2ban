FROM ghcr.io/linuxserver/baseimage-alpine:3.16

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="nomandera"

# environment settings
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

RUN \
  echo "**** install runtime packages ****" && \
  apk add --no-cache --upgrade \
    curl \
    fail2ban \
    fail2ban-doc


# add local files
COPY root/ /
