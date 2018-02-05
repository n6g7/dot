# dot

A dotfiles manager.

- Store your files in a single directory (`~/.dotfiles` by default) ;
- Sync this directory accross machines (using eg. git, dropbox, keybase, syncthing, etc) ;
- Use `dot` to automatically create symbolic links to your files.

## Usage

### Link files in `~/.dotfiles`

Creates symbolic links from `~/.dotfiles/*` to `~/.*`.
```sh
$ dot deploy
```

### Save a file

Copies `~/.my.dotfile` to `~/.dotfiles/my.dotfile` and creates a symbolic link from `~/.my.dotfile`.
```sh
$ dot add ~/.my.dotfile
```
