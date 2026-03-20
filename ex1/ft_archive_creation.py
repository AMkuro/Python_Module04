def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    new_file_name: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {new_file_name}")
    try:
        f = open(
            f"../attachments/{new_file_name}", mode="w", encoding="us-ascii"
        )
        try:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            entries: list[str] = [
                "New quantum algorithm discovered",
                "Efficiency increased by 347%",
                "Archived by Data Archivist trainee",
            ]
            entry_num = 1
            for text in entries:
                entry = f"[ENTRY {entry_num:03d}] {text}"
                f.write(f"{entry}\n")
                print(entry)
                entry_num += 1
        finally:
            f.close()
            if f.closed:
                print("\nStorage unit sealed. Data inscription complete.")
            else:
                print(
                    "\n[WARNING] Storage unit not sealed. "
                    "Data inscription uncomplete."
                )
        print("")
        print(f"Archive '{new_file_name}' ready for long-term preservation.")
    except FileNotFoundError:
        print(
            "ERROR: Storage directory not found. "
            "Make attachments/ at the project directory."
        )


if __name__ == "__main__":
    main()
