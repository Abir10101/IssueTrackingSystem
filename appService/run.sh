#!/bin/sh

flask db upgrade
gunicorn --bind 0.0.0.0:5000 --reload application:application
