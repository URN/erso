#! /bin/sh

export SECRET_1=$(head -c 40 /dev/urandom | base64)
export SECRET_2=$(head -c 40 /dev/urandom | base64)

python3 -m tarkin