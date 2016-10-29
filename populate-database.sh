#!/bin/bash

PYTHON=".venv/bin/python"
CMD="${PYTHON} manage.py"

cd $(dirname $0)

${CMD} migrate --run-syncdb
${CMD} loaddata home/fixtures/sites.json
${CMD} loaddata about/fixtures/moments.json
${CMD} loaddata journal/fixtures/posts.json
echo "Creating a super user account (user: iamarosewyatt) ..."
${CMD} createsuperuser --username "iamarosewyatt" --email "arose@ardynrosewyatt.com"
