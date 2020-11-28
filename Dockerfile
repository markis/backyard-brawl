FROM python:3
MAINTAINER m@rkis.cc
WORKDIR /brawl
ADD ./pyproject.toml /brawl/pyproject.toml
ADD ./requirements.txt /brawl/requirements.txt
RUN pip install -r requirements.txt
RUN pip install .

ADD . /brawl

CMD ["/bin/sh", "-c", "/brawl/job-docker.sh"]
