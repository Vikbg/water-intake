import argparse


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


def main() -> None:
    total_water_l: float = 0.0
    water_goal_l: float = 2.5

    parser = build_parser()
    args = parser.parse_args()

    if args.water_ml is not None:
        if args.water_ml < 0:
            parser.error("--add must be a non-negative integer (mL).")
        total_water_l += args.water_ml / 1000

    if args.stats:
        raw_progress = 10 * total_water_l / water_goal_l
        raw_percent = 100 * total_water_l / water_goal_l

        progress = max(0, min(10, int(raw_progress)))
        percent = max(0, min(100, int(raw_percent)))
        bar = "█" * progress + "░" * (10 - progress)

        print(f"[{bar}] {percent}%")


if __name__ == "__main__":
    main()
