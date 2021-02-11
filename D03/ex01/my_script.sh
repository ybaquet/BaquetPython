python3.8 -m pip --version
CURRENT=`pwd`
LOCAL_DIR=/Users/yde-mont/Desktop/ECLIPSE/workspace/PYTHON/42Python/D03/ex01/rendu/local_dir
if [ -e ${LOCAL_DIR}]
then
	rm -rf ${LOCAL_DIR}
fi
mkdir ${LOCAL_DIR}
cd ${LOCAL_DIR}
python3.8 -m pip install git+https://github.com/jaraco/path --target=. > ${LOCAL_DIR}/install_path.log
cd ${CURRENT}