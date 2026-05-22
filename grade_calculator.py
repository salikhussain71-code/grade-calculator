def main():
    print("=== Smart Grade Calculator ===")

    score = int(input("Enter your score: "))

    if score >= 90:
        print("Grade: A")
        print("Out standing!")

    elif score >= 80:
        print("Grade: B")
        print("Excellent!")

    elif score >= 70:
        print("Grade: C")
        print("Very good!")

    elif score >= 60:
        print("Grade: D")
        print("You passed.")

    else:
        print("Grade: F")
        print("You failed. Keep practicing.")

if __name__ == "__main__":
    main()