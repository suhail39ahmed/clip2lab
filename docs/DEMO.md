# Demo — clip2lab

Loom / screen recording script (**60–90 seconds**). Speak calmly; show the terminal, not slides.

## Setup (before record)

```bash
cd clip2lab
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font size ~16–18pt; dark theme
```

## Exact click / type script

1. Open terminal at repo root. Say: *"This is clip2lab — Turn a reel/short transcript into a lab pack: README, quiz, and skill stub — det…"*
2. Type `make demo` **or** walk the commands below one by one.
1. Run `python -m clip2lab --help` — wait for JSON / output.
2. Run `python -m clip2lab examples/one-reel/transcript.txt -o labs` — wait for JSON / output.
3. Run `ls labs/one-reel/` — wait for JSON / output.
3. Scroll the JSON briefly. Call out one concrete field (citation path, `human_approval_required`, findings, report path, etc.).
4. Close with: *"Offline fixtures only — clone it, `make demo`, adopt the pattern."* Link the GitHub repo in the Loom description.

## Talking points (pick 2)

- Who it's for: SAs and educators packaging short-form teaching into reusable labs.
- What it is NOT: Not an automatic video transcription service
- Honest MVP: no fabricated production metrics

## Outro card (last 3s)

`github.com/suhail39ahmed/clip2lab`
