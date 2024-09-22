# Task - 01 [Dictionary]


# Task - 01 : 1

courses = {
    "CSE101" : {
        "course_name" : "Introduction to Programming",
        "course_credits" : 3,
        "course_instructor" : "Dr. Alice"
    },
    "CSE102" : {
        "course_name" : "Data Structures",
        "course_credits" : 4,
        "course_instructor" : "Dr. Bob"
    },
    "CSE103" : {
        "course_name" : "Database Systems",
        "course_credits" : 3,
        "course_instructor" : "Dr. Carol"
    }
}


# Task - 01 : 2

courses["CSE102"]["course_instructor"] = "Dr. Bob Jr."



# Task - 01 : 3

courses["CSE104"] = {
    "course_name" : "Algorithms",
    "course_credits" : 4,
    "course_instructor" : "Dr. Dave"
}


# Task - 01 : 4

courses.pop("CSE101")



# Task - 01 : 5

for course_code, details in courses.items():
    print(course_code, ":", details)



# Task - 02 [String]

# Task 02 : a

sentence = "Learning Python is fun and rewarding."
print(sentence[-28:-14])


# Task 02 : b

new_sentence = sentence.replace("rewarding", "exciting")
print(new_sentence)


# Task 02 : c

# finding the index where exciting ends

pos = new_sentence.find("exciting.") + len("exciting.")

# using slicing + concatenation to find the final sentence

final_sentence = new_sentence[:pos] + " Keep practicing!" + new_sentence[pos:]

print(final_sentence)


# Task 02 : d

final_sentence = final_sentence.title()
print(final_sentence)





# Task 03 [List]

# Task - 03 : a

customers = ["Alice", "Bob", "Charlie", "David", "Eve"]
third_customer_name = customers[2]
print(third_customer_name)


# Task - 03 : b

customers[1] = "Ben"


# Task - 03 : c

customers.append("Frank")


# Task - 03 : d

customers.remove("David")


# Task - 03 : e

customers.sort()
print(customers)



# Task - 04 [Control FLow]

# Task 04 : a

grades = [85, 78, 92, 45, 33, 67, 88, 41]

for i in grades:
    print("Score:", i , end = " ")
    if(i > 80):
        print("Grade A")
    elif(i >= 60 and i <= 80):
        print("Grade B")
    elif(i >= 40 and i <= 60):
        print("Grade C")
    else:
        print("Grade F")


# Task 04 : b

grades = [85, 78, 92, 45, 33, 67, 88, 41]

def boost_grades(score):
    return score + score * 0.05

boost_grades = list(map(boost_grades, grades))

print("New Grades after 5% increase:", boost_grades)


# Task 04 : c

grades_above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("Boosted Grades Above 90:")
print(grades_above_90)



# Task - 05 [Tuple & Set]


# Task 05 : a

books = (("To Kill a Mockingbird", "Harper Lee", 1960),("1984", "George Orwell", 1949), ("The Great Gatsby", "F. Scott Fitzgerald", 1925))

tags = {"classic", "dystopian", "novel", "literature"}

lst = list(books)
print(lst[1][1])


# Task 05 : b

lst.append(("Brave New World", "Aldus Huxley", 1932))
books = tuple(lst)
print(books)

# Task 05 : c

third_book_name = lst[2][0]
third_book_author = lst[2][1]
third_book_year = lst[2][2]
print("Information of third books:")
print("Name:", third_book_name)
print("Author:", third_book_author)
print("Publication Year:", third_book_year)


# Task 05 : d

print("Title of all the books:")
for i in books:
    print(i[0])


# Task 05 : e

tags.add("sci-fi")
print("all tags: ", tags)


# Task 05 : f

def remove_from_set(st):
    st.remove("novel")
    return st

updated_tags = remove_from_set(tags)
print("Updated Tags: ", updated_tags)


