ARG WHEEL_DIST="tmp/wheels"

FROM python:3.10.3-slim-bullseye as base

ENV _UWSGI_VERSION 2.0.20
ENV DEBIAN_FRONTEND=noninteractive

ARG WHEEL_DIST
ARG REQUIREMENTS_FILE

RUN echo deb http://deb.debian.org/debian bullseye contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
  && apt-get update \
  && apt-get --no-install-recommends install -y build-essential wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

RUN wget -O uwsgi-${_UWSGI_VERSION}.tar.gz https://github.com/unbit/uwsgi/archive/${_UWSGI_VERSION}.tar.gz \
    && tar zxvf uwsgi-*.tar.gz \
    && UWSGI_BIN_NAME=/usr/local/bin/uwsgi make -C uwsgi-${_UWSGI_VERSION} \
    && rm -Rf uwsgi-*

RUN pip install --no-cache-dir --upgrade pip

COPY ${REQUIREMENTS_FILE} /requirements.txt
RUN python3 -m pip wheel -w  "${WHEEL_DIST}" -r /requirements.txt

#######################################################
#######################################################

FROM python:3.10.3-slim-bullseye


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND=noninteractive

ARG WHEEL_DIST

COPY --from=base "${WHEEL_DIST}" "${WHEEL_DIST}"
COPY --from=base "/usr/local/bin/uwsgi" "/usr/local/bin/uwsgi"

RUN echo deb http://deb.debian.org/debian bullseye contrib non-free > /etc/apt/sources.list.d/debian-contrib.list \
    && apt-get update \
    && apt-get --no-install-recommends install -y gettext locales-all tzdata libpq-dev libmagic-dev libffi-dev \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

WORKDIR "${WHEEL_DIST}"

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir *.whl

WORKDIR /src

COPY . /src
COPY ./scripts /scripts

RUN chmod +x /scripts/*.sh

ENTRYPOINT ["/scripts/entrypoint.sh"]

CMD ["/scripts/start.sh"]
