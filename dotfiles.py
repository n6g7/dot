#!/usr/bin/env python3
from src.commands import add, deploy
from src.manager import Manager
import argparse
import os

cwd = os.getcwd()
source_dir = os.path.join(cwd, 'files')
target_dir = os.getenv('HOME')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage your dotfiles')
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

    # parser.add_argument(
    #     'file',
    #     nargs='?',
    #     default='dotfiles.json',
    #     help='Your dotfiles manifest file.',
    #     type=argparse.FileType('r')
    # )
    # parser.add_argument('-a', '--add', nargs='+')
    # parser.add_argument('-d', '--delete', nargs='+')

    args = parser.parse_args()
    manager = Manager(source_dir, target_dir)
    args.func(manager, args)
