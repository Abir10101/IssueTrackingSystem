#!/bin/sh

gunicorn --bind 0.0.0.0:9000 --reload "app:run()"
