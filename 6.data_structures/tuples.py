# inmutable
langs = ("Python", "JavaScript", "Go", "Java", "Scala", "Perl", "Rust", "C", "C++")

counter = 0
while counter < len(langs):
    print(langs[counter])
    counter += 1

to_list = list(langs)
to_list.pop()
print(to_list)
to_list.append("TypeScript")
print(to_list)
