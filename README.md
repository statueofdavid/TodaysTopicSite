# TodaysTopicSite

## Overview
A friend of mine and I are doing a podcast. 
I wanted to write the code responsible for:
- distributing the podcast
- whatever else comes along with it.

## How to Build

### Basic Steps
1. install python3
2. install pip3
3. python -m venv ~/.venv/dev
4. source ~/.venv/dev/bin/activate
5. pip install -r requirements.txt

### Of Note ...
- This project is using pip-tools and pipreqs to generate the requirements.txt

## Usage
1. cd todaysTopic/
2. python3 manager.py runserver
3. open a browser and goto `localhost:8000`
