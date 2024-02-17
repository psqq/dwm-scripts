#!/bin/bash

mv ~/.dwm.log ~/."dwm-$(date '+%Y-%m-%d %H:%M:%S').log"
mv ~/.dwm.error.log ~/."dwm.error-$(date '+%Y-%m-%d %H:%M:%S').log"
touch ~/.dwm.log
touch ~/.dwm.error.log
