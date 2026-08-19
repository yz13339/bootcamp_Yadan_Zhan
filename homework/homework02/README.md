# Stage 02: Tooling Setup Practice

This folder contains the reproducible Python project scaffold created for the Stage 02 tooling setup assignment. It uses the existing `bootcamp_env` Jupyter kernel, keeps configuration values in a local `.env` file, loads them through a reusable helper in `src/config.py`, and includes a setup notebook that verifies the environment, configuration, and a small NumPy operation.

## Run the environment check

1. Activate the existing environment with `conda activate bootcamp_env`.
2. Open `notebooks/00_project_setup.ipynb`.
3. Select the `python3` kernel from `bootcamp_env` and run all cells from top to bottom.

The included `.env` contains dummy homework values only and is excluded from Git. Use `.env.example` as the safe configuration template.
