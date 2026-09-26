# clip2lab

CLI: `transcript.txt` → lab folder with **README**, **quiz.md**, and **skill stub**. Includes `examples/one-reel/`.

## What it is
- Content→enablement pack generator for teaching reels / shorts
- Offline, deterministic templates (no LLM required for MVP)

## What it is not
- Not an automatic video transcription service
- Not a full LMS

## Architecture

```
  transcript.txt --> clip2lab --> labs/<slug>/
                                   README.md
                                   quiz.md
                                   SKILL.md
                                   source/transcript.txt
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m clip2lab.cli examples/one-reel/transcript.txt -o labs
ls labs/one-reel/
```

## Demo assets checklist
- [ ] `assets/demo.gif`
- [ ] `assets/architecture.png`
- [ ] `docs/DEMO.md`

## License
MIT
