from pathlib import Path


with (Path(__file__).parent / "data" / "06.txt").open() as fin:
    answers_count = 0
    for group_answers in fin.read().split("\n\n"):
        group_answers = map(set, group_answers.split())
        common_answers = next(group_answers)
        for answers in group_answers:
            common_answers = common_answers.intersection(answers)
        answers_count += len(common_answers)

print(f"answers_count: {answers_count}")
