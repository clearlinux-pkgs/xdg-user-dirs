#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xdg-user-dirs
Version  : 0.17
Release  : 10
URL      : https://user-dirs.freedesktop.org/releases/xdg-user-dirs-0.17.tar.gz
Source0  : https://user-dirs.freedesktop.org/releases/xdg-user-dirs-0.17.tar.gz
Summary  : Manage user directories like ~/Desktop and ~/Music
Group    : Development/Tools
License  : GPL-2.0
Requires: xdg-user-dirs-bin = %{version}-%{release}
Requires: xdg-user-dirs-data = %{version}-%{release}
Requires: xdg-user-dirs-license = %{version}-%{release}
Requires: xdg-user-dirs-locales = %{version}-%{release}
Requires: xdg-user-dirs-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt
BuildRequires : m4
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
Patch1: 0001-Convert-to-a-stateless-configuration.patch

%description
See info at:
http://freedesktop.org/wiki/Software/xdg-user-dirs

%package bin
Summary: bin components for the xdg-user-dirs package.
Group: Binaries
Requires: xdg-user-dirs-data = %{version}-%{release}
Requires: xdg-user-dirs-license = %{version}-%{release}

%description bin
bin components for the xdg-user-dirs package.


%package data
Summary: data components for the xdg-user-dirs package.
Group: Data

%description data
data components for the xdg-user-dirs package.


%package license
Summary: license components for the xdg-user-dirs package.
Group: Default

%description license
license components for the xdg-user-dirs package.


%package locales
Summary: locales components for the xdg-user-dirs package.
Group: Default

%description locales
locales components for the xdg-user-dirs package.


%package man
Summary: man components for the xdg-user-dirs package.
Group: Default

%description man
man components for the xdg-user-dirs package.


%prep
%setup -q -n xdg-user-dirs-0.17
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557104150
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557104150
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-user-dirs
cp COPYING %{buildroot}/usr/share/package-licenses/xdg-user-dirs/COPYING
%make_install
%find_lang xdg-user-dirs

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xdg-user-dir
/usr/bin/xdg-user-dirs-update

%files data
%defattr(-,root,root,-)
/usr/share/xdg/autostart/xdg-user-dirs.desktop
/usr/share/xdg/user-dirs.conf
/usr/share/xdg/user-dirs.defaults

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-user-dirs/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xdg-user-dir.1
/usr/share/man/man1/xdg-user-dirs-update.1
/usr/share/man/man5/user-dirs.conf.5
/usr/share/man/man5/user-dirs.defaults.5
/usr/share/man/man5/user-dirs.dirs.5

%files locales -f xdg-user-dirs.lang
%defattr(-,root,root,-)

