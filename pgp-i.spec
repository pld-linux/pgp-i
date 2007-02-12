Summary:	PGP File/email encryption tool
Summary(pl.UTF-8):   PGP - narzędzia do kodowania danych i poczty elektronicznej
Name:		pgp
Version:	5.0i
Release:	4
License:	Free for non-commerical use
Group:		Applications/System
Source0:	ftp://ftp.ifi.uio.no/pub/pgp/5.0/unix/%{name}50i-unix-src.tar.gz
# Source0-md5:	7a01203f0053aa78a781367461d52187
Patch0:		%{name}50i-64bit-fix.diff
Patch1:		%{name}-lang.patch
Patch2:		%{name}-remove_broken_asm.patch
URL:		http://www.pgpi.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PGP encryption suite is the defacto standard for Internet email
encryption. See "man 7 pgp-intro" for more details.

%description -l pl.UTF-8
Pakiet zawiera pgp - aplikację, która jest defacto standardem dla
kodowania poczty elektronicznej (email), jak również może być używana
do kodowania danych.

%package static
Summary:	PGP static library
Summary(pl.UTF-8):   Biblioteki statyczne dla PGP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
This package contains the PGP static libraries.

%description static -l pl.UTF-8
Pakiet zawiera biblioteki statyczne dla PGP.

%prep
%setup -q -n %{name}50i

%ifarch alpha
%patch0 -p0
%endif

%patch1 -p1
%patch2 -p1

%build
cd src
%configure2_13

%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
mv -f README README-PGP

cd src
%{__make} \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	install

rm -f $RPM_BUILD_ROOT%{_bindir}/pgp_old

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-PGP WELCOME src/language50.txt src/plugins/{README,README-PINE}
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[157]/*

%files static
%defattr(644,root,root,755)

%{_libdir}/*.a
