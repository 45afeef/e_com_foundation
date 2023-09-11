# README for the `localhelp` Branch

## Overview
The `localhelp` branch is a dedicated branch for local development and automation tasks. It contains scripts and management commands that aid in populating the database and other local development tasks. This branch is separate from the main project and does not include any details about it.

## Management Commands
The `localhelp` branch includes several management commands:

1. **clear_db**: This command deletes all the model data in the database of the `listing_app`. You can run it using:
```bash
python manage.py clear_db
```

2. **feed_db**: This command reads data from the `data.xlsx` file located in the project directory and populates the database. It also takes files from the **media directory** to populate media models from `listing_app`. You can run it using:
```bash
python manage.py feed_db
```

3. **start**: This command runs several commands in sequence: `makemigrations`, `migrate`, creates a superuser with username `admin` and password `123`, and finally runs `feed_db`. You can run it using:
```bash
python manage.py start
```

## Purpose of the Branch
The purpose of this branch is to provide a separate environment for local development tasks, such as populating the database and running management commands. It helps keep these tasks separate from the main project, ensuring that they do not interfere with the main project's codebase.

Please note that this README only includes details about this branch (`localhelp`) and its specific features, not about the main project.