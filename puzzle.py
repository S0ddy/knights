from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # describe context. Each character is either a knight or a knave
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # A says "I am both a knight and a knave."
    Implication(And(AKnight, AKnave), AKnight),  # if it says true then AKnight
    Implication(Not(And(AKnight, AKnave)), AKnave),  # if it says lie then AKnave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # describe context. Each character is either a knight or a knave
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # A says "We are both knaves."
    Implication(And(AKnave, BKnave), AKnight),  # if it says true then AKnight
    Implication(Not(And(AKnave, BKnave)), AKnave),  # if it says lie then AKnave
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # describe context. Each character is either a knight or a knave
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # A says "We are the same kind."
    Implication(Or(And(AKnave, BKnave), And(AKnight, BKnight)),
                AKnight),  # if it says true then AKnight
    Implication(Not(Or(And(AKnave, BKnave), And(AKnight, BKnight))),
                AKnave),  # if it says lie then AKnave

    # B says "We are of different kinds."
    Implication(Or(And(AKnave, BKnight), And(AKnight, BKnave)),
                BKnight),  # if it says true then BKnight
    Implication(Not(Or(And(AKnave, BKnight), And(AKnight, BKnave))),
                BKnave),  # if it says lie then BKnave

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # describe context. Each character is either a knight or a knave
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(Or(AKnight, AKnave), AKnight),
    Implication(Not(Or(AKnight, AKnave)), AKnave),

    # B says "A said 'I am a knave'."
    Implication(AKnave, BKnight),
    Implication(Not(AKnave), BKnave),

    # B says "C is a knave."
    Implication(CKnave, BKnight),
    Implication(Not(CKnave), BKnave),

    # C says "A is a knight."
    Implication(AKnight, CKnight),
    Implication(Not(AKnight), CKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
