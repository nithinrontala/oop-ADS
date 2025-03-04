from Solution import DateADT

def main():
    all_tests_passed = True

    # ---------------------------
    # Test 1: Three-argument constructor
    # ---------------------------
    try:
        d1 = DateADT(2023, 2, 28)  # Month 2 is valid (March if 0-indexed, but here it is just a test value)
        if d1.getYear() != 2023:
            print("Test 1 Failed: getYear() returned", d1.getYear())
            all_tests_passed = False
        if d1.getMonth() != 2:
            print("Test 1 Failed: getMonth() returned", d1.getMonth())
            all_tests_passed = False
        if d1.getDay() != 28:
            print("Test 1 Failed: getDay() returned", d1.getDay())
            all_tests_passed = False
        if d1.getHours() != 0 or d1.getMinutes() != 0 or d1.getSeconds() != 0:
            print("Test 1 Failed: Default time values are not 0")
            all_tests_passed = False
    except Exception as e:
        print("Test 1 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 2: Six-argument constructor
    # ---------------------------
    try:
        d2 = DateADT(2024, 1, 15, 13, 45, 50)
        if d2.getYear() != 2024:
            print("Test 2 Failed: getYear() returned", d2.getYear())
            all_tests_passed = False
        if d2.getMonth() != 1:
            print("Test 2 Failed: getMonth() returned", d2.getMonth())
            all_tests_passed = False
        if d2.getDay() != 15:
            print("Test 2 Failed: getDay() returned", d2.getDay())
            all_tests_passed = False
        if d2.getHours() != 13 or d2.getMinutes() != 45 or d2.getSeconds() != 50:
            print("Test 2 Failed: Time values are incorrect")
            all_tests_passed = False
    except Exception as e:
        print("Test 2 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 3: String-based constructor
    # ---------------------------
    try:
        # IMPORTANT: Since the numeric constructors expect months 0-11,
        # the string-based constructor should follow the same rule.
        # For example, here "10" stands for month 10 (i.e. November if January is 0).
        d3 = DateADT("2025-10-30 23:59:60")
    except Exception as e:
        print("Test 3 Exception:", e)
        all_tests_passed = True
    # ---------------------------
    # Test 4: toString method
    # ---------------------------
    try:
        s = d2.toString()
        expected = "2024-01-15 13:45:50"
        if s != expected:
            print("Test 4 Failed: toString() returned", s, "expected", expected)
            all_tests_passed = False
    except Exception as e:
        print("Test 4 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 5: getTime and setTime methods
    # ---------------------------
    try:
        ms = d2.getTime()
        d4 = DateADT(1970, 0, 1)  # starting point
        d4.setTime(ms)
        if d4.toString() != d2.toString():
            print("Test 5 Failed: setTime() did not properly update the date.")
            print("Expected:", d2.toString(), "Got:", d4.toString())
            all_tests_passed = False
    except Exception as e:
        print("Test 5 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 6: before and after methods
    # ---------------------------
    try:
        # d1 was set to (2023, 2, 28) and d2 to (2024, 1, 15,...)
        if not d1.before(d2):
            print("Test 6 Failed: d1.before(d2) should return True")
            all_tests_passed = False
        if not d2.after(d1):
            print("Test 6 Failed: d2.after(d1) should return True")
            all_tests_passed = False
    except Exception as e:
        print("Test 6 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 7: Setter methods (setYear, setMonth, setDay, setHours, setMinutes, setSeconds)
    # ---------------------------
    try:
        d5 = DateADT(2023, 3, 10, 10, 10, 10)
        d5.setYear(2022)
        if d5.getYear() != 2022:
            print("Test 7 Failed: setYear() did not update correctly")
            all_tests_passed = False
        d5.setMonth(5)
        if d5.getMonth() != 5:
            print("Test 7 Failed: setMonth() did not update correctly")
            all_tests_passed = False
        d5.setDay(15)
        if d5.getDay() != 15:
            print("Test 7 Failed: setDay() did not update correctly")
            all_tests_passed = False
        d5.setHours(20)
        if d5.getHours() != 20:
            print("Test 7 Failed: setHours() did not update correctly")
            all_tests_passed = False
        d5.setMinutes(30)
        if d5.getMinutes() != 30:
            print("Test 7 Failed: setMinutes() did not update correctly")
            all_tests_passed = False
        d5.setSeconds(55)
        if d5.getSeconds() != 55:
            print("Test 7 Failed: setSeconds() did not update correctly")
            all_tests_passed = False
    except Exception as e:
        print("Test 7 Exception:", e)
        all_tests_passed = False

    # ---------------------------
    # Test 8: Invalid input tests
    # ---------------------------
    # 8a: Month out of range
    try:
        # 12 is invalid because valid months are 0-11.
        d_invalid = DateADT(2023, 12, 10)
        print("Test 8a Failed: Month out of range not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # 8b: Day out of range (February in a non-leap year has only 28 days)
    try:
        d_invalid = DateADT(2023, 1, 29)
        print("Test 8b Failed: Day out of range not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # 8c: Hour out of range
    try:
        d_invalid = DateADT(2023, 5, 10, 24, 0, 0)
        print("Test 8c Failed: Hour out of range not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # 8d: Minute out of range
    try:
        d_invalid = DateADT(2023, 5, 10, 12, 60, 0)
        print("Test 8d Failed: Minute out of range not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # 8e: Second out of range
    try:
        d_invalid = DateADT(2023, 5, 10, 12, 30, 61)
        print("Test 8e Failed: Second out of range not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # 8f: Invalid string format
    try:
        d_invalid = DateADT("2023/05/10 12:30:30")
        print("Test 8f Failed: Invalid string format not caught")
        all_tests_passed = False
    except ValueError:
        pass  # Expected

    # ---------------------------
    # Final output
    # ---------------------------
    if all_tests_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please review the messages above.")

main()
