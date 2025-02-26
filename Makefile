install:
	uv sync

brain-games:
	uv brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl