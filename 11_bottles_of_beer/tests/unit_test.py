from bottles import verse


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == "\n".join(
        [
            "1 bottle of beer on the wall,",
            "1 bottle of beer,",
            "Take one down, pass it around,",
            "No more bottles of beer on the wall!",
        ]
    )

    two_bottles = verse(2)
    assert two_bottles == "\n".join(
        [
            "2 bottles of beer on the wall,",
            "2 bottles of beer,",
            "Take one down, pass it around,",
            "1 bottle of beer on the wall!",
        ]
    )
