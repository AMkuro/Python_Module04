def crisis_handler(filename):
    content: str | None = None
    response: str | None = None
    status: str | None = None

    try:
        with open(f"../attachments/{filename}") as f:
            content = f.read()
    except FileNotFoundError:
        response = "Archive not found in storage matrix"
        status = "Crisis handled, system stable"
    except PermissionError:
        response = "Security protocols deny access"
        status = "Crisis handled, security maintained"

    if content is not None:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        status = "Normal operations resumed"
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print(f"RESPONSE: {response}")

    print(f"STATUS: {status}\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")
