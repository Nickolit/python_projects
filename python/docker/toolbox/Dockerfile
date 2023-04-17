FROM anapsix/alpine-java
MAINTAINER Justin Commu

RUN mkdir /allure
RUN mkdir /allure-results
RUN mkdir /allure-report
RUN mkdir /allure-config

RUN apk update && \
	apk add ca-certificates && \
	update-ca-certificates && \
	apk add openssl && \
	apk add unzip

RUN wget https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.0.0/allure-2.0.0.tgz
RUN unzip allure-commandline.zip -d /allure
RUN rm allure-commandline.zip
ENV PATH="/allure/bin:${PATH}"
ENV ALLURE_CONFIG="/allure-config/allure.properties"

RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python3 py-pip && \
pip install pytest allure-python-commons allure-pytest Faker pytest pydantic
RUN apk --purge -v del py-pip
CMD tail -f /dev/null
WORKDIR /
COPY python/tests/test_sk_internall.py /
RUN pytest test_sk_internall.py --alluredir=allure-results

