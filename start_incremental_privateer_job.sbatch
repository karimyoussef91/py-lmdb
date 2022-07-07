#!/bin/bash

#SBATCH --exclusive
#SBATCH --time=24:00:00

module load gcc/10.2.1

rm -rf /l/ssd/*

. /g/g90/youssef2/.bashrc
conda activate /p/vast1/youssef2/conda_envs/py_lmdb_privateer

export OMP_NUM_THREADS=128
export LD_LIBRARY_PATH=/g/g90/youssef2/privateer_github_private/build/lib:${LD_LIBRARY_PATH}
export privateer_block_size_bytes=$((${1}*1024*1024))

./run_incremental_privateer.sh ${privateer_block_size_bytes} filenames /l/ssd/lmdb_privateer_snapshots reddit_comments 

