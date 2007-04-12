%define module	forest_utils
%define name	perl-%{module}
%define version	0.07
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module to convert between various formats for shared derivation forest
License:	GPL
Group:		Sciences/Computer science
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{module}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#forest_utils
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-libxml-perl
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}
Obsoletes:	perl-Forest
Provides:	perl-Forest

%description
forest_utils is a set of Perl scripts to convert between various formats for
shared derivation forest produced by parsers for Tree Adjoining Grammars [TAG].

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{perl_vendorlib}/*.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/Forest*
%{_mandir}/*/*

