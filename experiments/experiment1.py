"""
This is the first experiment
"""

import argparse
import os
import datetime

from common import utils
from common.logging_utils import MetaLogger

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hyper_param_directory",
                        required=False,
                        default="./hyper_parameters",
                        type=str)

    parser.add_argument("--hyper_parameter_name",
                        required=True,
                        help="0, 10, 20, etc. Corresponds to .hyper file",
                        default="0")  # OpenAI gym environment name

    parser.add_argument("--seed", default=0, help="seed",
                        type=int)  # Sets Gym, PyTorch and Numpy seeds

    parser.add_argument("--experiment_name",
                        type=str,
                        help="Experiment Name",
                        required=True)

    parser.add_argument("--run_title",
                        type=str,
                        help="subdirectory for this run",
                        required=True)

    args, unknown = parser.parse_known_args()
    other_args = {(utils.remove_prefix(key, '--'), val)
                  for (key, val) in zip(unknown[::2], unknown[1::2])}

    full_experiment_name = os.path.join(args.experiment_name, args.run_title)

    utils.create_log_dir(full_experiment_name)
    hyperparams_dir = utils.create_log_dir(
        os.path.join(full_experiment_name, "hyperparams"))

    params = utils.get_hyper_parameters(args.hyper_parameter_name,
                                        args.hyper_param_directory)

    params['hyper_parameters_name'] = args.hyper_parameter_name

    for arg_name, arg_value in other_args:
        utils.update_param(params, arg_name, arg_value)
    params['hyperparams_dir'] = hyperparams_dir
    params['start_time'] = str(datetime.datetime.now())
    params['seed'] = args.seed

    utils.save_hyper_parameters(params, args.seed)

    # The rest is up to you!
