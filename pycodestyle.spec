#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycodestyle
Version  : 2.3.1
Release  : 27
URL      : http://pypi.debian.net/pycodestyle/pycodestyle-2.3.1.tar.gz
Source0  : http://pypi.debian.net/pycodestyle/pycodestyle-2.3.1.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pycodestyle-bin
Requires: pycodestyle-legacypython
Requires: pycodestyle-python3
Requires: pycodestyle-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-python

%description
===============================================================

%package bin
Summary: bin components for the pycodestyle package.
Group: Binaries

%description bin
bin components for the pycodestyle package.


%package legacypython
Summary: legacypython components for the pycodestyle package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pycodestyle package.


%package python
Summary: python components for the pycodestyle package.
Group: Default
Requires: pycodestyle-python3

%description python
python components for the pycodestyle package.


%package python3
Summary: python3 components for the pycodestyle package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pycodestyle package.


%prep
%setup -q -n pycodestyle-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526509006
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1526509006
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycodestyle

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
