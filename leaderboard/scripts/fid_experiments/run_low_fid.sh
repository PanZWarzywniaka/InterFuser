#!/bin/bash

export CUDA_VISIBLE_DEVICES=0
export PORT=20010 #for low fid simulator
export TM_PORT=8000
export FPS=10 #low fidelity
export REPETITIONS=1
export CHECKPOINT_ENDPOINT=results/low_fid_official_test.json

#if running headless (no visual output)
export SDL_VIDEODRIVER=dummy 

bash ./leaderboard/scripts/experiment2/run_experiment.sh