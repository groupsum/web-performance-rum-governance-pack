# web-performance-rum-governance-pack

Installable SSOT governance pack for Navigation Timing, Resource Timing, User Timing, Performance Timeline, Reporting API, Beacon, and RUM evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:web-performance-rum`
- Priority: `P4.1`
- PyPI package: `web-performance-rum-governance-pack`
- Import package: `ssot_pack_web_performance_rum`
- GitHub repository: `groupsum/web-performance-rum-governance-pack`
- Reservation owner: `extension-pack:web-performance-rum-governance-pack`

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

- `spc:navigation-timing-entry-requirements` - Navigation Timing Entry Requirements
- `spc:navigation-timing-rum-derived-metric-requirements` - Navigation Timing RUM Derived Metric Requirements
- `spc:resource-timing-entry-requirements` - Resource Timing Entry Requirements
- `spc:resource-timing-privacy-filtering-requirements` - Resource Timing Privacy Filtering Requirements
- `spc:user-timing-mark-measure-requirements` - User Timing Mark Measure Requirements
- `spc:performance-timeline-observer-requirements` - Performance Timeline Observer Requirements
- `spc:performance-entry-export-envelope-requirements` - Performance Entry Export Envelope Requirements
- `spc:reporting-api-report-ingestion-requirements` - Reporting API Report Ingestion Requirements
- `spc:reporting-api-endpoint-group-requirements` - Reporting API Endpoint Group Requirements
- `spc:beacon-rum-delivery-requirements` - Beacon RUM Delivery Requirements
- `spc:beacon-payload-reliability-requirements` - Beacon Payload Reliability Requirements
- `spc:web-performance-rum-audit-evidence-requirements` - Web Performance RUM Audit Evidence Requirements

## Install With uv

```bash
uv add web-performance-rum-governance-pack
uv add ssot-registry web-performance-rum-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install web-performance-rum-governance-pack
uvx --from ssot-registry ssot pack sync . web-performance-rum-governance-pack
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
- PyPI package: https://pypi.org/project/web-performance-rum-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
