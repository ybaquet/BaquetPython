python3.8 -m pip --version
CURRENT=`pwd`
LOCAL_DIR=./rendu/local_dir
if [ -z ${LOCAL_DIR} ]
then
	rm -rf ${LOCAL_DIR}
fi
mkdir -p ${LOCAL_DIR}
cd ${LOCAL_DIR}
python3.8 -m pip install git+https://github.com/jaraco/path --target=. > ./install_path.log
cd ${CURRENT}