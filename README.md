# ssot-pack-web-performance-rum

Installable SSOT governance pack for Navigation Timing, Resource Timing, User Timing, Performance Timeline, Reporting API, Beacon, and RUM evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:web-performance-rum`
- Priority: `P4.1`
- PyPI package: `ssot-pack-web-performance-rum`
- Import package: `ssot_pack_web_performance_rum`
- GitHub repository: `groupsum/web-performance-rum-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-web-performance-rum`

## Domain Focus

Web Performance And Real User Measurement

## Authority Sources

- Navigation Timing
- Resource Timing
- User Timing
- Performance Timeline
- Reporting API
- W3C Beacon API

## Included ADRs

- `adr:navigation-timing-rum-policy` - Navigation Timing RUM Policy
- `adr:resource-timing-rum-policy` - Resource Timing RUM Policy
- `adr:user-timing-instrumentation-policy` - User Timing Instrumentation Policy
- `adr:performance-timeline-observation-policy` - Performance Timeline Observation Policy
- `adr:browser-reporting-rum-policy` - Browser Reporting RUM Policy
- `adr:beacon-rum-delivery-policy` - Beacon RUM Delivery Policy

## Included SPECs

- `spc:navigation-timing-contract` - Navigation Timing Contract
- `spc:resource-timing-contract` - Resource Timing Contract
- `spc:user-timing-performance-timeline-contract` - User Timing Performance Timeline Contract
- `spc:reporting-api-rum-contract` - Reporting API RUM Contract

## Install With uv

```bash
uv add ssot-pack-web-performance-rum
uv add ssot-registry ssot-pack-web-performance-rum
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-web-performance-rum
uvx --from ssot-registry ssot pack sync . ssot-pack-web-performance-rum
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_web_performance_rum import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/web-performance-rum-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-web-performance-rum/
- SSOT Registry: https://pypi.org/project/ssot-registry/
