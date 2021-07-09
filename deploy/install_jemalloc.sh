export JEMALLOC_VER=5.2.1
apt update
apt install -y gcc make autoconf git
mkdir build
cd build
git clone https://github.com/jemalloc/jemalloc.git
cd jemalloc
./autogen.sh
make dist
make -j $(nproc)
make install
ldconfig
cd /