#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
    opening_brackets = dict(zip(brackets[0::2], brackets[1::2]))
    closing_brackets = dict(zip(brackets[1::2], brackets[0::2]))
    listBrakets = []
    for chr in text:
        if chr in opening_brackets:
            listBrakets.append(chr)
        elif chr in closing_brackets:
            if (len(listBrakets) == 0) or (listBrakets[-1] != closing_brackets[chr]):

                return False
            else:
                listBrakets.pop()
    check = len(listBrakets) == 0
   
    return check

def remove_comments(full_text, comment_start, comment_end):
    if comment_start in full_text:
        firstPart = full_text.replace(comment_start, "")
        if comment_end in full_text:
            secondPart = firstPart.replace(comment_end, "").split(" ")
        else:
         return None
    elif comment_end not in full_text:
        return full_text
    else:
        return None
    comment = secondPart[0] + secondPart[-1]
    return comment



def get_tag_prefix(text, opening_tags, closing_tags):
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	return False


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

