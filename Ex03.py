import sys


def parse_log_line(line: str) -> dict:
    part = line.split(" ", 3)

    return {
        "date": part[0],
        "time": part[1],
        "level": part[2],
        "message": part[3].strip()
    }


def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                logs.append(parse_log_line(line))

    return logs


def filter_logs(logs: list, level: str) -> list:
    filtered = []

    for log in logs:
        if log["level"] == level:
            filtered.append(log)

    return filtered


def count_logs(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts


def display_log_counts(counts: dict):
    print("\nLevel    | Count")
    print("---------|------")

    for level, count in counts.items():
        print(f"{level:<8} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Надайте шлях до файлу")
        return

    file_path = sys.argv[1]

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    counts = count_logs(logs)
    display_log_counts(counts)

    # Якщо переданий другий аргумент (рівень)
    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered = filter_logs(logs, level)

        print(f"\nДеталі логів для рівня '{level}':")

        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
