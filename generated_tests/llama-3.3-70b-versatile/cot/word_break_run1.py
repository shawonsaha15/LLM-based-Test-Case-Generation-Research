class TestWordBreak:
    def test_normal_input(self):
        assert word_break("leetcode", ["leet", "code"]) is True
        assert word_break("applepenapple", ["apple", "pen"]) is True
        assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False

    def test_empty_input(self):
        assert word_break("", ["a", "b"]) is True
        assert word_break("", []) is True

    def test_zero_length_word(self):
        assert word_break("a", ["", "a"]) is True
        assert word_break("a", [""]) is False

    def test_none_input(self):
        try:
            word_break(None, ["a", "b"])
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_none_word_dict(self):
        try:
            word_break("a", None)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_large_input(self):
        large_string = "a" * 100
        large_word_dict = ["a"] * 100
        assert word_break(large_string, large_word_dict) is True

    def test_invalid_input_type(self):
        try:
            word_break(123, ["a", "b"])
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_invalid_word_dict_type(self):
        try:
            word_break("a", "abc")
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_malformed_word_dict(self):
        try:
            word_break("a", [1, 2, 3])
            assert False, "Expected TypeError"
        except TypeError:
            pass