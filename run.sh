#!/bin/sh

exec flask run
killall flask
killall python

