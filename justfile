exec *name:
  scheme --quiet < $(find . -name {{name}}.scm)
