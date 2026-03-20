def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    access_file_name: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {access_file_name}")
    try:
        with open(
            f"../attachments/{access_file_name}", encoding="us-ascii"
        ) as f:
            print("Connection established...\n")
            sentence = f.read()
            print("RECOVERED DATA:")
            print(sentence)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
