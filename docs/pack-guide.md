# Web Performance And Real User Measurement pack guide

Installable SSOT governance pack for Navigation Timing, Resource Timing, User Timing, Performance Timeline, Reporting API, Beacon, and RUM evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `web-performance-rum-governance-pack` is an installable SSOT governance pack for Web Performance And Real User Measurement. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern web performance and real user measurement, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`web-performance-rum-governance-pack`](https://pypi.org/project/web-performance-rum-governance-pack/)
- GitHub package repository: [`groupsum/web-performance-rum-governance-pack`](https://github.com/groupsum/web-performance-rum-governance-pack)
- Import package: `ssot_pack_web_performance_rum`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:web-performance-rum`
- PyPI package: `web-performance-rum-governance-pack`
- Import package: `ssot_pack_web_performance_rum`
- GitHub repository: [groupsum/web-performance-rum-governance-pack](https://github.com/groupsum/web-performance-rum-governance-pack)
- Reservation owner: `extension-pack:web-performance-rum-governance-pack`

## Domain Focus

Web Performance And Real User Measurement

## Authority Sources

- [Navigation Timing](https://w3c.github.io/navigation-timing/)
- [Resource Timing](https://w3c.github.io/resource-timing/)
- [User Timing](https://w3c.github.io/user-timing/)
- [Performance Timeline](https://w3c.github.io/performance-timeline/)
- [Reporting API](https://w3c.github.io/reporting/)
- [W3C Beacon API](https://www.w3.org/TR/beacon/)

## Included ADRs

- [`adr:navigation-timing-rum-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1001-navigation-timing-rum-policy.yaml) - Navigation Timing RUM Policy
- [`adr:resource-timing-rum-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1002-resource-timing-rum-policy.yaml) - Resource Timing RUM Policy
- [`adr:user-timing-instrumentation-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1003-user-timing-instrumentation-policy.yaml) - User Timing Instrumentation Policy
- [`adr:performance-timeline-observation-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1004-performance-timeline-observation-policy.yaml) - Performance Timeline Observation Policy
- [`adr:browser-reporting-rum-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1005-browser-reporting-rum-policy.yaml) - Browser Reporting RUM Policy
- [`adr:beacon-rum-delivery-policy`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/adr/ADR-1006-beacon-rum-delivery-policy.yaml) - Beacon RUM Delivery Policy

## Included SPECs

- [`spc:navigation-timing-entry-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2001-navigation-timing-entry-requirements.yaml) - Navigation Timing Entry Requirements
- [`spc:navigation-timing-rum-derived-metric-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2002-navigation-timing-rum-derived-metric-requirements.yaml) - Navigation Timing RUM Derived Metric Requirements
- [`spc:resource-timing-entry-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2003-resource-timing-entry-requirements.yaml) - Resource Timing Entry Requirements
- [`spc:resource-timing-privacy-filtering-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2004-resource-timing-privacy-filtering-requirements.yaml) - Resource Timing Privacy Filtering Requirements
- [`spc:user-timing-mark-measure-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2005-user-timing-mark-measure-requirements.yaml) - User Timing Mark Measure Requirements
- [`spc:performance-timeline-observer-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2006-performance-timeline-observer-requirements.yaml) - Performance Timeline Observer Requirements
- [`spc:performance-entry-export-envelope-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2007-performance-entry-export-envelope-requirements.yaml) - Performance Entry Export Envelope Requirements
- [`spc:reporting-api-report-ingestion-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2008-reporting-api-report-ingestion-requirements.yaml) - Reporting API Report Ingestion Requirements
- [`spc:reporting-api-endpoint-group-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2009-reporting-api-endpoint-group-requirements.yaml) - Reporting API Endpoint Group Requirements
- [`spc:beacon-rum-delivery-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2010-beacon-rum-delivery-requirements.yaml) - Beacon RUM Delivery Requirements
- [`spc:beacon-payload-reliability-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2011-beacon-payload-reliability-requirements.yaml) - Beacon Payload Reliability Requirements
- [`spc:web-performance-rum-audit-evidence-requirements`](https://github.com/groupsum/web-performance-rum-governance-pack/blob/master/src/ssot_pack_web_performance_rum/templates/specs/SPEC-2012-web-performance-rum-audit-evidence-requirements.yaml) - Web Performance RUM Audit Evidence Requirements

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

- GitHub package repository: [groupsum/web-performance-rum-governance-pack](https://github.com/groupsum/web-performance-rum-governance-pack)
- PyPI package: [web-performance-rum-governance-pack](https://pypi.org/project/web-performance-rum-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative ownership boundary

Established canonical browser metric and Beacon ownership and added FCP, LCP, CLS, INP, long-task, and TBT contracts.
