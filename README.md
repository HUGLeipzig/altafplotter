# altafplotter_public

Plotting alternative allele fractions and identifying UPDs

This tool is a python streamlit app, and allows for quick and interactive exploration of panel or exome-vcf files.

Additionally, all deviations from expected distributions of ROHs and inheritance are flagged accordingly, to allow a reliable detection of potential UPD-patterns.

Publication:

[altAFplotter: a web app for reliable UPD detection in NGS diagnostics](https://www.biorxiv.org/content/10.1101/2023.08.08.546838v1)

## Public version

A public version of the plotter is available [here](https://altafplotter.uni-leipzig.de/).

## Installation

Install python packages

`pip install -r requirements.txt`

Install additional tools needed:

[Tabix](https://wiki.wubrowse.org/How_to_install_tabix)

[BCFtools](https://samtools.github.io/bcftools/howtos/install.html)

## Starting the streamlit server

In order to start the streamlit server, run

```
streamlit run main.py
```

and your are good to go.

## Create docker container

`sudo podman build --build-arg VERSION=${APP_VERSION} --tag ${APP_VERSION} .`

## User guidelines

Guidelines on how to use the altafplotter and interpretation of potential UPD findings can be found [here](https://github.com/HUGLeipzig/altafplotter/blob/main/user_guideline/user_guideline.md).

**We had en error in the guidelines and the sidebar description "Flagging criteria" in the app, where the cutoffs for the inheritance ratio for trios and duos were swapped. This is now corrected.
The correct values are: trio:2, duo:5**

## Integration with Varvis/Gepado

We run a local version of this tool, that is integrated with our NGS-evaluation software Varvis and our LIMS Gepado.

In order to connect Varvis:
1. activate the respective toggle in `settings/settings.py` : `toggle_varvis = True`
2. add your varvis credentials to: `settings/credentials.py`

## Build Docker

You can build the docker container with:
```
sudo docker build --build-arg VERSION=${APP_VERSION} --tag ${APP_VERSION} .
```
and create the container with:
```
sudo docker create  \
    -it --restart always \
    --privileged \
    --volume log:/var/log \
    --env-file docker/settings-test.env \
    --cpus 2 \
    --memory 2G \
    -p 8880:8880 \
    --name altafplotter \
    altafplotter:{tag}

sudo docker run altafplotter
```
