def crisis_handler(filename: str) -> None:
    content: str | None = None
    response: str = "Unknown error occurred"
    status: str = "Crisis handled, cause unknown"

    f = None
    try:
        with open(f"../attachments/{filename}", encoding="us-ascii") as f:
            content = f.read()
    except FileNotFoundError:
        response = "Archive not found in storage matrix"
        status = "Crisis handled, system stable"
    except PermissionError:
        response = "Security protocols deny access"
        status = "Crisis handled, security maintained"
    except UnicodeDecodeError:
        response = "Archive data contains unreadable encoding"
        status = "Crisis handled, data format logged"
    except OSError:
        response = "Storage system failure detected"
        status = "Crisis handled, hardware check required"
    except Exception:
        response = "Unknown system anomaly encountered"
        status = "Crisis handled, diagnostics initiated"
    finally:
        if f is not None and not f.closed:
            print(f"[WARNING] Vault connection not closed: {f.closed}")

    if content is not None:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        status = "Normal operations resumed"
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print(f"RESPONSE: {response}")

    print(f"STATUS: {status}\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
