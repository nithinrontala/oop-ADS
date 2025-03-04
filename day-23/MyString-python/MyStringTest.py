

from Solution import MyString
# ---------------------------
# Main method with test cases
# ---------------------------
def main():
    print("----- Testing MyString Methods -----")
    
    # Test 1: Empty constructor, __str__(), and length()
    try:
        empty = MyString()
        if empty.length() == 0 and str(empty) == "":
            print("Test 1 Passed: Empty constructor")
        else:
            print("Test 1 Failed: Empty constructor")
    except Exception as e:
        print("Test 1 Exception:", e)

    # Test 2: List constructor
    try:
        hello_chars = ['H', 'e', 'l', 'l', 'o']
        hello = MyString(hello_chars)
        # print(12345,hello)
        if hello.length() == 5 and str(hello) == "Hello":
            print("Test 2 Passed: List constructor")
        else:
            print("Test 2 Failed: List constructor")
    except Exception as e:
        print("Test 2 Exception:", e)

    # Test 3: Copy constructor
    try:
        copy_hello = MyString(hello)
        # print(78787878,hello)
        if str(copy_hello) == "Hello":
            print("Test 3 Passed: Copy constructor")
        else:
            print("Test 3 Failed: Copy constructor")
    except Exception as e:
        print("Test 3 Exception:", e)

    # Test 4: char_at()
    try:
        if hello.char_at(0) == 'H' and hello.char_at(4) == 'o':
            print("Test 4 Passed: char_at()")
        else:
            print("Test 4 Failed: char_at()")
    except Exception as e:
        print("Test 4 Exception:", e)

    # Test 5: substring(begin_index, end_index)
    try:
        sub = hello.substring(1, 4)  # expected "ell"
        if str(sub) == "ell":
            print("Test 5 Passed: substring(1,4)")
        else:
            print("Test 5 Failed: substring(1,4)")
    except Exception as e:
        print("Test 5 Exception:", e)

    # Test 6: substring(begin_index)
    try:
        sub2 = hello.substring(2)  # expected "llo"
        if str(sub2) == "llo":
            print("Test 6 Passed: substring(2)")
        else:
            print("Test 6 Failed: substring(2)")
    except Exception as e:
        print("Test 6 Exception:", e)

    # Test 7: compare_to()
    try:
        a = MyString(list("abc"))
        b = MyString(list("abd"))
        cmp_result = a.compare_to(b)
        if cmp_result < 0:
            print("Test 7 Passed: compare_to()")
        else:
            print("Test 7 Failed: compare_to()")
    except Exception as e:
        print("Test 7 Exception:", e)

    # Test 8: compare_to_ignore_case()
    try:
        s1 = MyString(list("Hello"))
        s2 = MyString(list("hello"))
        if s1.compare_to_ignore_case(s2) == 0:
            print("Test 8 Passed: compare_to_ignore_case()")
        else:
            print("Test 8 Failed: compare_to_ignore_case()")
    except Exception as e:
        print("Test 8 Exception:", e)

    # Test 9: equals_ignore_case()
    try:
        if hello.equals_ignore_case(MyString(list("hello"))):
            print("Test 9 Passed: equals_ignore_case()")
        else:
            print("Test 9 Failed: equals_ignore_case()")
    except Exception as e:
        print("Test 9 Exception:", e)

    # Test 10: concat()
    try:
        world = MyString(list("World"))
        concatenated = hello.concat(world)  # expected "HelloWorld"
        if str(concatenated) == "HelloWorld":
            print("Test 10 Passed: concat()")
        else:
            print("Test 10 Failed: concat()")
    except Exception as e:
        print("Test 10 Exception:", e)

    # Test 11: replace(char, char)
    try:
        replaced = hello.replace('l', 'x')  # expected "Hexxo"
        if str(replaced) == "Hexxo":
            print("Test 11 Passed: replace(char, char)")
        else:
            print("Test 11 Failed: replace(char, char)")
    except Exception as e:
        print("Test 11 Exception:", e)

    # Test 12: replace_seq (replace substring)
    try:
        replaced2 = hello.replace_seq(MyString(list("ell")), MyString(list("ipp")))  # expected "Hippo"
        if str(replaced2) == "Hippo":
            print("Test 12 Passed: replace_seq()")
        else:
            print("Test 12 Failed: replace_seq()")
    except Exception as e:
        print("Test 12 Exception:", e)

    # Test 13: replace_all()
    try:
        digits_test = MyString(list("a1b2c3"))
        replaced_all = digits_test.replace_all(r"\d", MyString([]))  # expected behavior: remove digits -> "abc"
        if str(replaced_all) == "abc":
            print("Test 13 Passed: replace_all()")
        else:
            print("Test 13 Failed: replace_all()")
    except NotImplementedError as nie:
        print("Test 13 NotImplementedError:", nie)
    except Exception as e:
        print("Test 13 Exception:", e)

    # Test 14: replace_first()
    try:
        digits_test2 = MyString(list("a1b2c3"))
        replaced_first = digits_test2.replace_first(r"\d", MyString([]))  # expected: remove first digit -> "ab2c3"
        if str(replaced_first) == "ab2c3":
            print("Test 14 Passed: replace_first()")
        else:
            print("Test 14 Failed: replace_first()")
    except NotImplementedError as nie:
        print("Test 14 NotImplementedError:", nie)
    except Exception as e:
        print("Test 14 Exception:", e)

    # Test 15: contains()
    try:
        if hello.contains(MyString(list("ell"))):
            print("Test 15 Passed: contains()")
        else:
            print("Test 15 Failed: contains()")
    except Exception as e:
        print("Test 15 Exception:", e)

    # Test 16: index_of() for a character
    try:
        index = hello.index_of('l')  # expected first occurrence at index 2
        if index == 2:
            print("Test 16 Passed: index_of(char)")
        else:
            print("Test 16 Failed: index_of(char) expected 2 but got", index)
    except Exception as e:
        print("Test 16 Exception:", e)

    # Test 17: index_of_from() for a character
    try:
        index = hello.index_of_from('l', 3)  # expected 3
        if index == 3:
            print("Test 17 Passed: index_of_from(char, 3)")
        else:
            print("Test 17 Failed: index_of_from(char, 3) expected 3 but got", index)
    except Exception as e:
        print("Test 17 Exception:", e)

    # Test 18: index_of() for a substring
    try:
        sub_hello = MyString(list("lo"))
        index = hello.index_of(sub_hello)  # expected 3
        if index == 3:
            print("Test 18 Passed: index_of(MyString)")
        else:
            print("Test 18 Failed: index_of(MyString) expected 3 but got", index)
    except Exception as e:
        print("Test 18 Exception:", e)

    # Test 19: index_of_from() for a substring
    try:
        sub_hello2 = MyString(list("l"))
        index = hello.index_of_from(sub_hello2, 3)  # expected 3
        if index == 3:
            print("Test 19 Passed: index_of_from(MyString, 3)")
        else:
            print("Test 19 Failed: index_of_from(MyString, 3) expected 3 but got", index)
    except Exception as e:
        print("Test 19 Exception:", e)

    # Test 20: last_index_of() for a character
    try:
        last_index = hello.last_index_of('l')  # expected 3 (last occurrence)
        if last_index == 3:
            print("Test 20 Passed: last_index_of(char)")
        else:
            print("Test 20 Failed: last_index_of(char) expected 3 but got", last_index)
    except Exception as e:
        print("Test 20 Exception:", e)

    # Test 21: last_index_of_from() for a character
    try:
        last_index = hello.last_index_of_from('l', 2)  # expected 2
        if last_index == 2:
            print("Test 21 Passed: last_index_of_from(char, 2)")
        else:
            print("Test 21 Failed: last_index_of_from(char, 2) expected 2 but got", last_index)
    except Exception as e:
        print("Test 21 Exception:", e)

    # Test 22: last_index_of() for a substring
    try:
        sub_l = MyString(list("l"))
        last_index = hello.last_index_of(sub_l)  # expected 3
        if last_index == 3:
            print("Test 22 Passed: last_index_of(MyString)")
        else:
            print("Test 22 Failed: last_index_of(MyString) expected 3 but got", last_index)
    except Exception as e:
        print("Test 22 Exception:", e)

    # Test 23: last_index_of_from() for a substring
    try:
        sub_l2 = MyString(list("l"))
        last_index = hello.last_index_of_from(sub_l2, 2)  # expected 2
        if last_index == 2:
            print("Test 23 Passed: last_index_of_from(MyString, 2)")
        else:
            print("Test 23 Failed: last_index_of_from(MyString, 2) expected 2 but got", last_index)
    except Exception as e:
        print("Test 23 Exception:", e)

    # Test 24: is_empty()
    try:
        if empty.is_empty() and not hello.is_empty():
            print("Test 24 Passed: is_empty()")
        else:
            print("Test 24 Failed: is_empty()")
    except Exception as e:
        print("Test 24 Exception:", e)

    # Test 25: to_char_array()
    try:
        arr = hello.to_char_array()
        if ''.join(arr) == "Hello":
            print("Test 25 Passed: to_char_array()")
        else:
            print("Test 25 Failed: to_char_array()")
    except Exception as e:
        print("Test 25 Exception:", e)

    # Test 26: to_lower_case()
    try:
        mixed = MyString(list("HeLLo"))
        lower = mixed.to_lower_case()  # expected "hello"
        if str(lower) == "hello":
            print("Test 26 Passed: to_lower_case()")
        else:
            print("Test 26 Failed: to_lower_case()")
    except Exception as e:
        print("Test 26 Exception:", e)

    # Test 27: to_upper_case()
    try:
        mixed = MyString(list("HeLLo"))
        upper = mixed.to_upper_case()  # expected "HELLO"
        if str(upper) == "HELLO":
            print("Test 27 Passed: to_upper_case()")
        else:
            print("Test 27 Failed: to_upper_case()")
    except Exception as e:
        print("Test 27 Exception:", e)

    # Test 28: trim()
    try:
        spaced = MyString(list("   Hello World   "))
        trimmed = spaced.trim()  # expected "Hello World"
        if str(trimmed) == "Hello World":
            print("Test 28 Passed: trim()")
        else:
            print("Test 28 Failed: trim()")
    except Exception as e:
        print("Test 28 Exception:", e)

    # Test 29: starts_with()
    try:
        if hello.starts_with(MyString(list("He"))) and not hello.starts_with(MyString(list("lo"))):
            print("Test 29 Passed: starts_with()")
        else:
            print("Test 29 Failed: starts_with()")
    except Exception as e:
        print("Test 29 Exception:", e)

    # Test 30: starts_with_from()
    try:
        if hello.starts_with_from(MyString(list("ll")), 2):
            print("Test 30 Passed: starts_with_from()")
        else:
            print("Test 30 Failed: starts_with_from()")
    except Exception as e:
        print("Test 30 Exception:", e)

    # Test 31: split()
    try:
        csv = MyString(list("a,b,c"))
        parts = csv.split(MyString(list(",")))
        if len(parts) == 3 and str(parts[0]) == "a" and str(parts[1]) == "b" and str(parts[2]) == "c":
            print("Test 31 Passed: split()")
        else:
            print("Test 31 Failed: split()")
    except Exception as e:
        print("Test 31 Exception:", e)

    # Test 32: split_limit()
    try:
        data = MyString(list("one,two,three,four"))
        parts = data.split_limit(MyString(list(",")), 3)
        if (len(parts) == 3 and str(parts[0]) == "one" and
            str(parts[1]) == "two" and str(parts[2]) == "three,four"):
            print("Test 32 Passed: split_limit()")
        else:
            print("Test 32 Failed: split_limit()")
    except Exception as e:
        print("Test 32 Exception:", e)

    print("----- Testing Completed -----")

main()
