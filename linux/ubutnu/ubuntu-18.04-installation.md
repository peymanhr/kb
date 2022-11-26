# Ubuntu 18.04 Desktop Installation

## Change default repository

```bash
sudo cp /etc/apt/sources.list{,.original}
sudo set -i 's/ir.ar/us.ar/g' /etc/apt/sources.list
sudo apt update
sudo apt upgrade
sudo apt install vim openssh-server lvm2 mdadm cifs-utils reiserfsprogs jfsutils btrfs-tools xfsprogs xfsdump screen socat stunnel4 proxychains redsocks tsocks curl git python-pip python3-pip python3-venv
```

## Add .vimrc file
```bash
cat <<EOF > ~.vimrc
" Environment {
    set nocompatible    " Must be first line. Disable vi compatibality 
    set background=dark " Assume a dark background
" }

" Formatting {
    set nowrap          " Disable text wrapping
    set shiftwidth=4    " Use indet of 4 spaces
    set expandtab       " Use spaces instead of tabs
    set tabstop=4       " An indentation every 4 columns
    set softtabstop=4   " Let backspace delete indent
    
" }

" General {
    syntax on           " Syntax highlighting
    set autowrite       " Automatically write a file when leaving a modified buffer
    set history=1000    " Store a ton of history. Default is 20
    set showmode        " Show current mode
    set showcmd         " Show partial command
    set ruler           " Show ruler    
    set linespace=0     " Line spacing
    set nu              " Show line numbers
    set incsearch       " Find as you type search
    set hlsearch        " Highlight search terms
    set ignorecase      " Case insensitive search
    set wildmenu        " Show list instead of completing
    set wildmode=list:longest,full
    set scrolloff=3     " Minimum lines to keep above and below cursor
    set scrolljump=5    " lines to scroll when cursor leaves screen
" }

" Key (re)Mappings {
    nnoremap Y y$         " Yank from cursor to the end of line
" }


" Remember last position(.viminfo must be writable) {
    set viminfo='10,\"100,:20,%,n~/.viminfo
    function! ResCur()
        if line("'\"") <= line("$")
            normal! g`"
            return 1
        endif
    endfunction
    augroup resCur
        autocmd!
        autocmd BufWinEnter * call ResCur()
    augroup END
" }
EOF
```

## Midding Packages:

- **net-tools**: *netstat,ifconfig,arp,route,arp,iptunnel, nameif,iwconfig*