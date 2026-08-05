"""
generate_and_push.py

Picks 3-4 unused problems from problems_bank.py, writes them as new
Qn.py files (continuing the numbering already used in the repo),
then commits and pushes to GitHub.

State (which problems have already been used) is tracked in
.practice_state.json so you don't get the same problem twice until
the whole bank has been used up.

Run this via run_practice.bat (Windows) or run_practice.sh (bash),
or directly with: python generate_and_push.py
"""

import os
import re
import json
import random
import datetime
import subprocess
import sys

from problems_bank import PROBLEMS

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(REPO_DIR, ".practice_state.json")


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"solved": []}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def next_q_number():
    nums = []
    for fname in os.listdir(REPO_DIR):
        m = re.match(r"^Q(\d+)\.py$", fname)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def pick_problems(state, n):
    unused = [p for p in PROBLEMS if p["id"] not in state["solved"]]
    if len(unused) < n:
        # Whole bank used up (or close to it) -> reset the pool so it
        # keeps working indefinitely, just avoid repeating the very
        # last batch immediately.
        recently_used = set(state["solved"][-n:]) if state["solved"] else set()
        unused = [p for p in PROBLEMS if p["id"] not in recently_used] or PROBLEMS[:]
        state["solved"] = []
    random.shuffle(unused)
    return unused[:n]


def write_problem_file(q_num, problem):
    path = os.path.join(REPO_DIR, f"Q{q_num}.py")
    header = (
        f'"""\n'
        f'Problem {q_num}: {problem["title"]}\n'
        f'Difficulty: {problem["difficulty"]}\n\n'
        f'{problem["description"]}\n'
        f'"""\n\n'
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(header + problem["code"].strip() + "\n")
    return path


def run_git(*args):
    result = subprocess.run(
        ["git"] + list(args),
        cwd=REPO_DIR,
        capture_output=True,
        text=True,
    )
    return result


def get_current_branch():
    result = run_git("rev-parse", "--abbrev-ref", "HEAD")
    branch = result.stdout.strip()
    return branch if branch and result.returncode == 0 else "main"


def main():
    if not os.path.isdir(os.path.join(REPO_DIR, ".git")):
        print("ERROR: This script must live inside the cloned git repo")
        print(f"       (no .git folder found in {REPO_DIR}).")
        sys.exit(1)

    state = load_state()
    n = random.choice([3, 4])
    chosen = pick_problems(state, n)

    q_start = next_q_number()
    created_files = []
    for i, problem in enumerate(chosen):
        q_num = q_start + i
        path = write_problem_file(q_num, problem)
        created_files.append(os.path.basename(path))
        state["solved"].append(problem["id"])

    save_state(state)

    branch = get_current_branch()
    print(f"Repo:   {REPO_DIR}")
    print(f"Branch: {branch}")
    print(f"Adding: {', '.join(created_files)}\n")

    pull = run_git("pull", "origin", branch)
    if pull.returncode != 0:
        print("Warning: git pull failed (continuing anyway):")
        print(pull.stderr)

    run_git("add", "-A")

    date_str = datetime.date.today().isoformat()
    commit_msg = f"Daily practice ({date_str}): " + ", ".join(created_files)
    commit = run_git("commit", "-m", commit_msg)
    if commit.returncode != 0:
        print("Nothing to commit or commit failed:")
        print(commit.stdout, commit.stderr)
        sys.exit(1)

    push = run_git("push", "origin", branch)
    if push.returncode != 0:
        print("ERROR: git push failed:")
        print(push.stderr)
        sys.exit(1)

    print("\nDone! Pushed:")
    for f in created_files:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
