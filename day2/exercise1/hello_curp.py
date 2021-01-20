import argparse
import os


def get_user_name():
    name = os.getenv('USER')
    if name is None:
        name = os.getenv('USERNAME')
    return name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type=str, default=None)

    args = parser.parse_args()

    if args.user is None:
        print(f'Hi! Are you {get_user_name()}?')
    else:
        print(f'Hi, {args.user}!')


if __name__ == '__main__':
    main()
