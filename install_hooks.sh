#!/bin/bash

HOOKS_DIR=".git/hooks"
mkdir -p "$HOOKS_DIR"
cp scripts/hooks/commit-msg "$HOOKS_DIR/commit-msg"
chmod +x "$HOOKS_DIR/commit-msg"

echo "✅ Git hook installed!"