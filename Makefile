COMPONENT?=mulefactory
TMP_HOOKS:=/tmp/.${COMPONENT}_hooks.empty_target
VERSION:=src/${COMPONENT}/version.py
SCRIPTS_DIR:=scripts

include make/common.mk

include make/install.mk
include make/test.mk
include make/run.mk
include make/help.mk
include make/clean.mk
include make/lint.mk
include make/format.mk
include make/ci.mk

.DEFAULT:help
