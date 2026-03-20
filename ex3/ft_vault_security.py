def vault_operation(path: str, label: str, write_content: str = "") -> None:
    with open(path, "w" if write_content else "r", encoding="us-ascii") as f:
        print(f"{label} vault opened with failsafe protocols\n")
        print(f"SECURE {label}:")
        if write_content:
            f.write(write_content)
            print(write_content, end="")
        else:
            print(f.read())
    print(f"{label} vault sealed.\n")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    vault_operation("../attachments/classified_data.txt", "EXTRACTION")
    vault_operation(
        "../attachments/security_protocols.txt",
        "PRESERVATION",
        "[CLASSIFIED] New security protocols archived\n",
    )
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
