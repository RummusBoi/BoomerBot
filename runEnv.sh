ABSOLUTE_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
docker run -itv $SOURCE:/python pythoninstall /bin/bash