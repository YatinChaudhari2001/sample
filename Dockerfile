FROM python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 2500
CMD python server.py

