import random


def main():
    print("--- GCSE Maths Worksheet Generator ---")
    print("1. Quadratics")
    print("2. Linear Equations")
    print("3. Pythagoras")
    print("4. Mixed")

    # keep asking until the user picks a valid option
    while True:
        choice = input("Pick a topic (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            break
        print("Please enter 1, 2, 3, or 4.")

    while True:
        try:
            num_questions = int(input("How many questions? "))
            if 1 <= num_questions <= 50:
                break
            print("Enter a number between 1 and 50.")
        except ValueError:
            print("That's not a valid number.")

    questions = []
    answers = []

    for _ in range(num_questions):
        if choice == "1":
            q, a = make_quadratic()
        elif choice == "2":
            q, a = make_linear()
        elif choice == "3":
            q, a = make_pythagoras()
        else:
            # pick a random topic for mixed worksheets
            topic = random.choice(["1", "2", "3"])
            if topic == "1":
                q, a = make_quadratic()
            elif topic == "2":
                q, a = make_linear()
            else:
                q, a = make_pythagoras()

        questions.append(q)
        answers.append(a)

    save_to_files(choice, questions, answers)
    print(f"\nDone! Saved {num_questions} questions to worksheet.md and answers.md")


def make_quadratic():
    # pick two non-zero roots first so the quadratic always factorises nicely
    r1 = 0
    while r1 == 0:
        r1 = random.randint(-9, 9)

    r2 = 0
    while r2 == 0:
        r2 = random.randint(-9, 9)

    # expand (x - r1)(x - r2) = x^2 - (r1 + r2)x + r1*r2
    b = -(r1 + r2)
    c = r1 * r2

    # build the equation string cleanly so we don't get "+ -3x" or "1x"
    eq = "x^2"
    if b > 0:
        eq += f" + {b}x" if b != 1 else " + x"
    elif b < 0:
        eq += f" - {abs(b)}x" if b != -1 else " - x"

    if c > 0:
        eq += f" + {c}"
    elif c < 0:
        eq += f" - {abs(c)}"

    question = f"Solve: {eq} = 0"

    # format brackets for the answer key
    b1 = f"(x - {r1})" if r1 > 0 else f"(x + {abs(r1)})"
    b2 = f"(x - {r2})" if r2 > 0 else f"(x + {abs(r2)})"

    if r1 == r2:
        ans = f"Factorise: {b1}^2 = 0  ->  x = {r1}"
    else:
        ans = f"Factorise: {b1}{b2} = 0  ->  x = {r1} or x = {r2}"

    return question, ans


def make_linear():
    # pick x first so the solution is always a whole number
    x = random.randint(-10, 10)
    a = random.randint(3, 9)
    c = random.randint(1, a - 1)  # keep a > c so the x term stays positive

    b = 0
    while b == 0:
        b = random.randint(-12, 12)

    # solve for d in ax + b = cx + d
    d = a * x + b - c * x

    b_part = f"+ {b}" if b > 0 else f"- {abs(b)}"
    d_part = f"+ {d}" if d > 0 else f"- {abs(d)}"
    if d == 0:
        d_part = ""

    lhs = f"{a}x {b_part}"
    rhs = f"{c}x {d_part}".strip()

    question = f"Solve for x: {lhs} = {rhs}"
    ans = f"{a - c}x = {d - b}  ->  x = {x}"

    return question, ans


def make_pythagoras():
    # scale up standard pythagorean triples so answers are exact integers
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
    a, b, c = random.choice(triples)
    scale = random.randint(1, 4)
    a, b, c = a * scale, b * scale, c * scale

    # randomly ask for either the hypotenuse or a shorter side
    if random.randint(0, 1) == 0:
        q = f"A right-angled triangle has shorter sides of {a} cm and {b} cm. Find the hypotenuse."
        ans = f"sqrt({a}^2 + {b}^2) = sqrt({a**2 + b**2}) = {c} cm"
    else:
        q = f"A right-angled triangle has a hypotenuse of {c} cm and one side of {b} cm. Find the missing side."
        ans = f"sqrt({c}^2 - {b}^2) = sqrt({c**2 - b**2}) = {a} cm"

    return q, ans


def save_to_files(choice, questions, answers):
    topic_names = {
        "1": "Quadratics",
        "2": "Linear Equations",
        "3": "Pythagoras' Theorem",
        "4": "Mixed Revision",
    }
    title = topic_names[choice]

    with open("worksheet.md", "w") as f:
        f.write(f"# GCSE Maths Worksheet - {title}\n\n")
        for i in range(len(questions)):
            f.write(f"**{i + 1}.** {questions[i]}\n\n")

    with open("answers.md", "w") as f:
        f.write(f"# Answer Key - {title}\n\n")
        for i in range(len(answers)):
            f.write(f"**{i + 1}.** {questions[i]}\n")
            f.write(f"Answer: {answers[i]}\n\n")


if __name__ == "__main__":
    main()