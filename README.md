# Water Intake Tracker

A simple command-line application to track your daily water intake and monitor progress toward your hydration goals.

## Features

- **Track Water Intake**: Log water consumption in milliliters
- **Daily Progress**: View your progress toward the daily goal with a visual progress bar
- **Persistent Data**: Automatically saves your data to `data.json`
- **Easy-to-use CLI**: Simple command-line interface with intuitive arguments

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone or navigate to this directory
2. No external dependencies required (uses only Python standard library)

## Usage

### Adding Water Intake

Log your water intake in milliliters:

```bash
python hydra.py --add 500
```

This adds 500 mL to today's water intake.

### Viewing Daily Statistics

Display your progress toward the daily goal:

```bash
python hydra.py --stats
```

Output example:
```
[█████░░░░░] 50% (1.25L / 2.5L)
```

### Combining Arguments

You can combine both arguments:

```bash
python hydra.py --add 500 --stats
```

## Daily Goal

The default daily water intake goal is **2.5 liters (2500 mL)**. To change this, modify the `WATER_GOAL_L` constant in [hydra.py](hydra.py).

## Data Storage

Water intake data is stored in [data.json](data.json) with the following structure:

```json
{
    "YYYY-MM-DD": {
        "water_l": 1.5,
        "goal_l": 2.5,
        "full": false
    }
}
```

Each day is tracked separately, resetting the counter at midnight.

## Project Structure

```
.
├── hydra.py          # Main application script
├── data.json         # Data storage (auto-created)
├── README.md         # This file
└── .gitignore        # Git configuration
```

## License

This is a personal learning project.
