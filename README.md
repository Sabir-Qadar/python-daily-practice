# Daily Practice Auto-Push Tool

Generates 3-4 new basic-to-moderate Python solutions and pushes them to
your `python-daily-practice` GitHub repo. One click and it's done.

## Files

- `problems_bank.py` – 30+ ready-made problems (title, difficulty, description, solution). Add more anytime.
- `generate_and_push.py` – picks unused problems, writes them as `Qn.py` (continuing your existing numbering), commits, and pushes.
- `run_practice.bat` – **Windows**: double-click this to run everything.
- `run_practice.sh` – **bash** (Git Bash / WSL / Linux / Mac): run with `bash run_practice.sh`, or double-click if your file manager is set to run `.sh` files.
- `.practice_state.json` – auto-created; tracks which problems have already been used so you don't get repeats until the whole bank cycles through.

## One-time setup

1. Clone your repo locally if you haven't already:
   ```
   git clone https://github.com/Sabir-Qadar/python-daily-practice.git
   ```
2. Copy `problems_bank.py`, `generate_and_push.py`, `run_practice.bat`, and `run_practice.sh` **into that cloned repo folder** (same place as your `push.bat`).
3. Make sure `git push` already works from that folder without prompting for a password every time — i.e. you're using SSH keys, or Windows Git Credential Manager has your GitHub login cached. If `push.bat` already works, you're set.
4. Make sure `python` (or `python3`) is on your PATH. Test with `python --version` in a terminal.

## Daily use

- **Windows:** double-click `run_practice.bat`.
- **Bash:** run `bash run_practice.sh`.

Each run:
1. Picks 3 or 4 problems you haven't solved yet in this repo.
2. Writes them as new files (`Q38.py`, `Q39.py`, ... continuing from your highest existing `Qn.py`).
3. Pulls the latest repo state, commits with a message like `Daily practice (2026-08-05): Q38.py, Q39.py, Q40.py`, and pushes.

## Customizing

- To change how many problems get added per run, edit this line in `generate_and_push.py`:
  ```python
  n = random.choice([3, 4])
  ```
- To add your own problems, open `problems_bank.py` and append a new dict to the `PROBLEMS` list following the same format (`id`, `title`, `difficulty`, `description`, `code`).

## Note

This is meant to help you actually practice and build a genuine commit
history — the solutions are real, runnable code, not placeholders. If a
problem's difficulty doesn't match your current pace, adjust the bank or
just delete/rewrite a generated file before your next run.
