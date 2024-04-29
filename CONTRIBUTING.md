# PMD
The project uses [PDM](https://pdm-project.org/latest/) for its development and package handling.

## Adding packages
PDM uses no `requirements.txt` new packages are installed using `pdm add <package>`.
If a package is only required during development use `pdm add -dG testing <package>`.

## Available commands
- `pdm test`:
    - installs the project
    - runs all tests in `tests` 
- `pdm lint`: 
    - runs flake8 on `src/wsi2brick` and `tests`

