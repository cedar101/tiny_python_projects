from textwrap import dedent

from twelve_days import verse


# --------------------------------------------------
def test_verse():
    """Test verse"""

    assert verse(1) == dedent(
        """\
        On the first day of Christmas,
        My true love gave to me,
        A partridge in a pear tree."""
    )

    assert verse(2) == dedent(
        """\
        On the second day of Christmas,
        My true love gave to me,
        Two turtle doves,
        And a partridge in a pear tree."""
    )
