<!--intro-start-->

# `basic-package`

<!--intro-end-->

```
├── .github                 <- GitHub workflows, templates, and actions.
├── configs                 <- Store project/build/analysis configuration files here.
├── scripts                 <- Analysis examples or production scripts which rely on
│                              importing the actual Python package, e.g. running queries.
├── src/
│   └── basic_package/          <- Actual Python package where the main functionality goes.
│       └── __init__.py     <- Root-level package init file.
│       └── __main__.py     <- Main package script.
│       └── version.py      <- Should only contain the current package version number.
├── tests                   <- Unit and integration tests which can be run with `pytest` or `nox`.
├── .cookiecutter.json      <- Options specified during template generation.
├── .gitignore              <- Files and folders to ignore for git.
├── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
├── CONTRIBUTING.md         <- Documentation on how to contribute to the project.
├── *.code-workspace        <- Visual Studio Code workspace file.
├── environment.yml         <- The conda environment file for new virtual environments.
├── LICENSE                 <- Open source license.
├── noxfile.py              <- `nox` automation file for continuous integration steps.
├── pyproject.toml          <- Build system configuration for the project.
└── README.md               <- The top-level "read me" for the repository.
```

©️ Datajoint, 2022. Licensed under the MIT license.
