#!/usr/bin/env python3
"""Import the API 26 declaration snapshot from a DevEco Studio SDK."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--deveco-app", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("references/JsEtsAPIReference/api26"))
    args = p.parse_args()
    root = args.deveco_app / "Contents" if (args.deveco_app / "Contents").is_dir() else args.deveco_app
    sdk = root / "sdk" / "default"
    metadata = json.loads((sdk / "sdk-pkg.json").read_text())["data"]
    if metadata.get("apiVersion") != "26" or metadata.get("releaseType") != "Release":
        raise SystemExit(f"expected API 26 Release SDK, got {metadata}")
    sources = {
        "openharmony-js": sdk / "openharmony/js/api",
        "hms-js": sdk / "hms/js/api",
        "hms-kits": sdk / "hms/ets/kits",
    }
    total = 0
    for bucket, source in sources.items():
        dest = args.output / bucket
        dest.mkdir(parents=True, exist_ok=True)
        for src in sorted(source.glob("*.d.ts")):
            body = src.read_text(errors="replace")
            (dest / f"{src.name}.md").write_text(
                f"# {src.name}\n\n"
                f"> API 26.0.0 Release declaration snapshot from SDK {metadata['version']}.\n\n"
                f"```ts\n{body}\n```\n"
            )
            total += 1
    print(json.dumps({"apiVersion": metadata["apiVersion"], "sdkVersion": metadata["version"], "files": total}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
