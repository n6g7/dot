#!/usr/bin/env python3
from src.commands import add, deploy
from src.manager import Manager
import argparse
import os

home = os.getenv('HOME')
default_source = os.path.join(home, '.dotfiles')
default_target = home


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage your dotfiles')
    parser.add_argument(
        '--source',
        nargs='?',
        default=default_source,
        help='The source directory to use'
    )
    parser.add_argument(
        '--home',
        nargs='?',
        default=default_target,
        help='Your home directory'
    )

    subparsers = parser.add_subparsers(title='subcommand')

    add_parser = subparsers.add_parser(
        'add',
        help='add a new dotfile',
        aliases=['a']
    )
    add_parser.add_argument(
        'files',
        nargs='+',
        help='the files to add'
    )
    add_parser.set_defaults(func=add)

    deploy_parser = subparsers.add_parser(
        'deploy',
        help='deploy dotfiles',
        aliases=['d']
    )
    deploy_parser.set_defaults(func=deploy)

    args = parser.parse_args()
    manager = Manager(args.source, args.home)
    args.func(manager, args)
