#!/bin/bash
WORKING_DIR=/var/www/singongo.com/singongo
ACTIVATE_PATH=/var/www/singongo.com/env/bin/activate
cd ${WORKING_DIR}
source ${ACTIVATE_PATH}
exec $@
