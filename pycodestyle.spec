#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycodestyle
Version  : 2.3.1
Release  : 8
URL      : http://pypi.debian.net/pycodestyle/pycodestyle-2.3.1.tar.gz
Source0  : http://pypi.debian.net/pycodestyle/pycodestyle-2.3.1.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pycodestyle-bin
Requires: pycodestyle-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
pycodestyle (formerly called pep8) - Python style guide checker
===============================================================

%package bin
Summary: bin components for the pycodestyle package.
Group: Binaries

%description bin
bin components for the pycodestyle package.


%package python
Summary: python components for the pycodestyle package.
Group: Default

%description python
python components for the pycodestyle package.


%prep
%setup -q -n pycodestyle-2.3.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487206504
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1487206504
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycodestyle

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
