Summary:	PGP File/email encryption tool
Summary(pl):	PGP - narzêdzia do kodowania danych i poczty elektronicznej
Name:		pgp
Version:	5.0i
Release:	3
Copyright:	free for non-commerical use
Group:		Utilities/System
Group(pl):	Narzêdzia/System
#######		ftp://ftp.ifi.uio.no/pub/pgp/5.0/international/unix
Source:		%{name}50i-unix-src.tar.gz
Patch0:		%{name}50i-64bit-fix.diff
Patch1:		%{name}-lang.patch
URL:		http://www.pgpi.com/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The PGP encryption suite is the defacto standard for Internet email
encryption. See "man 7 pgp-intro" for more details.

%description -l pl
Pakiet zawiera pgp - aplikacjê, która jest defacto standardem dla kodowania
poczty elektronicznej (email), jak równie¿ mo¿e byæ u¿ywana do kodowania 
danych.

%package	static
Summary:	PGP static library
Summary(pl):	Biblioteki statyczne dla PGP
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
This package contains the PGP static libraries.

%description -l pl static
Pakiet zawiera biblioteki statyczne dla PGP.

%prep 
%setup  -q -n %{name}50i

%ifarch alpha
%patch -p0
%endif

%patch1 -p1

%build
cd src
%configure

make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
mv README README-PGP

cd src
make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    libdir=$RPM_BUILD_ROOT%{_libdir} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    install

rm -f $RPM_BUILD_ROOT%{_bindir}/pgp_old
strip $RPM_BUILD_ROOT%{_bindir}/{pgp,pgpk}

cd ..
gzip -9nf README-PGP WELCOME src/language50.txt \
	$RPM_BUILD_ROOT%{_mandir}/man[157]/* src/plugins/{README,README-PINE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README-PGP,WELCOME}.gz src/language50.txt.gz
%doc src/plugins/*.gz

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[157]/*

%files static
%defattr(644,root,root,755) 

%{_libdir}/*.a

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
