def build_redirect(target: str) -> str:
    base = "https://example.local"
    if target.startswith("/"):
        return f"{base}{target}"
    return target
