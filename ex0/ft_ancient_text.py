def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    access_file_name: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {access_file_name}")
    try:
        f = open(f"../attachments/{access_file_name}", encoding="us-ascii")
        try:
            print("Connection established...\n")
            sentence = f.read()
            print("RECOVERED DATA:")
            print(sentence)
        finally:
            f.close()
            if f.closed:
                print("\nStorage unit disconnected. Data recovery complete.")
            else:
                print(
                    "\n[WARNING] Storage unit not disconnected. "
                    "Data recovery uncomplete."
                )
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
