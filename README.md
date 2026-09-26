# clip2lab

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-0.1.0%20MVP-green.svg)

**Turn a reel/short transcript into a lab pack: README, quiz, and skill stub — deterministic, offline, zero LLM required.**

> Who it's for: SAs and educators packaging short-form teaching into reusable labs.

## Why this exists

Teaching content dies in the scroll. `clip2lab` converts `transcript.txt` into a folder agents and humans can both use — lab README, quiz.md, and a skill stub — so enablement scales without a full LMS.

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

Or with pipx (once published to PyPI): `pipx install clip2lab` — until then use editable install from this repo.

## 30-second demo

```bash
python -m clip2lab --help
python -m clip2lab examples/one-reel/transcript.txt -o labs
ls labs/one-reel/
```

Or simply:

```bash
make demo
```

## What it is NOT

- Not an automatic video transcription service
- Not a full LMS or course platform
- Not LLM-dependent for the MVP path

## Architecture

![Architecture](assets/architecture.svg)

## Roadmap

- [ ] Optional LLM polish pass for quiz quality
- [ ] Batch mode over a transcripts/ directory
- [ ] Export to kc-mcp sample_corpus format

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Be kind — [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md). Security reports: [SECURITY.md](./SECURITY.md).

## License

MIT
