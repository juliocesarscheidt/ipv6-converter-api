# IPv6 Converter API Project

> This is an API project made with Python and Bottle using a virtual environment

[![Build Status](https://badgen.net/travis/julio-cesar-development/todo-vue?icon=travis)](https://travis-ci.org/julio-cesar-development/ipv6-converter-api)
[![GitHub Status](https://badgen.net/github/status/julio-cesar-development/ipv6-converter-api)](https://github.com/julio-cesar-development/ipv6-converter-api)

## Project setup

> Running with docker

```bash
# Build the image
docker image build --tag ipv6-converter-api .
# Run the image
docker container run --name ipv6-converter-api -p 8080:8080 ipv6-converter-api
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

## Authors

* **Julio Cesar** - *Initial work* - [Blackdevs](https://blackdevs.com.br)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
