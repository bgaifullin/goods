export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

export REMOTE_MACHINE=

function srcsync() {
  local SRC=$(basename $1)
  rsync -rzl --exclude '*.git*' --exclude '*.tox*' --exclude '*.idea*'  --delete ${SRC} ${REMOTE_MACHINE}:inbox/
}
