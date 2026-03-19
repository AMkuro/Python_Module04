import sys


def input_stream(msg: str) -> str:
    return input(f"Input Stream active. Enter {msg}: ")


def output_stdout(msg: str) -> int:
    return sys.stdout.write(f"[STANDARD] {msg}\n")


def output_stderr(msg: str) -> int:
    return sys.stderr.write(f"[ALERT] {msg}\n")


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id: str = input_stream("archivist ID")
    status_report: str = input_stream("status report")
    print()
    output_stdout(f"Archive status from {archivist_id}: {status_report}")
    output_stderr("System diagnostic: Communication channels verified")
    output_stdout("Data transmission Complete")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
