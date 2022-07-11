#!/bin/bash


export PRIVATEER_BLOCK_SIZE=${1}
export INPUT_FILES_LIST=${2}
export PRIVATEER_BASE_PATH=${3}
export INITIAL_DATABASE_NAME=${4}

first_file=$(head -n 1 ${INPUT_FILES_LIST})

while IFS= read -r line
do
    if [[ "$line" == "${first_file}" ]]; then
        python examples/incremental_snapshots_privateer.py /p/lustre3/youssef2/Reddit_comments_by_year/${line} ${PRIVATEER_BASE_PATH} ${INITIAL_DATABASE_NAME} "db_${line}" "1"
    else
        python examples/incremental_snapshots_privateer.py /p/lustre3/youssef2/Reddit_comments_by_year/${line} ${PRIVATEER_BASE_PATH} ${INITIAL_DATABASE_NAME} "db_${line}" "0"
    fi
    du -hs ${PRIVATEER_BASE_PATH}
    du -hs ${PRIVATEER_BASE_PATH}/blocks

    du -hs --apparent-size ${PRIVATEER_BASE_PATH}
    du -hs --apparent-size ${PRIVATEER_BASE_PATH}/blocks

    du -hs ${PRIVATEER_BASE_PATH}/"db_${line}"
    du -hs --apparent-size ${PRIVATEER_BASE_PATH}/"db_${line}"
done < "${INPUT_FILES_LIST}"
