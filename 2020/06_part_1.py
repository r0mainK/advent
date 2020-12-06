from pathlib import Path


with (Path(__file__).parent / "data" / "06.txt").open() as fin:
    answers_count = 0
    for group_answers in fin.read().split("\n\n"):
        answers_count += len(set(group_answers.replace("\n", "")))

print(f"answers_count: {answers_count}")
