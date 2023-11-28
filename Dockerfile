ARG BASE_IMAGE=python:3.10.6
FROM $BASE_IMAGE

# Install the packages
RUN apt-get update && \
    apt-get install -y python3-opencv && \
    apt-get install -y zbar-tools && \
    apt-get install -y build-essential libzbar-dev
# Set the working directory to /app
WORKDIR /application
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install \
    fastapi \
    uvicorn \
    fastapi-directory-routing \
    python-dotenv

RUN pip3 install -r requirements.txt
EXPOSE 80
# CMD ["uvicorn manage:app --reload --host 0.0.0.0 --port 9000"]
CMD ["uvicorn", "manage:app", "--host", "0.0.0.0", "--port", "80"]