FROM ubuntu:latest
RUN mkdir home/output
ADD IF.txt home/data/
ADD Limerick.txt home/data/
ADD app.py /home

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
	python3

CMD ["/home/app.py"]
ENTRYPOINT [ "python3" ]