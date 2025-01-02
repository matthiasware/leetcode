"""
271. String Encode and Decode

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode.

Constraints:
-) 0 <= strs.length < 100
-) 0 <= strs[i].length < 200
-) strs[i] contains only UTF-8 characters.

"""


def encode(strs: list[str]) -> str:
    return "".join([f"{len(s):03d}{s}" for s in strs])


def decode(string: str) -> list[str]:
    lst = []
    while string:
        sub_str_len = int(string[:3])
        sub_str = string[3: 3 + sub_str_len]
        lst.append(sub_str)
        string = string[3 + sub_str_len:]
    return lst


tests = [
    ([]),
    (["neet", "code", "love", "you"]),
    (["we", "say", ":", "yes"]),
    (
        [
            "The quick brown fox",
            "jumps over the",
            "lazy dog",
            "1234567890",
            "abcdefghijklmnopqrstuvwxyz",
        ]
    ),
]

if __name__ == "__main__":
    for test in tests:
        enc = encode(test)
        dec = decode(enc)
        assert dec == test
