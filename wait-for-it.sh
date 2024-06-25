#!/usr/bin/env bash
# Use this script to test if a given TCP host/port are available

# https://github.com/vishnubob/wait-for-it

# Check arguments
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 host:port [-t timeout] [-- command args...]"
    exit 1
fi

HOSTPORT=$1
shift

TIMEOUT=15
if [ "$1" == "-t" ]; then
    TIMEOUT=$2
    shift 2
fi

# Separate host and port
HOST=$(echo $HOSTPORT | cut -d: -f1)
PORT=$(echo $HOSTPORT | cut -d: -f2)

# Wait for the host/port to be available
timeout $TIMEOUT bash -c "until echo > /dev/tcp/$HOST/$PORT; do sleep 1; done"

# Run the command
exec "$@"
