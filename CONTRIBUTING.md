## PMD
The project uses [PDM](https://pdm-project.org/latest/) for its development and package handling.

### Adding packages
PDM uses no `requirements.txt` new packages are installed using `pdm add <package>`.
If a package is only required during development use `pdm add -dG testing <package>`.

### Available commands
- `pdm test`:
    - installs the project
    - runs all tests in `tests`
- `pdm lint`:
    - runs flake8 on `src/wsi2brick` and `tests`
- `cov_report`:
    - runs pytest (without installation of the project)
    - generates an coverage report
    - shows the coverage report

### Virtual Environment
The virtual environment is created as part of pdm. It can be activated using `source .venv/bin/activate`.<br>
In most cases, this is not required and all commands can simply be run with `pdm run ...`.

## Pre-Commit Hooks
This repository uses pre-commit hooks to run some workflows before committing to GitHub. This aims to increase code quality and reduce the number of failed action runs in the repository.<br>
Run `pdm run pre-commit install` initially to enable the pre-commit script on commits.<br>
Afterwards, all files can be checked with `pdm run check-pre-commit`.
