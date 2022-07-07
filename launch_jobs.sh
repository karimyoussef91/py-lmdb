#!/bin/bash

for block_size in 2 8 32 128; do
    sbatch --drop-caches=pagecache --job-name=output_${block_size} start_incremental_privateer_job.sbatch ${block_size}
done
