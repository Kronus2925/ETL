FROM apache/airflow:2.4.2
COPY requirements.txt /tmp/requirements.txt
RUN pip install --user --upgrade pip
RUN python3 -m pip install -r /tmp/requirements.txt