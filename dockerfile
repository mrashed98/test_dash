FROM amd64/ubuntu

COPY ./prepare_env.sh /prepare_env.sh
COPY ./requirements.txt /requirements.txt
COPY ./app /app

RUN bash prepare_env.sh
RUN pip3 install -r /requirements.txt

WORKDIR /app
RUN pytest

