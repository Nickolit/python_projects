FROM alpine
RUN apk add --no-cache curl wget busybox-extras netcat-openbsd allure python3 py-pip && \
pip install pytest allure-python-commons allure-pytest Faker pytest pydantic
RUN apk --purge -v del py-pip
CMD tail -f /dev/null
RUN pytest python/tests/test_sk_internall.py --alluredir=allure-results
