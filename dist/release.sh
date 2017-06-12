#!/bin/bash
set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

readonly VERSION=$1
readonly RPM_BRANCH="rpmbuild"
readonly CURRENT_BRANCH=$(git branch | grep "^\*" | cut -d' ' -f2)

git checkout $RPM_BRANCH
git reset --hard $VERSION
git mv dist/simple.spec .
tito init
tito tag --use-version=$VERSION --no-auto-changelog
git push --follow-tags
git checkout $CURRENT_BRANCH

