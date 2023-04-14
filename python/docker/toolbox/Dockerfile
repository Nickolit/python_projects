FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip
RUN pip install pytest allure-python-commons allure-pytest Faker pytest pydantic
RUN apk --purge -v del py-pip
CMD tail -f /dev/null
