import argparse
import random   

# I will be learning about the argparse 

# parser = argparse.ArgumentParser(description="learning about argparse")
# parser.add_argument("-name", help="enter your name")


# args = parser.parse_args()
# print(f"Your name: {args.name}")

# challange1

# parser = argparse.ArgumentParser(description="Takes your name")
# parser.add_argument('name', help="Your name")
# parser.add_argument('-u','--upper',action="store_true", help="This just turns your things to upper case")

# args = parser.parse_args()
# if args.upper:
#     print(f"HELLO {args.name.upper()}")
# else:
#     print(f"Hello {args.name}")


# 🟢 Challenge 2 — EASY

# I will create a cli that takes a number as your age
# parser = argparse.ArgumentParser(description="I will creat a CLI for taking age")
# parser.add_argument('--age', type=int, required=True, help="This is your age")

# args = parser.parse_args()
# print(f"You are {args.age} years old.")


# 🟡 Challenge 3 — EASY ➜ MEDIUM

# parser = argparse.ArgumentParser(description="This parser is for addition of 2 numbers")
# parser.add_argument("numbers", help="x value for addition", type=int, nargs='+' )
# # parser.add_argument("y", help="y value for addition", type=int,)

# # def addition(x,y):
# #     return x+y
# args = parser.parse_args()

# print(f"Result: {sum(args.numbers)}")


# 🟡 Challenge 4 — MEDIUM (Flags)
# parser = argparse.ArgumentParser(description="This parser is expected to reverse your text")
# parser.add_argument("text",help="Your text")
# parser.add_argument("--reverse", help="This flag reverses your text", action="store_true")

# args = parser.parse_args()

# if args.reverse:
#     print(f"{args.text[::-1]}")
# else:
#     print(args.text)


# 🔵 Challenge 5 — MEDIUM (Choices + Logic)
parser = argparse.ArgumentParser(description="This one is all about choices")
parser.add_argument("--score", help="Your score",required=True)
parser.add_argument("--grade", help="Your grade A,B,C", required=True, choices=["A","B", "C"])

args = parser.parse_args()

print(f"Score: {args.score} | Grade {args.grade}")