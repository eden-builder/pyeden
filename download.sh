#!/bin/sh

UPLOAD_URL="http://app.edengame.net/upload2.php"
LIST_URL="http://app.edengame.net/list2.php"
REPORT_URL="http://app.edengame.net/report.php"
MAPS_URL="http://files.edengame.net/"
POPULAR_URL="http://files.edengame.net/popularlist.txt"

curl $MAPS_URL$1.eden.png > $1.eden.png
curl $MAPS_URL$1.eden > $1.eden