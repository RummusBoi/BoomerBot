SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/python"
echo $SOURCE
docker run -itv $SOURCE:/proj/python pythoninstall /bin/bash