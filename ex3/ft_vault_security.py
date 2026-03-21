def vault_operation(path: str, label: str, write_content: str = "") -> None:
    try:
        mode = "w" if write_content else "r"
        with open(path, mode, encoding="us-ascii") as f:
            print(f"{label} vault opened with failsafe protocols\n")
            print(f"SECURE {label}:")
            if write_content:
                f.write(write_content)
                print(write_content, end="")
            else:
                print(f.read())
        if f.closed:
            print(f"[INTEGRITY] Vault connection closed: {f.closed}")
            print(f"{label} vault sealed.\n")
        else:
            print(f"[WARNING] Vault connection not closed: {f.closed}")
    except FileNotFoundError:
        print("Archive not found in storage matrix")
    except PermissionError:
        print("Security protocols deny access")
    except UnicodeDecodeError:
        print("Archive data contains unreadable encoding")


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
