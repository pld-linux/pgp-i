Summary:     PGP File/email encryption tool
Summary(pl): PGP - narzêdzia do kodowania danych i poczty elektronicznej
Name:        pgp
Version:     5.0i
Release:     2
Copyright:   free for non-commerical use
Group:       Utilities/File
Group(pl):   Narzêdzia/Pliki
Source:      ftp://ftp.ifi.uio.no/pub/pgp/5.0/international/unix/%{name}50i-unix-src.tar.gz
Patch:       %{name}50i-64bit-fix.diff
URL:         http://www.pgpi.com/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The PGP encryption suite is the defacto standard for Internet email
encryption. See "man 7 pgp-intro" for more details.

%description -l pl
Pakiet zawiera pgp - aplikacjê, która jest defacto standardem dla kodowania
poczty elektronicznej (email), jak równie¿ mo¿e byæ u¿ywana do kodowania 
danych.

%package static
Summary:     PGP static library
Summary(pl): Biblioteki statyczne dla PGP
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki
Requires:    %{name} = %{version}

%description static
This package contains the PGP static libraries.

%description -l pl static
Pakiet zawiera biblioteki statyczne dla PGP.

%prep 
%setup -q -n %{name}50i
%ifarch alpha
%patch -p0
%endif

%build
cd src
./configure %{_target_platform} \
	--prefix=$RPM_BUILD_ROOT/usr
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cd src
make install

rm -f $RPM_BUILD_ROOT%{_bindir}/pgp_old

cd ..
gzip -9nf README WELCOME src/README src/language50.txt \
	$RPM_BUILD_ROOT%{_mandir}/man[157]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,WELCOME,src/README,src/language50.txt}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[157]/*

%files static
%attr(644,root,root) %{_libdir}/*.a

%changelog
* Sun Apr  4 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [5.0i-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added Group(pl),
- added gzipping documentation and man pages,
- removed man group from man pages,
- removed 'rm -f plugins/Makefil*' from %install,
- cosmetic changes for common l&f.

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
