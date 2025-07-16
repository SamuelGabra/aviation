# Aviation

A simple model for global sustainable aviation. The model currently contains the documentation for the model

## Developer Guide

### Dependencies

This repository uses [uv](https://docs.astral.sh/uv) for comprehensive project management.
Dependency bounds are defined in [`pyproject.toml`](pyproject.toml) and the locked environment is specified in [`uv.lock`](uv.lock)

To create the virtual environment from lockfile, make sure you have uv installed and run:

```
uv sync
```

### Model/Analysis

This repository contains a single analysis script, [`aviation.py`](aviation.py), which implements the simple model for global aviation.
It outputs the required global fleet.

To execute the analysis script, run:

```
uv run python aviation.py
```
