import argparse
import json
import datetime
import os

DATA_FILE = "data.json"
WATER_GOAL_L = 2.5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track daily water intake.")
    parser.add_argument(
        "--add",
        dest="water_ml",
        type=int,
        help="Add water intake in mL.",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show progress toward the daily goal.",
    )
    return parser


def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    data = load_json(DATA_FILE)

    today = datetime.date.today().isoformat()

    # Initialize today's entry if not present
    if today not in data:
        data[today] = {
            "water_l": 0.0,
            "goal_l": WATER_GOAL_L,
            "full": False,
        }

    if args.water_ml is not None:
        if args.water_ml < 0:
            parser.error("--add must be a non-negative integer (mL).")

        data[today]["water_l"] += args.water_ml / 1000
        data[today]["full"] = data[today]["water_l"] >= WATER_GOAL_L
        save_json(DATA_FILE, data)

    if args.stats:
        total_water_l = data[today]["water_l"]

        raw_progress = 10 * total_water_l / WATER_GOAL_L
        raw_percent = 100 * total_water_l / WATER_GOAL_L

        progress = max(0, min(10, int(raw_progress)))
        percent = max(0, min(100, int(raw_percent)))

        bar = "█" * progress + "░" * (10 - progress)

        print(f"[{bar}] {percent}% ({total_water_l:.2f}L / {WATER_GOAL_L}L)")


if __name__ == "__main__":
    main()
