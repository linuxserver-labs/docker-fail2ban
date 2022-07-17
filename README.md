<!-- DO NOT EDIT THIS FILE MANUALLY  -->
<!-- Please read the https://github.com/linuxserver/docker-fail2ban/blob/master/.github/CONTRIBUTING.md -->

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)](https://linuxserver.io)

[![Blog](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Blog)](https://blog.linuxserver.io "all the things you can do with our containers including How-To guides, opinions and much more!")
[![Discord](https://img.shields.io/discord/354974912613449730.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Discord&logo=discord)](https://discord.gg/YWrKVTn "realtime support / chat with the community and the team.")
[![Discourse](https://img.shields.io/discourse/https/discourse.linuxserver.io/topics.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=discourse)](https://discourse.linuxserver.io "post on our community forum.")
[![Fleet](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Fleet)](https://fleet.linuxserver.io "an online web interface which displays all of our maintained images.")
[![GitHub](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub&logo=github)](https://github.com/linuxserver "view the source for all of our repositories.")
[![Open Collective](https://img.shields.io/opencollective/all/linuxserver.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=Supporters&logo=open%20collective)](https://opencollective.com/linuxserver "please consider helping us by either donating or contributing to our budget")

The [LinuxServer.io](https://linuxserver.io) team brings you another container release featuring:

* regular and timely application updates
* easy user mappings (PGID, PUID)
* custom base image with s6 overlay
* weekly base OS updates with common layers across the entire LinuxServer.io ecosystem to minimise space usage, down time and bandwidth
* regular security updates

Find us at:

* [Blog](https://blog.linuxserver.io) - all the things you can do with our containers including How-To guides, opinions and much more!
* [Discord](https://discord.gg/YWrKVTn) - realtime support / chat with the community and the team.
* [Discourse](https://discourse.linuxserver.io) - post on our community forum.
* [Fleet](https://fleet.linuxserver.io) - an online web interface which displays all of our maintained images.
* [GitHub](https://github.com/linuxserver) - view the source for all of our repositories.
* [Open Collective](https://opencollective.com/linuxserver) - please consider helping us by either donating or contributing to our budget

# [linuxserver/fail2ban](https://github.com/linuxserver/docker-fail2ban)

[![Scarf.io pulls](https://scarf.sh/installs-badge/linuxserver-ci/linuxserver%2Ffail2ban?color=94398d&label-color=555555&logo-color=ffffff&style=for-the-badge&package-type=docker)](https://scarf.sh/gateway/linuxserver-ci/docker/linuxserver%2Ffail2ban)
[![GitHub Stars](https://img.shields.io/github/stars/linuxserver/docker-fail2ban.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-fail2ban)
[![GitHub Release](https://img.shields.io/github/release/linuxserver/docker-fail2ban.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/linuxserver/docker-fail2ban/releases)
[![GitHub Package Repository](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitHub%20Package&logo=github)](https://github.com/linuxserver/docker-fail2ban/packages)
[![GitLab Container Registry](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=GitLab%20Registry&logo=gitlab)](https://gitlab.com/linuxserver.io/docker-fail2ban/container_registry)
[![Quay.io](https://img.shields.io/static/v1.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=linuxserver.io&message=Quay.io)](https://quay.io/repository/linuxserver.io/fail2ban)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/fail2ban.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/r/linuxserver/fail2ban)
[![Docker Stars](https://img.shields.io/docker/stars/linuxserver/fail2ban.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=stars&logo=docker)](https://hub.docker.com/r/linuxserver/fail2ban)
[![Jenkins Build](https://img.shields.io/jenkins/build?labelColor=555555&logoColor=ffffff&style=for-the-badge&jobUrl=https%3A%2F%2Fci.linuxserver.io%2Fjob%2FDocker-Pipeline-Builders%2Fjob%2Fdocker-fail2ban%2Fjob%2Fmaster%2F&logo=jenkins)](https://ci.linuxserver.io/job/Docker-Pipeline-Builders/job/docker-fail2ban/job/master/)
[![LSIO CI](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=CI&query=CI&url=https%3A%2F%2Fci-tests.linuxserver.io%2Flinuxserver%2Ffail2ban%2Flatest%2Fci-status.yml)](https://ci-tests.linuxserver.io/linuxserver/fail2ban/latest/index.html)

[Fail2ban](http://www.fail2ban.org/) is a daemon to ban hosts that cause multiple authentication errors.

[![fail2ban](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/fail2ban.png)](http://www.fail2ban.org/)

## Supported Architectures

We utilise the docker manifest for multi-platform awareness. More information is available from docker [here](https://github.com/docker/distribution/blob/master/docs/spec/manifest-v2-2.md#manifest-list) and our announcement [here](https://blog.linuxserver.io/2019/02/21/the-lsio-pipeline-project/).

Simply pulling `lscr.io/linuxserver/fail2ban:latest` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| x86-64 | ✅ | amd64-\<version tag\> |
| arm64 | ✅ | arm64v8-\<version tag\> |
| armhf| ✅ | arm32v7-\<version tag\> |

## Application Setup

App Setup Info

## Usage

Here are some example snippets to help you get started creating a container.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
version: "2.1"
services:
  fail2ban:
    image: lscr.io/linuxserver/fail2ban:latest
    container_name: fail2ban
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    volumes:
      - /path/to/appdata/config:/config
      - /var/log:/var/log:ro
      - /path/to/airsonic/airsonic.log:/remotelogs/airsonic/airsonic.log:ro #optional
      - /path/to/apache2/log:/remotelogs/apache2:ro #optional
      - /path/to/audit/audit.log:/remotelogs/audit/audit.log:ro #optional
      - /path/to/authelia/authelia.log:/remotelogs/authelia/authelia.log:ro #optional
      - /path/to/emby/embyserver.txt:/remotelogs/emby/embyserver.txt:ro #optional
      - /path/to/exim/mainlog:/remotelogs/exim/mainlog:ro #optional
      - /path/to/filebrowser/filebrowser.log:/remotelogs/filebrowser/filebrowser.log:ro #optional
      - /path/to/gitea/gitea.log:/remotelogs/gitea/gitea.log:ro #optional
      - /path/to/homeassistant/home-assistant.log:/remotelogs/homeassistant/home-assistant.log:ro #optional
      - /path/to/lighttpd/error.log:/remotelogs/lighttpd/error.log:ro #optional
      - /path/to/nginx/log:/remotelogs/nginx:ro #optional
      - /path/to/nzbget/log:/remotelogs/nzbget:ro #optional
      - /path/to/overseerr/overseerr.log:/remotelogs/overseerr/overseerr.log:ro #optional
      - /path/to/prowlarr/prowlarr.txt:/remotelogs/prowlarr/prowlarr.txt:ro #optional
      - /path/to/radarr/radarr.txt:/remotelogs/radarr/radarr.txt:ro #optional
      - /path/to/roundcube/errors:/remotelogs/roundcube/errors:ro #optional
      - /path/to/sabnzbd/log:/remotelogs/sabnzbd:ro #optional
      - /path/to/sonarr/sonarr.txt:/remotelogs/sonarr/sonarr.txt:ro #optional
      - /path/to/unificontroller/server.log:/remotelogs/unificontroller/server.log:ro #optional
      - /path/to/vaultwarden/vaultwarden.log:/remotelogs/vaultwarden/vaultwarden.log:ro #optional
      - /path/to/vsftpd.log:/remotelogs/vsftpd.log:ro #optional
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=fail2ban \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=America/New_York \
  -v /path/to/appdata/config:/config \
  -v /var/log:/var/log:ro \
  -v /path/to/airsonic/airsonic.log:/remotelogs/airsonic/airsonic.log:ro `#optional` \
  -v /path/to/apache2/log:/remotelogs/apache2:ro `#optional` \
  -v /path/to/audit/audit.log:/remotelogs/audit/audit.log:ro `#optional` \
  -v /path/to/authelia/authelia.log:/remotelogs/authelia/authelia.log:ro `#optional` \
  -v /path/to/emby/embyserver.txt:/remotelogs/emby/embyserver.txt:ro `#optional` \
  -v /path/to/exim/mainlog:/remotelogs/exim/mainlog:ro `#optional` \
  -v /path/to/filebrowser/filebrowser.log:/remotelogs/filebrowser/filebrowser.log:ro `#optional` \
  -v /path/to/gitea/gitea.log:/remotelogs/gitea/gitea.log:ro `#optional` \
  -v /path/to/homeassistant/home-assistant.log:/remotelogs/homeassistant/home-assistant.log:ro `#optional` \
  -v /path/to/lighttpd/error.log:/remotelogs/lighttpd/error.log:ro `#optional` \
  -v /path/to/nginx/log:/remotelogs/nginx:ro `#optional` \
  -v /path/to/nzbget/log:/remotelogs/nzbget:ro `#optional` \
  -v /path/to/overseerr/overseerr.log:/remotelogs/overseerr/overseerr.log:ro `#optional` \
  -v /path/to/prowlarr/prowlarr.txt:/remotelogs/prowlarr/prowlarr.txt:ro `#optional` \
  -v /path/to/radarr/radarr.txt:/remotelogs/radarr/radarr.txt:ro `#optional` \
  -v /path/to/roundcube/errors:/remotelogs/roundcube/errors:ro `#optional` \
  -v /path/to/sabnzbd/log:/remotelogs/sabnzbd:ro `#optional` \
  -v /path/to/sonarr/sonarr.txt:/remotelogs/sonarr/sonarr.txt:ro `#optional` \
  -v /path/to/unificontroller/server.log:/remotelogs/unificontroller/server.log:ro `#optional` \
  -v /path/to/vaultwarden/vaultwarden.log:/remotelogs/vaultwarden/vaultwarden.log:ro `#optional` \
  -v /path/to/vsftpd.log:/remotelogs/vsftpd.log:ro `#optional` \
  --restart unless-stopped \
  lscr.io/linuxserver/fail2ban:latest
```

## Parameters

Container images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

| Parameter | Function |
| :----: | --- |
| `-e PUID=1000` | for UserID - see below for explanation |
| `-e PGID=1000` | for GroupID - see below for explanation |
| `-e TZ=America/New_York` | Specify a timezone to use EG America/New_York |
| `-v /config` | Contains all relevant configuration files. |
| `-v /var/log:ro` | Host logs. Mounted as Read Only. |
| `-v /remotelogs/airsonic/airsonic.log:ro` | Path to airsonic log file. Mounted as Read Only. |
| `-v /remotelogs/apache2:ro` | Path to apache2 log folder. Mounted as Read Only. |
| `-v /remotelogs/audit/audit.log:ro` | Path to auditd log file. Mounted as Read Only. |
| `-v /remotelogs/authelia/authelia.log:ro` | Path to authelia log file. Mounted as Read Only. |
| `-v /remotelogs/emby/embyserver.txt:ro` | Path to emby log file. Mounted as Read Only. |
| `-v /remotelogs/exim/mainlog:ro` | Path to exim log file. Mounted as Read Only. |
| `-v /remotelogs/filebrowser/filebrowser.log:ro` | Path to filebrowser log file. Mounted as Read Only. |
| `-v /remotelogs/gitea/gitea.log:ro` | Path to gitea log file. Mounted as Read Only. |
| `-v /remotelogs/homeassistant/home-assistant.log:ro` | Path to homeassistant log file. Mounted as Read Only. |
| `-v /remotelogs/lighttpd/error.log:ro` | Path to lighttpd error log file. Mounted as Read Only. |
| `-v /remotelogs/nginx:ro` | Path to nginx log folder. Mounted as Read Only. |
| `-v /remotelogs/nzbget:ro` | Path to nzbget log folder. Mounted as Read Only. |
| `-v /remotelogs/overseerr/overseerr.log:ro` | Path to overseerr log file. Mounted as Read Only. |
| `-v /remotelogs/prowlarr/prowlarr.txt:ro` | Path to prowlarr log file. Mounted as Read Only. |
| `-v /remotelogs/radarr/radarr.txt:ro` | Path to radarr log file. Mounted as Read Only. |
| `-v /remotelogs/roundcube/errors:ro` | Path to roundcube error log file. Mounted as Read Only. |
| `-v /remotelogs/sabnzbd:ro` | Path to nzbget log folder. Mounted as Read Only. |
| `-v /remotelogs/sonarr/sonarr.txt:ro` | Path to sonarr log file. Mounted as Read Only. |
| `-v /remotelogs/unificontroller/server.log:ro` | Path to unificontroller server log file. Mounted as Read Only. |
| `-v /remotelogs/vaultwarden/vaultwarden.log:ro` | Path to vaultwarden log file. Mounted as Read Only. |
| `-v /remotelogs/vsftpd.log:ro` | Path to vsftpd log file. Mounted as Read Only. |

## Environment variables from files (Docker secrets)

You can set any environment variable from a file by using a special prepend `FILE__`.

As an example:

```bash
-e FILE__PASSWORD=/run/secrets/mysecretpassword
```

Will set the environment variable `PASSWORD` based on the contents of the `/run/secrets/mysecretpassword` file.

## Umask for running applications

For all of our images we provide the ability to override the default umask settings for services started within the containers using the optional `-e UMASK=022` setting.
Keep in mind umask is not chmod it subtracts from permissions based on it's value it does not add. Please read up [here](https://en.wikipedia.org/wiki/Umask) before asking for support.

## User / Group Identifiers

When using volumes (`-v` flags) permissions issues can arise between the host OS and the container, we avoid this issue by allowing you to specify the user `PUID` and group `PGID`.

Ensure any volume directories on the host are owned by the same user you specify and any permissions issues will vanish like magic.

In this instance `PUID=1000` and `PGID=1000`, to find yours use `id user` as below:

```bash
  $ id username
    uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

## Docker Mods

[![Docker Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=fail2ban&query=%24.mods%5B%27fail2ban%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=fail2ban "view available mods for this container.") [![Docker Universal Mods](https://img.shields.io/badge/dynamic/yaml?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=universal&query=%24.mods%5B%27universal%27%5D.mod_count&url=https%3A%2F%2Fraw.githubusercontent.com%2Flinuxserver%2Fdocker-mods%2Fmaster%2Fmod-list.yml)](https://mods.linuxserver.io/?mod=universal "view available universal mods.")

We publish various [Docker Mods](https://github.com/linuxserver/docker-mods) to enable additional functionality within the containers. The list of Mods available for this image (if any) as well as universal mods that can be applied to any one of our images can be accessed via the dynamic badges above.

## Support Info

* Shell access whilst the container is running: `docker exec -it fail2ban /bin/bash`
* To monitor the logs of the container in realtime: `docker logs -f fail2ban`
* container version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' fail2ban`
* image version number
  * `docker inspect -f '{{ index .Config.Labels "build_version" }}' lscr.io/linuxserver/fail2ban:latest`

## Updating Info

Most of our images are static, versioned, and require an image update and container recreation to update the app inside. With some exceptions (ie. nextcloud, plex), we do not recommend or support updating apps inside the container. Please consult the [Application Setup](#application-setup) section above to see if it is recommended for the image.

Below are the instructions for updating containers:

### Via Docker Compose

* Update all images: `docker-compose pull`
  * or update a single image: `docker-compose pull fail2ban`
* Let compose update all containers as necessary: `docker-compose up -d`
  * or update a single container: `docker-compose up -d fail2ban`
* You can also remove the old dangling images: `docker image prune`

### Via Docker Run

* Update the image: `docker pull lscr.io/linuxserver/fail2ban:latest`
* Stop the running container: `docker stop fail2ban`
* Delete the container: `docker rm fail2ban`
* Recreate a new container with the same docker run parameters as instructed above (if mapped correctly to a host folder, your `/config` folder and settings will be preserved)
* You can also remove the old dangling images: `docker image prune`

### Via Watchtower auto-updater (only use if you don't remember the original parameters)

* Pull the latest image at its tag and replace it with the same env variables in one run:

  ```bash
  docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --run-once fail2ban
  ```

* You can also remove the old dangling images: `docker image prune`

**Note:** We do not endorse the use of Watchtower as a solution to automated updates of existing Docker containers. In fact we generally discourage automated updates. However, this is a useful tool for one-time manual updates of containers where you have forgotten the original parameters. In the long term, we highly recommend using [Docker Compose](https://docs.linuxserver.io/general/docker-compose).

### Image Update Notifications - Diun (Docker Image Update Notifier)

* We recommend [Diun](https://crazymax.dev/diun/) for update notifications. Other tools that automatically update containers unattended are not recommended or supported.

## Building locally

If you want to make local modifications to these images for development purposes or just to customize the logic:

```bash
git clone https://github.com/linuxserver/docker-fail2ban.git
cd docker-fail2ban
docker build \
  --no-cache \
  --pull \
  -t lscr.io/linuxserver/fail2ban:latest .
```

The ARM variants can be built on x86_64 hardware using `multiarch/qemu-user-static`

```bash
docker run --rm --privileged multiarch/qemu-user-static:register --reset
```

Once registered you can define the dockerfile to use with `-f Dockerfile.aarch64`.

## Versions

* **01.08.22:** - Initial Release.
