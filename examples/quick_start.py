"""Inspect the installed pack identity."""

from ssot_pack_web_performance_rum import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:web-performance-rum"
print(metadata["origin"]["id"])
