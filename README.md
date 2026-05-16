<div align="center">

<h1>ssot-registry-pack-template</h1>

<p>
  <a href="https://pypi.org/project/ssot-registry-pack-template/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/ssot-registry-pack-template.svg"></a>
  <a href="https://pepy.tech/projects/ssot-registry-pack-template"><img alt="Downloads" src="https://static.pepy.tech/badge/ssot-registry-pack-template"></a>
  <a href="https://hits.sh/github.com/groupsum/ssot-registry-pack-template/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/ssot-registry-pack-template.svg"></a>
  <a href="https://pypi.org/project/ssot-registry-pack-template/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/ssot-registry-pack-template.svg"></a>
  <a href="https://github.com/groupsum/ssot-registry-pack-template/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/ssot-registry-pack-template.svg"></a>
  <a href="https://github.com/groupsum/ssot-registry-pack-template/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/ssot-registry-pack-template/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/ssot-registry-pack-template"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fssot--registry--pack--template-181717?logo=github"></a>
</p>

</div>

`ssot-registry-pack-template` is a starter repository for creating installable SSOT Registry governance packs.

Use it when a governance domain needs reusable Architecture Decision Records (ADRs), Specifications (SPECs), manifests, tests, and packaging metadata that can be installed beside [`ssot-registry`](https://pypi.org/project/ssot-registry/) and synchronized into downstream repositories.

The template intentionally ships with no ADR or SPEC documents. Derived packs should add their own governed rows after the domain boundary is reviewed.

## Template Scope

This template provides:

- a Python package that can expose packaged ADR and SPEC documents
- manifest loaders for pack-aware SSOT Registry workflows
- empty ADR and SPEC manifests as the starting state
- tests that verify the empty template manifests stay loadable
- a manifest sync script that derives package manifests from the packaged document resources
- CI and publish workflow scaffolding suitable for a new governance-pack repository

## Create A Pack From This Template

Create a new private repository from this template, then replace the template values:

```bash
gh repo create groupsum/example-governance-pack --private --template groupsum/ssot-registry-pack-template --clone
```

Update these values before the first release:

- package name in `pyproject.toml`
- public package badges and links in `README.md`
- `src/<package_name>/metadata.json` pack metadata
- `src/<package_name>/__init__.py` contract binding via `ssot_pack_contracts.bind_pack_contract`
- import package directory under `src/`
- package-data keys in `pyproject.toml`
- package origin values once ADR and SPEC YAML resources exist
- manifest rows under `src/<package_name>/templates/**/manifest.json` after adding governance documents
- README domain language, included ADR/SPEC lists, install commands, CLI examples, PyPI link, and resources after the pack has governed rows
- test import paths and expected document IDs

## Included ADRs And SPECs

None. This repository is a template and does not ship governed ADR or SPEC rows.

## Authoring Flow

1. Author ADR YAML resources in `src/<package_name>/templates/adr`.
2. Author SPEC YAML resources in `src/<package_name>/templates/specs`.
3. Run `python scripts/sync_packaged_docs.py` after setting the package paths for the new pack.
4. Run tests to verify manifests and packaged documents.
5. Publish the pack only after the ADR/SPEC surface is intentionally scoped.

## Required Public README Elements

Concrete packs derived from this template should keep a consistent public README shape:

- badge rows for PyPI version, downloads, hits, Python versions, license, CI, and GitHub repository
- a concise opening description naming the domain and the pack's governance scope
- a clear audience statement explaining who uses the pack
- `What Is An SSOT Registry Pack?`
- `Why This Pack Exists`
- `Domain Focus`
- `Included ADRs`
- `Included SPECs`
- a standards, proposal, or target-review section when the pack is still in review
- `Install With uv`
- `Install With The SSOT Registry Pack CLI`
- `Use With The SSOT Registry CLI`
- `Programmatic Usage`
- `Resources` with GitHub repository, PyPI package, and SSOT Registry links

The supported Python surface should stay aligned across `pyproject.toml`, `uv.lock`, README badges, and `.github/workflows/ci.yml`. Current packs test Python 3.10, 3.11, 3.12, 3.13, and 3.14.

## Required Pack Contract Elements

Concrete packs must expose the shared `ssot-pack-contracts` API:

- depend on `ssot-pack-contracts>=0.2.17,<0.3.0`
- ship `metadata.json` as package data at the import package root
- bind top-level package exports with `ssot_pack_contracts.bind_pack_contract(__name__)`
- declare `metadata.schema_version`, `metadata.ssot_package_name`, `metadata.origin`, `metadata.compatibility`, `metadata.trust`, and `metadata.documents`
- declare document manifests through normalized `adr` and `spec` keys
- set manifest `origin` to `extension-pack`
- set manifest `reservation_owner` to `extension-pack:<pypi-package-name>`
- set manifest `minimum_schema_version` to the compatible SSOT registry schema, currently `0.4.0`
- include lowercase SHA-256 hashes for every packaged document resource

## Install With uv

Install the pack into a project environment:

```bash
uv add ssot-registry-pack-template
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry ssot-registry-pack-template
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with ssot-registry-pack-template ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can install and synchronize packs through the pack command surface:

```bash
uvx --from ssot-registry ssot pack install ssot-registry-pack-template
uvx --from ssot-registry ssot pack sync . ssot-registry-pack-template
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, synchronize ADRs and SPECs into a target repository:

```bash
uv run ssot adr sync .
uv run ssot spec sync .
```

Review the synchronized governance surface:

```bash
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_registry_pack_template import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest)
print(spec_manifest)
```

## Resources

- GitHub repository: [groupsum/ssot-registry-pack-template](https://github.com/groupsum/ssot-registry-pack-template)
- PyPI package: [ssot-registry-pack-template](https://pypi.org/project/ssot-registry-pack-template/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
