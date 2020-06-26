#!/usr/bin/env bash

while true; do
	echo Polling on `date`: `curl --connect-timeout 10 ${1}`
	sleep 1
done
