# RL Scaffolding
When starting a new project, I'll clone this repository as a starting place. It should make experimentation with the type of logging I prefer easier.


## Steps
1. Download this repo.
2. Change the remote origin to where you want your project to live: `git remote rm origin && git remote add origin git@github.com:samlobel/my_new_repo.git`
3. Change the name of the folder from "rl_scaffolding" to something related to your project
4. Change the name of the "package" directory to something related to your project
5. Change the "name" field in `setup.py`. 
6. Make a >=python3.7 virtual environment. Do "pip install -e ." from this directory to install your package!
7. Commit all your changes, and push!

#### Example that works:

`python experiments/experiment1.py --hyper_parameter_name 00 --experiment_name ./results/testing --run_title testing --learning_rate 100.0`