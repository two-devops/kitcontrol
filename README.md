# kitcontrol

It is a tool to automatically install applications and services on remote targets

Awesome tool for Install Kits ;)

## Install kitcontrol as editable local packages

```bash
pipenv install -e .
```

## Test with docker ssh image

<https://docs.linuxserver.io/images/docker-openssh-server>

```bash
docker run -d \
  --name=openssh-server \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e SUDO_ACCESS=true \
  -e PASSWORD_ACCESS=true \
  -e USER_NAME=kitcontrol \
  -e USER_PASSWORD=password \
  -p 2222:2222 \
  --restart unless-stopped \
  lscr.io/linuxserver/openssh-server:latest
```

```bash
ssh kitcontrol@localhost -p 2222
```

```bash
docker run -d \
  --name=openssh-server2 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e SUDO_ACCESS=true \
  -e PASSWORD_ACCESS=true \
  -e USER_NAME=kitcontrol \
  -e USER_PASSWORD=password \
  -p 22222:2222 \
  --restart unless-stopped \
  lscr.io/linuxserver/openssh-server:latest
```

```bash
ssh kitcontrol@localhost -p 22222
```
