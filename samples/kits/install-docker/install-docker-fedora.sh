dnf remove docker \
    docker-client \
    docker-client-latest \
    docker-common \
    docker-latest \
    docker-latest-logrotate \
    docker-logrotate \
    docker-selinux \
    docker-engine-selinux \
    docker-engine

dnf -y install dnf-plugins-core
dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo

# dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

#dnf list docker-ce  --showduplicates | sort -r
#
#docker-ce.x86_64    3:23.0.5-1.fc37    docker-ce-stable
#docker-ce.x86_64    3:23.0.4-1.fc37    docker-ce-stable

VERSION="3:23.0.5-1.fc37"

dnf -y install docker-ce-${VERSION} docker-ce-cli-${VERSION} containerd.io docker-buildx-plugin docker-compose-plugin

systemctl start docker