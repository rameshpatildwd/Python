# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.

Common Regex Shorthand Characters
Pattern	Meaning	Example Match
\d	Matches any digit (0-9)	"123" in "Order 123"
\D	Matches any non-digit	"Order" in "Order 123"
\w	Matches any word character (letters, digits, underscore _)	"Hello_123" in "Hello_123!"
\W	Matches any non-word character (symbols, spaces, etc.)	"!" in "Hello!"
\s	Matches any whitespace (spaces, tabs, newlines)	Space in "Hello world"
\S	Matches any non-whitespace	"Hello" in "Hello world"