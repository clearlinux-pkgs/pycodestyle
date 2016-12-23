#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycodestyle
Version  : 2.0.0
Release  : 2
URL      : http://pypi.debian.net/pycodestyle/pycodestyle-2.0.0.tar.gz
Source0  : http://pypi.debian.net/pycodestyle/pycodestyle-2.0.0.tar.gz
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
%setup -q -n pycodestyle-2.0.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycodestyle

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
