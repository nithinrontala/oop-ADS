import os
from Solution import Person, Grade, Student, GradeBook

# Test harness with 30 test cases.
def main():
    print("=== TEST CASES FOR GRADEBOOK PROJECT ===")
    test_count = 1

    # Test 1: Create a sample data file "S18grades.txt"
    sample_data = (
        "John Doe USA 20 CS jd123 HW1 85 Q1 90 MT 88 F 92\n"
        "Jane Smith Canada 21 EE js456 HW1 95 Q1 87 MT 90 F 93\n"
        "Alice Brown UK 22 ME ab789 HW1 75 Q1 80 MT 70 F 85"
    )
    filename = "S18grades.txt"
    with open(filename, "w") as f:
        f.write(sample_data)

    # Test 2: Create GradeBook from file
    gb = GradeBook(filename)
    print(f"\nTest {test_count}: GradeBook creation from file.")
    # print(gb)
    test_count += 1
    if "jd123" in str(gb) and "js456" in str(gb) and "ab789" in str(gb):
        print("PASS: GradeBook created with 3 students.")
    else:
        print("FAIL: GradeBook creation issue.")

    # Test 3: __str__ method output
    print(f"\nTest {test_count}: GradeBook.__str__() output:")
    test_count += 1
    print(str(gb))

    # Test 4: print_individual_grades() for valid id "jd123"
    print(f"\nTest {test_count}: print_individual_grades() for jd123")
    test_count += 1
    gb.print_individual_grades("jd123")

    # Test 5: print_individual_grades() for invalid id "xx000"
    print(f"\nTest {test_count}: print_individual_grades() for invalid id xx000")
    test_count += 1
    gb.print_individual_grades("xx000")

    # Test 6: print_grades_by_major() for valid major "CS"
    print(f"\nTest {test_count}: print_grades_by_major() for major CS")
    test_count += 1
    gb.print_grades_by_major("CS")

    # Test 7: print_grades_by_major() for invalid major "Bio"
    print(f"\nTest {test_count}: print_grades_by_major() for major Bio")
    test_count += 1
    gb.print_grades_by_major("Bio")

    # Test 8: remove_student() for valid id "js456"
    print(f"\nTest {test_count}: remove_student() for js456")
    test_count += 1
    gb.remove_student("js456")
    if "js456" not in str(gb):
        print("PASS: js456 removed.")
    else:
        print("FAIL: js456 still exists.")

    # Test 9: remove_student() for invalid id "xx999"
    print(f"\nTest {test_count}: remove_student() for invalid id xx999")
    test_count += 1
    gb.remove_student("xx999")

    # Test 10: change_grade() for valid id "jd123", HW1 to 90
    print(f"\nTest {test_count}: change_grade() for jd123, HW1 to 90")
    test_count += 1
    gb.change_grade("jd123", "HW1", 90)
    print("Verifying jd123 grades:")
    gb.print_individual_grades("jd123")

    # Test 11: change_grade() for valid id but invalid assignment "Quiz2"
    print(f"\nTest {test_count}: change_grade() for jd123, Quiz2 (invalid assignment)")
    test_count += 1
    gb.change_grade("jd123", "Quiz2", 85)

    # Test 12: change_grade() for invalid id "xx111"
    print(f"\nTest {test_count}: change_grade() for invalid id xx111")
    test_count += 1
    gb.change_grade("xx111", "HW1", 100)

    # Test 13: print_current_grade() for valid id "jd123"
    print(f"\nTest {test_count}: print_current_grade() for jd123")
    test_count += 1
    gb.print_current_grade("jd123")

    # Test 14: print_current_grade() for invalid id "xx222"
    print(f"\nTest {test_count}: print_current_grade() for invalid id xx222")
    test_count += 1
    gb.print_current_grade("xx222")

    # Test 15: what_do_i_need() for valid id "jd123" for target grade A
    print(f"\nTest {test_count}: what_do_i_need() for jd123 for target grade A")
    test_count += 1
    need_val = gb.what_do_i_need("jd123", 'A')

    # Test 16: what_do_i_need() for invalid id "xx333"
    print(f"\nTest {test_count}: what_do_i_need() for invalid id xx333")
    test_count += 1
    gb.what_do_i_need("xx333", 'B')

    # Test 17: add_grade_to_all() – interactive test skipped (uncomment to test interactively)
    # gb.add_grade_to_all()

    # Test 18: update_database() writes current gradebook to new file "updatedGrades.txt"
    print(f"\nTest {test_count}: update_database() to updatedGrades.txt")
    test_count += 1
    gb.update_database("updatedGrades.txt")

    # Test 19: Create a new Student Bob and add multiple grades manually
    print(f"\nTest {test_count}: Manual Student grade additions for Bob")
    test_count += 1
    sTest = Student("Bob", "Marley", "Jamaica", 23, "Music", "bm001")
    sTest.add_grade(Grade("HW2", 88))
    sTest.add_grade(Grade("Q2", 92))
    sTest.add_grade(Grade("MT", 85))
    sTest.add_grade(Grade("F", 90))
    if sTest.get_current_score() > 0:
        print(f"PASS: Bob's current score: {sTest.get_current_score()}")
    else:
        print("FAIL: Bob's grade calculation.")

    # Test 20: Check letter grade boundaries for Bob
    print(f"\nTest {test_count}: Check letter grade boundary for Bob")
    test_count += 1
    letter = sTest.get_current_letter_grade()
    if letter in ['A', 'B', 'C']:
        print(f"Bob's letter grade is: {letter}")
    else:
        print(f"Unexpected letter grade: {letter}")

    # Test 21: what_do_i_need() for Bob for target grade A
    print(f"\nTest {test_count}: what_do_i_need() for Bob for target grade A")
    test_count += 1
    bob_need = sTest.what_do_i_need('A')
    if bob_need != -1:
        print(f"Bob needs an average of {bob_need:.2f} on remaining work.")

    # Test 22: Add Bob to GradeBook and then print individual grades.
    print(f"\nTest {test_count}: Add Bob (bm001) to GradeBook and print grades.")
    test_count += 1
    gb.students.append(sTest)
    gb.print_individual_grades("bm001")

    # Test 23: Remove Bob from GradeBook.
    print(f"\nTest {test_count}: Remove Bob (bm001) from GradeBook.")
    test_count += 1
    gb.remove_student("bm001")
    if all("bm001" not in str(student) for student in gb.students):
        print("PASS: Bob removed.")
    else:
        print("FAIL: Bob still exists.")

    # Test 24: Try to change grade for Alice (ab789) with non-existent assignment "HW3"
    print(f"\nTest {test_count}: change_grade() for Alice (ab789) with non-existent assignment HW3")
    test_count += 1
    gb.change_grade("ab789", "HW3", 100)

    # Test 25: Check current grade for Alice (ab789)
    print(f"\nTest {test_count}: print_current_grade() for ab789")
    test_count += 1
    gb.print_current_grade("ab789")

    # Test 26: Add a new grade for Alice and check update.
    print(f"\nTest {test_count}: Add new grade HW2 for Alice (ab789) and verify.")
    test_count += 1
    for student in gb.students:
        if student.andrew_id.lower() == "ab789":
            student.add_grade(Grade("HW2", 82))
            break
    gb.print_individual_grades("ab789")

    # Test 27: what_do_i_need() for a student with full weight (simulate for jd123)
    print(f"\nTest {test_count}: what_do_i_need() for student with full weight (simulate for jd123)")
    test_count += 1
    for student in gb.students:
        if student.andrew_id.lower() == "jd123":
            student.add_grade(Grade("Extra", 100))  # This grade gets 0.0 weight if not recognized.
            break
    gb.what_do_i_need("jd123", 'A')

    # Test 28: Verify change_grade() changes the correct assignment for jd123 (change HW1 to 95)
    print(f"\nTest {test_count}: Verify change_grade() for jd123 changes HW1 to 95")
    test_count += 1
    gb.change_grade("jd123", "HW1", 95)
    gb.print_individual_grades("jd123")

    # Test 29: Create student with perfect scores to yield A.
    print(f"\nTest {test_count}: Create student with perfect scores to yield A")
    test_count += 1
    perfect = Student("Perfect", "Score", "Nowhere", 20, "Math", "ps100")
    perfect.add_grade(Grade("HW1", 90))
    perfect.add_grade(Grade("MT", 90))
    perfect.add_grade(Grade("F", 90))
    if perfect.get_current_letter_grade() == 'A':
        print("PASS: Perfect student letter grade is A.")
    else:
        print(f"FAIL: Perfect student letter grade is {perfect.get_current_letter_grade()}.")

    # Test 30: Add Perfect student to GradeBook, update database, and re-read file to verify.
    print(f"\nTest {test_count}: Add Perfect student to GradeBook and update database.")
    test_count += 1
    gb.students.append(perfect)
    gb.update_database("updatedGrades2.txt")
    print(f"\nTest {test_count}: Re-read updated database file to verify content.")
    test_count += 1
    gb3 = GradeBook("updatedGrades2.txt")
    if "ps100" in str(gb3):
        print("PASS: Updated database contains Perfect student.")
    else:
        print("FAIL: Updated database does not contain Perfect student.")

    print("\n=== End of Tests ===")


if __name__ == "__main__":
    main()
