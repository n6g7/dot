import os.path

from ..print import print_line


def add(manager, args):
    for file in args.files:
        abs_path = os.path.abspath(file)
        manager.add(abs_path)
        print_line("🔗  Added {:green}", os.path.relpath(abs_path, manager.target_dir))
