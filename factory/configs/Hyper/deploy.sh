if git diff --quiet .
then
  PREV_VERSION="$(npm show hyper-sublette version 2>/dev/null || echo 0.0.0)"

  MAJOR="$(echo "$PREV_VERSION" | awk -F. '{ print $1 }')"
  MINOR="$(echo "$PREV_VERSION" | awk -F. '{ print $2 }')"
  PATCH="$(echo "$PREV_VERSION" | awk -F. '{ print $3 }')"

  VERSION="$MAJOR.$MINOR.$((PATCH+1))"
  sed -i "s/#VERSION#/$VERSION/g" package.json

  npm publish
fi
