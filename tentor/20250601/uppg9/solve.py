import re
import sys


def get_email_addresses(registration_files, exam_files):
    all_registered = dict()
    test_takers = set()

    compile_mail = lambda x: f"{x}@student.litu.se"

    for reg_file in registration_files:
        with open(reg_file, "r") as f:
            for i, row in enumerate(f.read().splitlines()):
                if i % 7 != 0:
                    continue

                first_name, last_name, liu_id = row.split(" ")
                all_registered[f"{first_name} {last_name}".lower()] = liu_id[1:-1]
                if reg_file.endswith("VT25.txt"):
                    test_takers.add(compile_mail(liu_id[1:-1]))

    a = re.compile("(?P<first_name>\w+), (?P<last_name>\w+)")
    for exam_file in exam_files:
        with open(exam_file, "r") as f:
            for row in f.read().splitlines():
                last_name, first_name = a.findall(row)[0]
                s = f"{first_name} {last_name}".lower()
                if s in all_registered:
                    test_takers.add(compile_mail(all_registered[s]))

    return "\n".join(sorted(test_takers))


if __name__ == "__main__":
    registration_files = sys.argv[1:-1]
    exam_files = sys.argv[-1]
    answer = get_email_addresses(registration_files, [exam_files])

    with open("answer.txt") as f:
        print(answer)
        assert answer == f.read()
