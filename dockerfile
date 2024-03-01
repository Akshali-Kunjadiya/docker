FROM ubuntu

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /streamlit-mysql-crud

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit","run","streamlit-crud.py"]

