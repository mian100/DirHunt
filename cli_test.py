import argparse

parser = argparse.ArgumentParser(
    description="DirHunt - Local Lab Tool"
)

parser.add_argument("-u", required=True, help="Lab URL")
parser.add_argument("-w", required=True, help="Wordlist")
parser.add_argument("-t", type=int, default=1)
parser.add_argument("-o", default="results.txt")

args = parser.parse_args()

report = (
    "=== DirHunt Configuration ===\n"
    f"URL: {args.u}\n"
    f"Wordlist: {args.w}\n"
    f"Workers: {args.t}\n"
)

print(report)

with open(args.o, "w") as file:
    file.write(report)

print("Report saved:", args.o)
