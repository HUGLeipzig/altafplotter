FROM docker.io/phusion/baseimage:jammy-1.0.1

# Set bash
RUN rm /bin/sh && \
    ln -s /bin/bash /bin/sh

# Add UKL Certificates


# Update System
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

# Unattended Upgrades
ARG packagesToInstallForUnattendedUpgrades="unattended-upgrades"

RUN apt-get update && \
    apt-get install --no-install-recommends -y ${packagesToInstallForUnattendedUpgrades} && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean && \
    sed -i  -e 's|//Unattended-Upgrade::Mail "";|Unattended-Upgrade::Mail "root";|g' \
            -e 's|//Unattended-Upgrade::MailReport "on-change";|Unattended-Upgrade::MailReport "on-change";|g' \
            -e 's|//Unattended-Upgrade::Remove-Unused-Dependencies "false";|Unattended-Upgrade::Remove-Unused-Dependencies "true";|g' \
            /etc/apt/apt.conf.d/50unattended-upgrades

# Streamlit App
## Packages
ARG packagesToInstallForStreamlit="python3.10-venv python3 supervisor git tabix bcftools"

RUN apt-get update && \
    apt-get install --no-install-recommends -y ${packagesToInstallForStreamlit} && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

## Supervisor
RUN useradd -ms /bin/bash streamlit
COPY ./docker/supervisor_streamlit.conf /etc/supervisor/conf.d/streamlit.conf

## App
COPY ./source/ /usr/local/bin/StreamlitApp

WORKDIR /usr/local/bin/StreamlitApp

RUN python3 -m venv /usr/local/bin/streamlit_env && \
    source /usr/local/bin/streamlit_env/bin/activate && \
    pip install wheel && \
    pip install -r requirements.txt

# Add version to file from build argument
ARG VERSION
RUN echo ${VERSION} > /usr/local/bin/StreamlitApp/VERSION

CMD /etc/init.d/cron start && \
    touch /var/log/altafplotter.log && \
    chown streamlit:streamlit /var/log/altafplotter.log && \
    mkdir -p /var/log/supervisor && \
    chown -R streamlit:streamlit /var/log/supervisor && \
    /usr/bin/supervisord && \
    bash
