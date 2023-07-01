import argparse


def hello_world():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", nargs="?", default="world", help="Name to greet")
    args = parser.parse_args()

    print(f"Hello, {args.name}!")