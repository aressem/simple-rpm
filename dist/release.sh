#!/bin/sh

readonly VERSION=$1

git push origin :rpmbuild || true
git branch -D rpmbuild || true 
git checkout -b rpmbuild
git mv dist/simple.spec .
tito init
tito tag --use-version=$VERSION --no-auto-changelog
git push -u origin --follow-tags rpmbuild

