#! /bin/sh
#$ -N bidsify_PROJECT                            # Name of job
#$ -S /bin/sh                                    # Bash script
#$ -j y                                          # Job error stream is merged with output stream
#$ -q veryshort.q                                # Queue to use
#$ -o PROJECT_PATH.log                           # Where to store logfile
#$ -u scdropbox                                  # Username

# Load environment modules
module load fsl/6.0.5.2 # for defacing
module load development/anaconda/3-8

conda activate $HOME/software/envs/bidsify

bidsify -c PROJECT_PATH/bidsify.yml -d PROJECT_PATH/parrec -o PROJECT_PATH/bids -v

