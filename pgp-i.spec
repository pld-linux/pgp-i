Summary:     PGP File/email encryption tool
Summary(pl): PGP - narzêdzia do kodowania danych i poczty elektronicznej
Name:        pgp
Version:     5.0i
Release:     2
Copyright:   free for non-commerical use
Group:       Utilities/File
Source:      ftp://ftp.ifi.uio.no/pub/pgp/5.0/international/unix/%{name}50i-unix-src.tar.gz
Patch:       %{name}50i-64bit-fix.diff
URL:         http://www.pgpi.com/
BuildRoot:   /tmp/%{name}-%{version}-%{release}-root

%description
The PGP encryption suite is the defacto standard for Internet email
encryption. See "man 7 pgp-intro" for more details.

%description -l pl
Pakiet zawiera pgp - aplikacjê która jest defacto standardem dla kodowania
poczty elektronicznej (email), jak równie¿ mo¿e byc u¿ywany do kodowania 
danych.

%package static
Summary:     PGP static library
Summary(pl): Biblioteki statyczne dla PGP
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description static
This package contains the PGP static libraries.

%description -l pl static
Pakiet zawiera biblioteki statyczne dla PGP

%prep 
%setup -q -n %{name}50i
%ifarch alpha
%patch -p0
%endif

%build
cd src
./configure \
	--prefix=$RPM_BUILD_ROOT/usr
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin

cd src
make install

rm -f $RPM_BUILD_ROOT/usr/bin/pgp_old
rm -f plugins/Makefil*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README WELCOME src/README src/language50.txt
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man[157]/*

%files static
%attr(644, root, root) /usr/lib/*.a

%changelog
* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.0i-2]
- fixed passing $RPM_OPT_FLAGS,
- removed src/plugins from %doc.

* Sat Aug 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.0i-1]
- added pl translation,
- added static package,
- minor modifications of spec file.

* Sat Apr 18 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Added BuildRoot
- Minor spec file and install script improvements
