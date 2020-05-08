FROM lsiobase/alpine

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="anoma"

# environment settings
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

RUN \
 echo "**** install runtime packages ****" && \
 apk add --no-cache --upgrade \
    curl \
    fail2ban && \
 echo "**** remove unnecessary fail2ban filters ****" && \
    rm \
    	/etc/fail2ban/jail.d/alpine-ssh.conf && \
echo "**** copy fail2ban default action and filter to /default ****" && \
mkdir -p /defaults/fail2ban && \
mv /etc/fail2ban/action.d /defaults/fail2ban/ && \
mv /etc/fail2ban/filter.d /defaults/fail2ban/
     

# add local files
COPY root/ /
