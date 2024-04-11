

from itertools import product
import random
import asyncio
import sys

#deterministic pseudo randomness
random.seed(2137)

ports = {
    "epic": (20_000, 8000),
    "low": (20_010, 8010)
}

# EPIC_CARLA_WORLD_PORT = 20_000
# EPIC_CARLA_TM_PORT = 8000

# LOW_CARLA_WORLD_PORT = 20_010
# LOW_CARLA_TM_PORT = 8010
REPEAT = 1



def do_variants(params):
    variants = [combination for combination in product(*params.values())]
    random.shuffle(variants)
    return variants

def result_file_name(variant):

    config_strs = map(str, variant)

    return "_".join(config_strs)+".json"


async def run(cmd):
    print("Running command:")
    print(cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

def get_cmd(quality, fps):
    wp, tmp = ports[quality]    
    results_file = f"results/quality_{quality}_fps_{fps}_repeat_{REPEAT}.json"

    cmd = f"CUDA_VISIBLE_DEVICES=0 PORT={wp} TM_PORT={tmp} FPS={fps} REPETITIONS={REPEAT} CHECKPOINT_ENDPOINT={results_file} "
    cmd += "./leaderboard/scripts/experiment2/run_experiment.sh"

    return cmd


if __name__ == "__main__":

    quality = sys.argv[1]
    print(f"Doing tests in {quality} quality")

    fps_values = [20]
    random.shuffle(fps_values)
    for fps in fps_values:
        
        cmd = get_cmd(quality, fps)
        print("Running tests for fps: ", fps)
        print(cmd)
        # asyncio.run(run(cmd))
        
