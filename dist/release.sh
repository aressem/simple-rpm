#!/bin/bash
set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

readonly VERSION=$1

git checkout master
git push origin :rpmbuild &> /dev/null || true
git branch -D rpmbuild &> /dev/null || true 
git checkout -b rpmbuild $VERSION
git mv dist/simple.spec .
tito init
tito tag --use-version=$VERSION --no-auto-changelog
git push -u origin --follow-tags rpmbuild
git checkout master

