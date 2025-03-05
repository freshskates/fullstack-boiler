![tests](https://github.com/freshskates/python-backend-boiler/actions/workflows/tests.yml/badge.svg)

Python Backend Boilerplate

This guide will help you set up and run the Python backend project.

## Setup

1. Install uv:

```sh
   pip install uv
```

2. Create a virtual environment:

```sh
   uv venv
```

3. Install dependencies:

```sh
   uv pip install .
```

Alternatively, you can use:

```sh
uv sync
```

## Available Commands

After setup, you can use the following commands:

### Run Development Server

```sh
uv run task dev
```

### Start the Application

```sh
uv run task start
```

### Build Dockerfile

```sh
uv run task build
```

### Run Docker

For Windows:

```sh
uv run task dockerwin
```

For Unix-based systems:

```sh
uv run task dockerunix
```

### Run Tests

```sh
uv run task test
```
