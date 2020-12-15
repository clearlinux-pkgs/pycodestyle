#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycodestyle
Version  : 2.6.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/bb/82/0df047a5347d607be504ad5faa255caa7919562962b934f9372b157e8a70/pycodestyle-2.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/82/0df047a5347d607be504ad5faa255caa7919562962b934f9372b157e8a70/pycodestyle-2.6.0.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pycodestyle-bin = %{version}-%{release}
Requires: pycodestyle-license = %{version}-%{release}
Requires: pycodestyle-python = %{version}-%{release}
Requires: pycodestyle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-python

%description
===============================================================

%package bin
Summary: bin components for the pycodestyle package.
Group: Binaries
Requires: pycodestyle-license = %{version}-%{release}

%description bin
bin components for the pycodestyle package.


%package license
Summary: license components for the pycodestyle package.
Group: Default

%description license
license components for the pycodestyle package.


%package python
Summary: python components for the pycodestyle package.
Group: Default
Requires: pycodestyle-python3 = %{version}-%{release}

%description python
python components for the pycodestyle package.


%package python3
Summary: python3 components for the pycodestyle package.
Group: Default
Requires: python3-core
Provides: pypi(pycodestyle)

%description python3
python3 components for the pycodestyle package.


%prep
%setup -q -n pycodestyle-2.6.0
cd %{_builddir}/pycodestyle-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589235621
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover testsuite -vv
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycodestyle
cp %{_builddir}/pycodestyle-2.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pycodestyle/0b3a0b386cf2762bc7b475c9855cdec47dd70a38
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pycodestyle

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycodestyle/0b3a0b386cf2762bc7b475c9855cdec47dd70a38

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
