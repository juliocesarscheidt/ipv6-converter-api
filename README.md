# IPv6 Converter API Project

> This is an API project made with Python and Bottle using a virtual environment

[![Build Status](https://badgen.net/travis/julio-cesar-development/todo-vue?icon=travis)](https://travis-ci.org/julio-cesar-development/ipv6-converter-api)
![License](https://badgen.net/badge/license/MIT/blue)
[![GitHub Status](https://badgen.net/github/status/julio-cesar-development/ipv6-converter-api)](https://github.com/julio-cesar-development/ipv6-converter-api)

## API Specification

[See Specification - Swagger](https://app.swaggerhub.com/apis-docs/julio-cesar/ipv6-converter-api/1.0.0#/default/get_api_v1_convert)

## Project setup

> To run all services you must execute the following command with docker-compose

```bash
# Build all images and run the containers
docker-compose up -d
# Then access http://localhost:8000/swagger-docs to see the swagger documentation
```

## Project setup API

> Running with docker

```bash
# Build the image
docker image build --tag ipv6-converter-api -f Dockerfile .
# Run the image
docker container run -d --name ipv6-converter-api -p 5000:5000 ipv6-converter-api
```

> Running with docker-compose

```bash
# Run the API
docker-compose up -d api
```

> Running appart

```bash
# Install Python and pip
apt-get install -y python3.7 python3-pip
# Install venv
pip install virtualenv
# Create virtual env
virtualenv venv -p python3.7
# Activate venv
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run server
python -u app/server.py
```

## Project setup Docs

> Running with docker

```bash
# Build the image
docker image build --tag ipv6-converter-docs -f Dockerfile-docs .
# Run the image
docker container run -d --name ipv6-converter-docs -p 8000:8000 ipv6-converter-docs
```

> Running with docker-compose

```bash
# Run the docs
docker-compose up -d docs
```

> Running appart

```bash
# Go to docs directory
cd ./swagger-docs
# Install dependencies
npm i
# Run server
npm start
```

## Usage

> Example of API usage with cURL

```bash
# Endpoint /api/v1/valid_ipv4 running at http://localhost:5000
curl --request GET \
  --url 'http://localhost:5000/api/v1/valid_ipv4?ipv4=192.168.100.255' \
  --header 'content-type: application/json'
# Endpoint /api/v1/convert_ipv6 running at http://localhost:5000
curl --request GET \
  --url 'http://localhost:5000/api/v1/convert_ipv6?ipv6_prefix=2000:ffff:ffff:ffff&mac=ff-ff-ff-ff-ff-ff' \
  --header 'content-type: application/json'
```

## Authors

* **Julio Cesar** - *Initial work* - [Blackdevs](https://blackdevs.com.br)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
